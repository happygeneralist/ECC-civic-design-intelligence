# Validation baseline report

This report records the repository validation baseline before ID, filename or link migration begins.

No research notes should be changed as part of this baseline report.

## How to generate the baseline

Run from the repository root:

```bash
python3 tools/validate_repository.py
```

Do not use `--warnings-as-errors` for the first baseline. The first pass should separate hard errors from warnings and migration signals.

## Baseline status

```text
Baseline run date: 2026-06-08
Run by: GitHub Actions validation workflow
Branch or commit: audit/validation-baseline
Validator command: python3 tools/validate_repository.py
Errors: 181
Warnings: 124
Result: Failed, as expected for first baseline
```

## Executive summary

The first validation baseline is useful, but it shows two different things:

1. **Real repository migration work is needed** for existing research notes, especially older study, evidence, user need, behaviour, insight, theme and journey notes that predate the new schema.
2. **The validator needs calibration** before it is used as a strict migration gate, because it currently reports many findings from `Templates/`, `docs/` and `migration/` files that should not be treated the same way as structured research notes.

The baseline should therefore not be used to start blind mechanical fixes.

Recommended next step: create a small validator-calibration PR before migrating research notes.

## Summary by finding group

| Finding group | Count | Severity | Migration action |
|---|---:|---|---|
| Missing required fields | 127 | Error | Fix in metadata batch after validator calibration |
| Missing YAML frontmatter | 6 | Error | Decide whether each file is a structured note, summary, dashboard or loose note |
| Invalid ID format | 10 | Error | Fix in ID batch after mapping |
| Duplicate IDs | 2 | Error | Recheck after excluding templates from validation |
| Wrong ID prefix for type | 12 | Error | Fix in ID batch after mapping |
| Invalid controlled values | 24 | Error | Fix in metadata batch, mostly legacy capitalised/status values |
| Lifecycle contradictions | 0 | Error | No explicit lifecycle contradiction reported in this run |
| `evidence_basis: validated` without review | 0 | Error | No explicit evidence-basis validation overclaim reported in this run |
| Unresolved wikilinks | 17 | Warning | Separate real broken links from example links in docs/schema |
| Unresolved relationship links | 3 | Warning | Link mapping batch, mostly `source_study: [[Study_001]]` |
| Filename/ID mismatch | 20 | Warning | Filename migration batch, but exclude templates first |
| Template option placeholders | 84 | Warning | Validator calibration; template option values should not be treated as real-note values |

## Main findings

### 1. Validator calibration is needed before migration

The validator currently reports warnings and errors for files that are not ordinary research notes, especially:

- `Templates/*_template.md`
- `docs/*`
- `migration/*`

This creates noise, including:

- template IDs such as `UN_000`, `EVID_000`, `TH_000` being treated as real IDs
- template option values such as `draft | reviewed | validated` being treated as invalid selected values
- example wikilinks in documentation being treated as broken links
- `Templates/Study_template.md` contributing to a duplicate `RS_001` finding

This should be fixed before using the validator as a strict migration gate.

Recommended validator changes:

- skip `Templates/` for ID, controlled-value, required-field and filename checks
- skip `docs/` and `migration/` for wikilink resolution, or allow documentation example links
- consider a `--include-docs` mode later if documentation link checking is useful
- consider reporting template issues separately from repository content issues

### 2. Research study notes need metadata and ID normalisation

Affected files include:

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

### 3. Evidence notes need metadata, evidence-kind and source-link cleanup

Affected files include:

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

### 4. User need notes need lifecycle, hierarchy and ID cleanup

Affected files include:

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
- some summary/anchor files are treated as structured notes but may not be canonical user need objects

Likely migration direction:

- normalise IDs to `UN_001`, `UN_002`, etc.
- add lifecycle fields conservatively
- do not mechanically preserve `status: Validated`; reviewed/validated states need human review and evidence basis
- classify summary/anchor files as loose summaries, indexes or structured objects before adding canonical metadata
- add `need_level` only where the level can be reasonably inferred, otherwise mark for review

### 5. Behaviour, pain point, insight, theme, persona and journey notes need mixed treatment

Affected files include:

