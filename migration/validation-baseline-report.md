# Validation baseline report

This report records the calibrated repository validation baseline before ID, filename or link migration begins.

No research notes were changed as part of this baseline report.

## How the baseline was generated

Run from the repository root:

```bash
python3 tools/validate_repository.py
```

Do not use `--warnings-as-errors` for the baseline. The first pass should separate hard errors from warnings and migration signals.

## Baseline status

```text
Baseline run date: 2026-06-08
Run by: GitHub Actions validation workflow
Branch or commit: after validator calibration in PR #8
Validator command: python3 tools/validate_repository.py
Errors: 168
Warnings: 17
Result: Failed, as expected for migration baseline
```

## Executive summary

The calibrated baseline is now focused on real repository content rather than template placeholders or documentation examples.

The validator output reduced from:

```text
181 errors / 124 warnings
```

to:

```text
168 errors / 17 warnings
```

This confirms that the validator calibration worked. The remaining findings are now mostly real migration issues in content folders:

- `001_Research_studies/`
- `002_Evidence/`
- `003_User_needs/`
- `004_Behaviours/`
- `005_Pain_point/`
- `006_Insights/`
- `007_Themes/`
- `008_Personas/`
- `009_Journeys/`

There are still two root-level documentation wikilink warnings from `SCHEMA.md` and `CONTRIBUTING.md`. These are minor and should not block migration. They can be handled later by excluding root documentation files from default wikilink checks or by updating example links.

## Summary by finding group

| Finding group | Count | Severity | Migration action |
|---|---:|---|---|
| Missing required fields | 127 | Error | Fix in metadata batch |
| Missing YAML frontmatter | 6 | Error | Classify whether each file is structured, summary, working note or artefact |
| Invalid ID format | 10 | Error | Fix in ID batch after mapping |
| Duplicate IDs | 0 | Error | No duplicate IDs reported after validator calibration |
| Wrong ID prefix for type | 12 | Error | Fix in ID batch after mapping |
| Invalid controlled values | 19 | Error | Fix in metadata batch, mostly legacy capitalised/status values |
| Lifecycle contradictions | 0 | Error | No explicit lifecycle contradiction reported in this run |
| `evidence_basis: validated` without review | 0 | Error | No explicit evidence-basis validation overclaim reported in this run |
| Unresolved wikilinks | 12 | Warning | Link mapping batch, mostly real content links plus 2 root-doc examples |
| Unresolved relationship links | 3 | Warning | Link mapping batch, mostly `source_study: [[Study_001]]` |
| Filename/ID mismatch | 7 | Warning | Filename migration batch |
| Template option placeholders | 0 | Warning | Removed from default baseline by validator calibration |

## Main findings

### 1. Research study notes need metadata and ID normalisation

Affected files:

- `001_Research_studies/S001_survey.md`
- `001_Research_studies/S002_parent_interviews.md`
- `001_Research_studies/S003_case_studies.md`
- `001_Research_studies/S004_professionals_interviews.md`
- `001_Research_studies/S005_focus_groups.md`
- `001_Research_studies/S006_in-school_workshops.md`

Common findings:

- missing `analysis_state`
- missing `creation_mode`
- missing `human_reviewed`
- missing `llm_generated`
- missing `review_status`
- legacy IDs such as `S003`, `S004`, `S005`, `S006`
- legacy status value `Completed`
- capitalised confidence values such as `High`
- filenames not matching canonical IDs

Likely migration direction:

- convert `S001`-style IDs to `RS_001`-style IDs
- normalise `status: Completed` to an allowed repository value, probably `reviewed` or `captured` depending on content review
- normalise `confidence: High` to `confidence: high`
- add lifecycle fields conservatively
- update filenames only after link mapping is reviewed

### 2. Evidence notes need metadata, evidence-kind and source-link cleanup

Affected files:

- `002_Evidence/Quote_001.md`
- `002_Evidence/Quote_002.md`
- `002_Evidence/Quote_003.md`
- `002_Evidence/EVID_DATA_001.md`

