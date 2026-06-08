# Validation baseline report

This report records the repository validation baseline before ID, filename or link migration begins.

No research notes should be changed as part of this baseline report.

## How to generate the baseline

Run from the repository root:

```bash
python3 tools/validate_repository.py
```

Optionally save the output:

```bash
python3 tools/validate_repository.py > migration/validation-baseline-output.txt
```

Do not use `--warnings-as-errors` for the first baseline. The first pass should separate hard errors from warnings and migration signals.

## Baseline status

```text
Baseline run date:
Run by:
Branch or commit:
Validator command:
Errors:
Warnings:
```

## Summary

| Finding group | Count | Severity | Migration action |
|---|---:|---|---|
| Missing required fields | TBD | Error | Fix in metadata batch |
| Invalid ID format | TBD | Error | Fix in ID batch |
| Duplicate IDs | TBD | Error | Human review before migration |
| Wrong ID prefix for type | TBD | Error | Fix in ID batch |
| Invalid controlled values | TBD | Error | Fix in metadata batch |
| Lifecycle contradictions | TBD | Error | Human review before promotion/demotion |
| `evidence_basis: validated` without review | TBD | Error | Human review before correction |
| Unresolved wikilinks | TBD | Warning | Link mapping batch |
| Unresolved relationship links | TBD | Warning | Link mapping batch |
| Filename/ID mismatch | TBD | Warning | Filename migration batch |

## Full validator output

Paste or summarise validator output here.

```text
TBD
```

## Findings by file

| File | Finding | Severity | Proposed class | Proposed action | Notes |
|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD |

## Finding classes

Use these classes when interpreting results.

| Class | Meaning | Typical action |
|---|---|---|
| Structural error | Breaks schema, IDs, controlled values or lifecycle consistency | Fix in early migration batch |
| Link integrity warning | Broken wikilink or relationship reference | Map before fixing |
| Filename/ID warning | File name does not match canonical ID | Include in ID mapping |
| Ambiguous object | Type, source or canonical status unclear | Human review before migration |
| Acceptable immaturity | Candidate or assumption is incomplete but honestly labelled | Leave as-is for now |

## Recommended migration batches

Use the baseline to decide the safest order.

### Batch 1: structural metadata fixes

Use for low-risk missing fields, invalid controlled values, and clear schema issues.

### Batch 2: ID normalisation

Use for invalid IDs, wrong prefixes and duplicate IDs after human review.

### Batch 3: link repair

Use for unresolved wikilinks, `source_study`, `source_note`, `related_*`, `parent_needs`, `child_needs`, `supersedes` and `superseded_by` links.

### Batch 4: filename normalisation

Use when filenames should match canonical IDs and link updates have been mapped.

### Batch 5: ambiguous or high-risk items

Use for items where type, source, evidence basis, review state or canonical status requires judgement.

## Do not mechanically fix

Record findings that should not be fixed without judgement.

| Finding | Why mechanical fixing is risky | Required review |
|---|---|---|
| TBD | TBD | TBD |

## Audit decision

```text
Baseline reviewed by:
Review date:
Decision: proceed to mapping | rerun baseline | fix validator | split audit | pause migration
Notes:
```