- `004_Behaviours/BEH_001.md`
- `004_Behaviours/BEH_002.md`
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
- missing YAML frontmatter for some structured-folder files
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
| `001_Research_studies/` | Missing lifecycle fields, legacy IDs, capitalised values, filename mismatch | Structural error / filename warning | Metadata and ID migration | Good candidate for early migration batch after validator calibration |
| `002_Evidence/` | Missing lifecycle fields, missing `evidence_kind`, ID issues, unresolved `Study_001` source links | Structural error / link integrity warning | Evidence metadata and source-link migration | Requires care because evidence source links matter |
| `003_User_needs/` | Missing lifecycle fields, missing `need_level`, legacy IDs, capitalised status, summary files lacking frontmatter | Structural error / ambiguous object | User-need metadata migration and summary classification | Do not mechanically validate old `Validated` status |
| `004_Behaviours/` | Missing lifecycle/status fields, capitalised confidence | Structural error | Metadata migration | Likely low-risk if content is straightforward |
| `005_Pain_point/` | Copied template-like file in content folder | Ambiguous object | Classify before migration | May be a real note or accidental template copy |
| `006_Insights/` | Missing frontmatter, legacy IDs, missing title, capitalised values | Structural error / ambiguous object | Insight metadata and ID migration | Some files need classification before canonical ID assignment |
| `007_Themes/` | Legacy `THEME_001`, template-like file, unresolved related links | Structural error / link integrity warning / ambiguous object | Classify then migrate | Avoid blind rename before checking content |
| `008_Personas/` | Missing frontmatter | Ambiguous object | Human review before migration | Important because persona/archetype risk is higher in SEND |
| `009_Journeys/` | Missing frontmatter | Ambiguous object | Human review before migration | Decide whether journey is canonical or working artefact |
| `Templates/` | Many template placeholder warnings and some legacy template errors | Validator calibration | Exclude or separately validate templates | Do not treat as research-note migration work |
| `docs/` and `migration/` | Example wikilinks reported as unresolved | Validator calibration | Exclude or allow example links | Do not fix examples as repository data |

## Selected validator output examples

```text
Validation summary
Errors: 181
Warnings: 124
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
Warning: Templates/User_need_template.md: field `need_level` appears to contain template options, not a selected value
```

## Do not mechanically fix

| Finding | Why mechanical fixing is risky | Required review |
|---|---|---|
| `status: Validated` on `003_User_needs/UN_001.md` | Legacy validation may not map safely to the new reviewed/validated model | Check evidence basis, review state and wording before preserving validation |
| Missing `need_level` on user needs | Need level affects hierarchy and solution vector | Review wording and scope before assigning level |
| Missing frontmatter on summaries, personas and journeys | Some files may be summaries, working notes or canonical objects | Classify object type before adding IDs |
| `source_study: [[Study_001]]` | Source links affect evidence traceability | Confirm correct study mapping before updating links |
| Persona and journey files | SEND representational risk is higher | Human review before canonicalising |
| Template warnings | These are likely validator false positives | Calibrate validator before migration |
| Documentation example links | These are not necessarily broken research links | Decide whether docs/example links should be validated at all |

## Recommended next steps

### Step 0: calibrate the validator

Before migrating research notes, update the validator so template and documentation examples do not dominate the baseline.

Suggested changes:

- exclude `Templates/` from real-note validation checks
- exclude `docs/` and `migration/` from wikilink resolution checks by default
- optionally add a separate template-validation mode later
- rerun the baseline after calibration

### Step 1: rerun validation baseline

After calibration, rerun:

```bash
python3 tools/validate_repository.py
```

Then update this report with the cleaner baseline.

### Step 2: migrate low-risk structural metadata

Prioritise files where the fix is clear and does not change research meaning.

Examples:

- add missing lifecycle fields conservatively
- lowercase controlled values where meaning is unchanged
- add `creation_mode: migrated`
- set `llm_generated: false` where the note predates LLM workflow or where provenance is manual/imported
- set `human_reviewed: false` unless review has actually happened

### Step 3: create an ID/source mapping

Only after the cleaner baseline, map:

- `S003` -> `RS_003`
- `UN002` -> `UN_002`
- `INS001` -> `INS_001`
- `THEME_001` -> `TH_001`
- `EVD_002` -> `EVID_002`
- `EVIDQ001` -> correct `EVID_` ID after checking content

### Step 4: handle ambiguous/high-risk files separately

Do not combine ambiguous persona, journey, summary, template-copy or evidence-source decisions with simple metadata fixes.

## Audit decision

```text
Baseline reviewed by:
Review date:
Decision: fix validator first | rerun baseline | proceed to mapping | split audit | pause migration
Notes: Recommended decision is `fix validator first`, then rerun the validation baseline before research-note migration.
```