Common findings:

- missing lifecycle fields
- missing `evidence_kind`
- wrong or invalid IDs such as `EVD_002` and `EVIDQ001`
- filenames not matching canonical IDs
- unresolved `source_study: [[Study_001]]`
- capitalised confidence value `Low`

Likely migration direction:

- normalise evidence IDs to `EVID_001`, `EVID_002`, etc.
- resolve `[[Study_001]]` to the correct research study, probably after confirming whether it maps to `RS_001`
- add `evidence_kind` based on content, not mechanically if unclear
- add lifecycle fields conservatively

### 3. User need notes need lifecycle, hierarchy and ID cleanup

Affected files:

- `003_User_needs/UN_001.md`
- `003_User_needs/UN_002.md`
- `003_User_needs/UN_003.md`
- `003_User_needs/UN_004.md`
- `003_User_needs/Anchor summaries.md`
- `003_User_needs/Pathway Planning User need summary.md`

Common findings:

- missing lifecycle fields
- missing `need_level`
- legacy IDs such as `UN002`, `UN003`, `UN004`
- capitalised status values such as `Validated` and `Assumption`
- summary/anchor files are being treated as structured notes because they are in `003_User_needs/`

Likely migration direction:

- normalise IDs to `UN_001`, `UN_002`, etc.
- add lifecycle fields conservatively
- do not mechanically preserve `status: Validated`; reviewed/validated states need human review and evidence basis
- classify summary/anchor files as loose summaries, indexes or structured objects before adding canonical metadata
- add `need_level` only where the level can be reasonably inferred, otherwise mark for review

### 4. Behaviour notes need low-risk metadata cleanup

Affected files:

- `004_Behaviours/BEH_001.md`
- `004_Behaviours/BEH_002.md`

Common findings:

- missing lifecycle/status fields
- capitalised confidence values such as `Low`

Likely migration direction:

- add lifecycle fields conservatively
- normalise `confidence: Low` to `confidence: low`
- keep status conservative until evidence and review state are clear

### 5. Pain point, insight, theme, persona and journey notes need classification before migration

Affected files:

- `005_Pain_point/Pain_point_template 1.md`
- `006_Insights/INS001.md`
- `006_Insights/INS002.md`
- `006_Insights/Insight001.md`
- `006_Insights/Regulation management.md`
- `007_Themes/Theme_template 1.md`
- `008_Personas/Persona.md`
- `009_Journeys/Pathway_planning.md`

Common findings:

- missing lifecycle fields
- missing YAML frontmatter for some files in structured folders
- legacy IDs such as `INS001`, `INS002`, `THEME_001`
- invalid status and confidence values
- unresolved links to evidence, user needs and insights
- some files look like copied templates or draft artefacts rather than canonical notes

Likely migration direction:

- classify each file before changing it
- add frontmatter only where the file is intended to be a structured object
- convert copied templates in numbered folders into real notes, move them to `Templates/`, or deprecate them
- normalise IDs only after confirming object type and canonical status

## Findings by file group

| File group | Main findings | Proposed class | Proposed action | Notes |
|---|---|---|---|---|
| `001_Research_studies/` | Missing lifecycle fields, legacy IDs, capitalised values, filename mismatch | Structural error / filename warning | Metadata and ID migration | Best candidate for first migration batch |
| `002_Evidence/` | Missing lifecycle fields, missing `evidence_kind`, ID issues, unresolved `Study_001` source links | Structural error / link integrity warning | Evidence metadata and source-link migration | Requires care because evidence source links matter |
| `003_User_needs/` | Missing lifecycle fields, missing `need_level`, legacy IDs, capitalised status, summary files lacking frontmatter | Structural error / ambiguous object | User-need metadata migration and summary classification | Do not mechanically validate old `Validated` status |
| `004_Behaviours/` | Missing lifecycle/status fields, capitalised confidence | Structural error | Metadata migration | Likely low-risk if content is straightforward |
| `005_Pain_point/` | Copied template-like file in content folder | Ambiguous object | Classify before migration | May be a real note or accidental template copy |
| `006_Insights/` | Missing frontmatter, legacy IDs, missing title, capitalised values | Structural error / ambiguous object | Insight metadata and ID migration | Some files need classification before canonical ID assignment |
| `007_Themes/` | Legacy `THEME_001`, template-like file, unresolved related links | Structural error / link integrity warning / ambiguous object | Classify then migrate | Avoid blind rename before checking content |
| `008_Personas/` | Missing frontmatter | Ambiguous object | Human review before migration | Important because persona/archetype risk is higher in SEND |
| `009_Journeys/` | Missing frontmatter | Ambiguous object | Human review before migration | Decide whether journey is canonical or working artefact |
| Root docs | `SCHEMA.md` and `CONTRIBUTING.md` example wikilinks | Validator calibration / low-risk docs warning | Defer | Not migration-critical |

