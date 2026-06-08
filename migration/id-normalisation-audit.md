# ID and link normalisation audit

This file will be used to audit existing IDs, filenames and links before any migration is attempted.

No research notes should be renamed or edited until this audit has been reviewed.

## Audit purpose

The audit now has two linked parts:

1. **Validation baseline** — run the repository validator and classify current structural, lifecycle and link findings.
2. **ID and link mapping** — use the validation findings to create a safe migration map for IDs, filenames, wikilinks and relationship fields.

The audit should produce a clear migration plan before any research notes are changed.

## Audit scope

The audit should cover:

- research studies
- evidence notes
- user needs
- behaviours
- pain points
- insights
- themes
- personas
- journeys
- opportunities
- value dimensions
- review notes
- relationship fields
- wikilinks
- validation findings

## Step 1: validation baseline

Run the repository validator from current `main` or from the audit branch after it is updated with `main`.

```bash
python3 tools/validate_repository.py
```

Record the result in:

```text
migration/validation-baseline-report.md
```

The baseline report should include:

- total errors
- total warnings
- affected files
- grouped finding types
- likely migration batches
- findings that should not be mechanically fixed
- findings requiring human judgement

## Step 2: classify validation findings

Classify findings before changing files.

| Class | Meaning | Typical action |
|---|---|---|
| Structural error | Breaks schema, IDs, controlled values or lifecycle consistency | Fix in early migration batch |
| Link integrity warning | Broken wikilink or relationship reference | Map before fixing |
| Filename/ID warning | File name does not match canonical ID | Include in ID mapping |
| Ambiguous object | Type, source or canonical status unclear | Human review before migration |
| Acceptable immaturity | Candidate or assumption is incomplete but honestly labelled | Leave as-is for now |

## Known issues to check

These are known or suspected from earlier repository inspection.

| Area | Issue | Risk | Action |
|---|---|---:|---|
| Research studies | Some study files may use filenames like `S001_survey.md` while IDs use `RS_001` | Medium | Confirm whether filename should change or alias is enough |
| Evidence | Some evidence notes may use names like `Quote_001` rather than `EVID_001` | Medium | Map evidence notes to canonical `EVID_` IDs |
| Source links | Some evidence may point to `[[Study_001]]` while the canonical study ID is `RS_001` | High | Resolve source references carefully before migration |
| User needs | Some notes already use `UN_001` format | Low | Check consistency and related evidence links |
| Anchor summaries | Some files may be LLM-generated summaries rather than canonical objects | Medium | Do not assign canonical IDs unless they become structured objects |
| Obsidian links | Wikilinks may use filenames rather than IDs | Medium | Update links only after mapping is reviewed |
| Validation findings | Some files may fail schema or lifecycle checks after validation is run | TBD | Classify before changing files |

## Audit table

Use this table for manual or automated audit results.

| Current path | Current filename | Type | Current ID | Expected prefix | Proposed ID | Proposed path | Source study | Related links | Wikilinks | Validator findings | Risk | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `001_Research_studies/S001_survey.md` | `S001_survey.md` | `research_study` | `RS_001` | `RS_` | TBD | TBD | n/a | TBD | TBD | TBD | Medium | Check filename and inbound links before renaming |
| `002_Evidence/Quote_001.md` | `Quote_001.md` | `evidence` | TBD | `EVID_` | TBD | TBD | TBD | TBD | TBD | TBD | Medium | Confirm current frontmatter ID and references |
| `003_User_needs/UN_001.md` | `UN_001.md` | `user_need` | `UN_001` | `UN_` | `UN_001` | likely unchanged | TBD | TBD | TBD | TBD | Low | Check related evidence links |

## Proposed mapping table

Use this table after the audit has been completed.

| Old path | New path | Old ID | New ID | Object type | Old aliases | Links to update | Validator findings | Risk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Review questions

Before migration, answer:

- Has the validation baseline been run and recorded?
- Are validation findings grouped by type and severity?
- Are all structured entity notes identified?
- Are any notes duplicates?
- Are any notes working notes rather than canonical objects?
- Do any notes need aliases during transition?
- Are any source references ambiguous?
- Are any reviewed or validated notes affected?
- Are any findings acceptable immaturity rather than true errors?
- Can the migration be split into low-risk and high-risk batches?

## Migration decision

Do not proceed to migration until this section is completed.

```text
Audit reviewed by:
Review date:
Decision: proceed | revise audit | split migration | do not proceed
Notes:
```
