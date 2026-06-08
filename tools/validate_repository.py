#!/usr/bin/env python3
"""Validate research repository structure and metadata.

This script is intentionally lightweight and dependency-free. It checks Markdown
files for frontmatter, canonical IDs, lifecycle values and basic link/reference
integrity.

By default it validates repository content notes and skips templates,
documentation, migration notes and inbox notes. This keeps normal validation
focused on real research objects rather than examples or scaffolding.

Run from the repository root:

    python3 tools/validate_repository.py

Use --warnings-as-errors when the repository is ready for stricter CI use:

    python3 tools/validate_repository.py --warnings-as-errors
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_DIRS = {
    ".git",
    ".obsidian",
    ".trash",
    "node_modules",
    "__pycache__",
}

STRUCTURED_DIRS = {
    "001_Research_studies",
    "002_Evidence",
    "003_User_needs",
    "004_Behaviours",
    "005_Pain_point",
    "006_Insights",
    "007_Themes",
    "008_Personas",
    "009_Journeys",
}

DOC_DIRS = {
    "000_Inbox",
    "docs",
    "migration",
}

TEMPLATE_DIRS = {
    "Templates",
}

TYPE_PREFIX = {
    "research_study": "RS",
    "evidence": "EVID",
    "user_need": "UN",
    "behaviour": "BEH",
    "pain_point": "PP",
    "insight": "INS",
    "theme": "TH",
    "persona": "PER",
    "journey": "JNY",
    "opportunity": "OPP",
    "review_note": "REV",
    "claim": "CLM",
    "value_dimension": "VAL",
}

ID_PATTERN = re.compile(r"^[A-Z]+_\d{3}$")
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")

CONTROLLED_VALUES = {
    "status": {
        "captured",
        "draft",
        "assumption",
        "reviewed",
        "validated",
        "deprecated",
        "idea",
        "assessing",
        "not_recommended",
        "recommended",
        "deferred",
        "implemented",
    },
    "analysis_state": {
        "captured",
        "placeholder",
        "candidate",
        "drafted",
        "evidence_linked",
        "reviewed",
        "validated",
        "deprecated",
    },
    "review_status": {
        "not_reviewed",
        "needs_review",
        "reviewed",
        "rejected",
    },
    "evidence_basis": {
        "none",
        "indicative",
        "traceable",
        "substantiated",
        "validated",
    },
    "evidence_strength": {
        "none",
        "weak",
        "moderate",
        "strong",
    },
    "confidence": {
        "low",
        "medium",
        "high",
    },
    "creation_mode": {
        "manual",
        "llm_assisted",
        "imported",
        "migrated",
    },
    "change_level": {
        "none",
        "minor",
        "material",
        "major",
    },
    "need_level": {
        "capability",
        "civic",
        "experience",
        "service",
        "journey",
        "task",
        "page",
        "interaction",
        "content",
    },
    "evidence_scope_fit": {
        "direct",
        "partial",
        "contextual",
        "weak",
    },
    "wording_sensitivity": {
        "low",
        "medium",
        "high",
    },
}

REQUIRED_COMMON_FIELDS = {
    "type",
    "id",
    "status",
    "analysis_state",
    "creation_mode",
    "llm_generated",
    "human_reviewed",
    "review_status",
    "tags",
}

REQUIRED_BY_TYPE = {
    "research_study": {"title"},
    "evidence": {"source_study", "evidence_kind"},
    "user_need": {"need", "need_level"},
    "behaviour": {"behaviour"},
    "pain_point": {"pain_point"},
    "insight": {"title"},
    "theme": {"title"},
    "persona": {"title"},
    "journey": {"title"},
    "opportunity": {"title", "opportunity"},
    "value_dimension": {"title", "value_statement"},
    "review_note": {"reviewed_item"},
}

STRICT_TYPES = set(TYPE_PREFIX)


@dataclass
class Finding:
    severity: str
    path: Path
    message: str

    def render(self) -> str:
        rel = self.path.relative_to(ROOT)
        return f"[{self.severity.upper()}] {rel}: {self.message}"


@dataclass
class Note:
    path: Path
    frontmatter: Dict[str, object]
    body: str
    has_frontmatter: bool


def iter_markdown_files() -> Iterable[Path]:
    for path in ROOT.rglob("*.md"):
        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue
        yield path


def parse_frontmatter(text: str) -> Tuple[bool, Dict[str, object], str]:
    if not text.startswith("---\n"):
        return False, {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return True, {}, text
    raw = text[4:end].strip("\n")
    body = text[end + 4 :]
    return True, parse_simple_yaml(raw), body


def parse_simple_yaml(raw: str) -> Dict[str, object]:
    """Parse the small YAML subset used in repository frontmatter.

    Supports scalar keys and simple dash lists. This avoids requiring PyYAML.
    """
    data: Dict[str, object] = {}
    current_key: Optional[str] = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - ") and current_key:
            value = strip_quotes(line[4:].strip())
            if not isinstance(data.get(current_key), list):
                data[current_key] = []
            data[current_key].append(value)  # type: ignore[union-attr]
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            current_key = key
            if value == "":
                data[key] = []
            else:
                data[key] = strip_quotes(value)
        else:
            current_key = None
    return data


def strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def load_notes() -> List[Note]:
    notes: List[Note] = []
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        has_frontmatter, frontmatter, body = parse_frontmatter(text)
        notes.append(Note(path=path, frontmatter=frontmatter, body=body, has_frontmatter=has_frontmatter))
    return notes


def top_level_dir(note: Note) -> str:
    rel = note.path.relative_to(ROOT)
    return rel.parts[0] if rel.parts else ""


def is_template(note: Note) -> bool:
    return top_level_dir(note) in TEMPLATE_DIRS


def is_doc_or_scaffold(note: Note) -> bool:
    return top_level_dir(note) in DOC_DIRS


def is_default_scope(note: Note) -> bool:
    return not is_template(note) and not is_doc_or_scaffold(note)


def is_validation_scope(note: Note, include_templates: bool, include_docs: bool) -> bool:
    if is_template(note) and not include_templates:
        return False
    if is_doc_or_scaffold(note) and not include_docs:
        return False
    return True


def is_structured_candidate(note: Note, include_templates: bool = False, include_docs: bool = False) -> bool:
    if not is_validation_scope(note, include_templates=include_templates, include_docs=include_docs):
        return False
    rel = note.path.relative_to(ROOT)
    if rel.parts and rel.parts[0] in STRUCTURED_DIRS:
        return True
    note_type = str(note.frontmatter.get("type", ""))
    return note_type in STRICT_TYPES


def check_frontmatter(note: Note, include_templates: bool, include_docs: bool) -> List[Finding]:
    findings: List[Finding] = []
    if is_structured_candidate(note, include_templates=include_templates, include_docs=include_docs) and not note.has_frontmatter:
        findings.append(Finding("error", note.path, "structured note is missing YAML frontmatter"))
    return findings


def scalar(frontmatter: Dict[str, object], key: str) -> str:
    value = frontmatter.get(key, "")
    if isinstance(value, list):
        return ""
    return str(value).strip()


def check_required_fields(note: Note, include_templates: bool, include_docs: bool) -> List[Finding]:
    findings: List[Finding] = []
    if not is_structured_candidate(note, include_templates=include_templates, include_docs=include_docs) or not note.has_frontmatter:
        return findings
    note_type = scalar(note.frontmatter, "type")
    required = set(REQUIRED_COMMON_FIELDS)
    required.update(REQUIRED_BY_TYPE.get(note_type, set()))
    for field in sorted(required):
        if field not in note.frontmatter:
            findings.append(Finding("error", note.path, f"missing required field `{field}`"))
    return findings


def check_id(note: Note, id_index: Dict[str, List[Path]], include_templates: bool, include_docs: bool) -> List[Finding]:
    findings: List[Finding] = []
    if not is_structured_candidate(note, include_templates=include_templates, include_docs=include_docs) or not note.has_frontmatter:
        return findings
    note_id = scalar(note.frontmatter, "id")
    note_type = scalar(note.frontmatter, "type")
    if not note_id:
        findings.append(Finding("error", note.path, "missing `id` value"))
        return findings
    if not ID_PATTERN.match(note_id):
        findings.append(Finding("error", note.path, f"id `{note_id}` does not match PREFIX_000 format"))
    expected = TYPE_PREFIX.get(note_type)
    prefix = note_id.split("_", 1)[0] if "_" in note_id else ""
    if expected and prefix != expected:
        findings.append(Finding("error", note.path, f"id prefix `{prefix}` does not match type `{note_type}` expected `{expected}`"))
    if note_id in id_index and len(id_index[note_id]) > 1:
        findings.append(Finding("error", note.path, f"duplicate id `{note_id}`"))
    filename_stem = note.path.stem
    if ID_PATTERN.match(note_id) and filename_stem != note_id:
        findings.append(Finding("warning", note.path, f"filename `{filename_stem}` does not match id `{note_id}`"))
    return findings


def check_controlled_values(note: Note, include_templates: bool, include_docs: bool) -> List[Finding]:
    findings: List[Finding] = []
    if not is_structured_candidate(note, include_templates=include_templates, include_docs=include_docs) or not note.has_frontmatter:
        return findings
    for field, allowed in CONTROLLED_VALUES.items():
        if field not in note.frontmatter:
            continue
        value = scalar(note.frontmatter, field)
        if not value:
            continue
        if " | " in value:
            findings.append(Finding("warning", note.path, f"field `{field}` appears to contain template options, not a selected value"))
            continue
        if value not in allowed:
            findings.append(Finding("error", note.path, f"field `{field}` has invalid value `{value}`"))
    return findings


def check_lifecycle_rules(note: Note, include_templates: bool, include_docs: bool) -> List[Finding]:
    findings: List[Finding] = []
    if not is_structured_candidate(note, include_templates=include_templates, include_docs=include_docs) or not note.has_frontmatter:
        return findings
    status = scalar(note.frontmatter, "status")
    analysis_state = scalar(note.frontmatter, "analysis_state")
    review_status = scalar(note.frontmatter, "review_status")
    human_reviewed = scalar(note.frontmatter, "human_reviewed")
    evidence_basis = scalar(note.frontmatter, "evidence_basis")
    evidence_strength = scalar(note.frontmatter, "evidence_strength")

    if status == "validated" and review_status != "reviewed":
        findings.append(Finding("error", note.path, "validated status requires review_status: reviewed"))
    if status == "validated" and human_reviewed != "true":
        findings.append(Finding("error", note.path, "validated status requires human_reviewed: true"))
    if analysis_state == "validated" and evidence_basis in {"", "none", "indicative"}:
        findings.append(Finding("error", note.path, "validated analysis_state requires traceable, substantiated or validated evidence_basis"))
    if evidence_basis == "validated" and human_reviewed != "true":
        findings.append(Finding("error", note.path, "evidence_basis: validated requires human_reviewed: true"))
    if evidence_basis == "validated" and review_status != "reviewed":
        findings.append(Finding("error", note.path, "evidence_basis: validated requires review_status: reviewed"))
    if evidence_strength == "strong" and evidence_basis in {"", "none", "indicative"}:
        findings.append(Finding("warning", note.path, "evidence_strength: strong should usually have traceable, substantiated or validated evidence_basis"))
    return findings


def build_indexes(notes: List[Note], include_templates: bool, include_docs: bool) -> Tuple[Dict[str, List[Path]], Dict[str, Path]]:
    id_index: Dict[str, List[Path]] = {}
    link_targets: Dict[str, Path] = {}
    for note in notes:
        if not is_validation_scope(note, include_templates=include_templates, include_docs=include_docs):
            continue
        note_id = scalar(note.frontmatter, "id")
        if note_id:
            id_index.setdefault(note_id, []).append(note.path)
            link_targets[note_id] = note.path
        link_targets[note.path.stem] = note.path
    return id_index, link_targets


def check_wikilinks(note: Note, link_targets: Dict[str, Path], include_templates: bool, include_docs: bool) -> List[Finding]:
    findings: List[Finding] = []
    if not is_validation_scope(note, include_templates=include_templates, include_docs=include_docs):
        return findings
    text = note.body
    for target in WIKILINK_PATTERN.findall(text):
        clean = target.strip()
        if clean and clean not in link_targets:
            findings.append(Finding("warning", note.path, f"wikilink target `[[{clean}]]` does not resolve to a known filename or id"))
    return findings


def check_relationship_links(note: Note, link_targets: Dict[str, Path], include_templates: bool, include_docs: bool) -> List[Finding]:
    findings: List[Finding] = []
    if not is_structured_candidate(note, include_templates=include_templates, include_docs=include_docs) or not note.has_frontmatter:
        return findings
    for key, value in note.frontmatter.items():
        if not (key.startswith("related_") or key in {"source_study", "source_note", "reviewed_item", "supersedes", "superseded_by", "parent_needs", "child_needs"}):
            continue
        values: List[str]
        if isinstance(value, list):
            values = [str(v) for v in value]
        else:
            values = [str(value)] if str(value).strip() else []
        for raw in values:
            for target in WIKILINK_PATTERN.findall(raw):
                clean = target.strip()
                if clean and clean not in link_targets:
                    findings.append(Finding("warning", note.path, f"field `{key}` links to unresolved target `[[{clean}]]`"))
    return findings


def validate(include_templates: bool = False, include_docs: bool = False) -> List[Finding]:
    notes = load_notes()
    id_index, link_targets = build_indexes(notes, include_templates=include_templates, include_docs=include_docs)
    findings: List[Finding] = []
    for note in notes:
        findings.extend(check_frontmatter(note, include_templates=include_templates, include_docs=include_docs))
        findings.extend(check_required_fields(note, include_templates=include_templates, include_docs=include_docs))
        findings.extend(check_id(note, id_index, include_templates=include_templates, include_docs=include_docs))
        findings.extend(check_controlled_values(note, include_templates=include_templates, include_docs=include_docs))
        findings.extend(check_lifecycle_rules(note, include_templates=include_templates, include_docs=include_docs))
        findings.extend(check_wikilinks(note, link_targets, include_templates=include_templates, include_docs=include_docs))
        findings.extend(check_relationship_links(note, link_targets, include_templates=include_templates, include_docs=include_docs))
    return findings


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Validate research repository metadata and links.")
    parser.add_argument("--warnings-as-errors", action="store_true", help="Treat warnings as errors.")
    parser.add_argument("--include-templates", action="store_true", help="Also validate files in Templates/.")
    parser.add_argument("--include-docs", action="store_true", help="Also validate docs, migration notes and inbox notes.")
    args = parser.parse_args(argv)

    findings = validate(include_templates=args.include_templates, include_docs=args.include_docs)
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    for finding in findings:
        print(finding.render())

    print("\nValidation summary")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors or (args.warnings_as_errors and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