## Selected validator output examples

```text
Validation summary
Errors: 168
Warnings: 17
```

Representative errors:

```text
Error: 001_Research_studies/S003_case_studies.md: id `S003` does not match PREFIX_000 format
Error: 002_Evidence/Quote_002.md: id prefix `EVD` does not match type `evidence` expected `EVID`
Error: 003_User_needs/UN_002.md: id `UN002` does not match PREFIX_000 format
Error: 006_Insights/Insight001.md: structured note is missing YAML frontmatter
Error: 007_Themes/Theme_template 1.md: field `status` has invalid value `Active`
```

Representative warnings:

```text
Warning: 002_Evidence/Quote_001.md: field `source_study` links to unresolved target `[[Study_001]]`
Warning: 007_Themes/Theme_template 1.md: wikilink target `[[UN_001 Support emotional regulation in daily routines]]` does not resolve to a known filename or id
Warning: SCHEMA.md: wikilink target `[[UN_024]]` does not resolve to a known filename or id
```

## Do not mechanically fix

| Finding | Why mechanical fixing is risky | Required review |
|---|---|---|
| `status: Validated` on `003_User_needs/UN_001.md` | Legacy validation may not map safely to the new reviewed/validated model | Check evidence basis, review state and wording before preserving validation |
| Missing `need_level` on user needs | Need level affects hierarchy and solution vector | Review wording and scope before assigning level |
| Missing frontmatter on summaries, personas and journeys | Some files may be summaries, working notes or canonical objects | Classify object type before adding IDs |
| `source_study: [[Study_001]]` | Source links affect evidence traceability | Confirm correct study mapping before updating links |
| Persona and journey files | SEND representational risk is higher | Human review before canonicalising |
| Copied template-like files in content folders | They may be accidental scaffolds rather than real research objects | Classify before migration |

## Recommended migration batches

### Batch 1: research study metadata and ID normalisation

Start here because the study notes are coherent as a group and are likely to unblock evidence source-link cleanup.

Suggested scope:

- `001_Research_studies/S001_survey.md`
- `001_Research_studies/S002_parent_interviews.md`
- `001_Research_studies/S003_case_studies.md`
- `001_Research_studies/S004_professionals_interviews.md`
- `001_Research_studies/S005_focus_groups.md`
- `001_Research_studies/S006_in-school_workshops.md`

### Batch 2: evidence metadata and source-link normalisation

Do after research-study IDs and filenames are stable.

### Batch 3: behaviour metadata cleanup

Likely low-risk, but should follow the study/evidence migration if behaviours link to evidence.

### Batch 4: user need metadata, ID and hierarchy review

Do not rush this batch because `need_level`, wording and legacy `Validated` status need judgement.

### Batch 5: insight, theme, persona and journey classification

Handle copied templates, summary files and representational artefacts separately.

## Audit decision

```text
Baseline reviewed by:
Review date:
Decision: proceed to Batch 1 mapping and migration
Notes: Recommended decision is to start with research study metadata and ID normalisation. Do not begin with user needs, personas or journeys because they require more judgement.
```
