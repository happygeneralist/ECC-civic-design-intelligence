# Repository validation

This file explains how to use lightweight tests to keep the research repository consistent as notes are migrated, normalised or added.

## Purpose

Validation gives contributors a test-driven way to clean up the repository.

Instead of manually guessing whether the repo is consistent, run the validator and make changes until the checks pass.

The default validation layer focuses on real repository content notes, not templates, documentation examples or migration scaffolds.

It checks:

- YAML frontmatter presence
- required fields on structured notes
- canonical ID format
- ID prefix matching object type
- duplicate IDs
- controlled values
- lifecycle safety rules
- unresolved wikilinks
- unresolved relationship links

## Validation philosophy

The validator does not exist to make every research object complete before it can be committed.

The repository is allowed to contain incomplete knowledge, weak signals, placeholders and LLM-assisted candidate objects.

The validator exists to stop incomplete knowledge being mistaken for reviewed or validated knowledge.

In short:

```text
Allow incomplete objects.
Block misleading objects.
```

A candidate user need can exist without direct evidence links if it is clearly marked as a candidate or assumption.

A user need must not be treated as reviewed, validated or decision-ready unless the required traceability, review state and evidence basis are present.

The validator should therefore protect against category errors such as:

- draft treated as validated
- assumption treated as evidence
- LLM output treated as research
- weak traceability treated as strong evidence basis
- review state hidden or misrepresented
- wrong ID or type making an object hard to trace

## Default validation scope

By default, the validator checks research and problem-space content folders, including:

- `001_Research_studies/`
- `002_Evidence/`
- `003_User_needs/`
- `004_Behaviours/`
- `005_Pain_point/`
- `006_Insights/`
- `007_Themes/`
- `008_Personas/`
- `009_Journeys/`

By default, it skips:

- `Templates/`
- `000_Inbox/`
- `docs/`
- `migration/`

This avoids treating template placeholders, documentation examples and audit scaffolds as real research notes.

## Optional validation scopes

To include templates:

```bash
python3 tools/validate_repository.py --include-templates
```

To include documentation, migration notes and inbox notes:

```bash
python3 tools/validate_repository.py --include-docs
```

To include both:

```bash
python3 tools/validate_repository.py --include-templates --include-docs
```

These flags are useful for separate quality checks, but they should not be used for the normal research-note migration baseline unless that is intentional.

## Three validation layers

### 1. Structural checks

These are suitable for automated validation.

Examples:

- duplicate IDs
- invalid ID format
- missing required fields
- invalid controlled values
- ID prefix does not match object type
- unresolved internal links

### 2. Governance checks

These are partly automatable.

Examples:

- `status: validated` requires `human_reviewed: true`
- `evidence_basis: validated` requires `review_status: reviewed`
- validated objects need a defensible evidence basis
- LLM-generated objects should not appear human-reviewed unless a review has been explicitly completed

### 3. Decision-readiness checks

These are not fully automated in the first version.

Decision-readiness means an object is being used for a higher-consequence purpose, such as:

- page or content design
- service design
- policy challenge
- prioritisation
- stakeholder synthesis
- value assessment
- ministerial or senior decision support
- validation

The validator can check whether minimum conditions are present, but it cannot judge whether the research interpretation is substantively correct.

The long-term pattern should be:

```text
machine checks presence and consistency
human checks meaning and judgement
```

A future validator mode may check notes marked with fields such as:

```yaml
intended_use:
  - policy_challenge
  - service_design
```

or:

```yaml
decision_use: true
```

and require stricter metadata such as:

- reviewed or validated status
- traceable or substantiated evidence basis
- human review
- linked evidence
- need level
- parent needs where relevant
- caveats or uncertainty
- review notes for higher-risk claims

Do not apply decision-readiness checks to every loose or candidate object.

## Running the validator

From the repository root, run:

```bash
python3 tools/validate_repository.py
```

To treat warnings as errors:

```bash
python3 tools/validate_repository.py --warnings-as-errors
```

## How to use during migration

Use this sequence:

```text
run validator -> review failures -> update notes -> rerun validator -> repeat until clean enough
```

This is especially useful for:

- ID normalisation
- source-link migration
- template migration
- adding new structured notes
- checking LLM-generated candidate objects

## Error versus warning

### Errors

Errors indicate something that should normally be fixed before merging migration work.

Examples:

- missing required field
- invalid ID format
- duplicate ID
- ID prefix does not match type
- invalid controlled value
- validated item without human review
- `evidence_basis: validated` without review

### Warnings

Warnings identify problems that may be acceptable temporarily during migration.

Examples:

- filename does not match ID
- unresolved wikilink
- relationship link target does not resolve
- `evidence_strength: strong` with weak evidence basis

Warnings can be promoted to errors later by using `--warnings-as-errors`.

## What should not be blocked by default

Do not block ordinary commits merely because:

- a candidate user need has no direct evidence link yet
- a placeholder object has no parent need yet
- an LLM-assisted object is not reviewed yet
- an insight is still a draft
- a value dimension is indicative rather than substantiated

These are acceptable if the metadata makes the incompleteness visible.

Block or fail only when the metadata overclaims reliability, review state or traceability.

## Incremental adoption

The validator is intentionally lightweight and should support incremental cleanup.

The repository does not need to be perfect before the validator is useful.

A good migration workflow is:

1. Run the validator.
2. Fix high-confidence errors first.
3. Leave ambiguous items for later audit.
4. Commit fixes in focused batches.
5. Tighten warnings only when the repository is ready.

## What the validator does not do yet

The first version does not fully check:

- semantic quality of user needs
- whether evidence genuinely supports a claim
- whether an insight is well interpreted
- whether personal data has been fully anonymised
- whether a note should be split or merged
- whether a relationship is conceptually correct
- whether an object is substantively decision-ready

These still need human review.

## Recommended migration order

Use the tests to clean up in this order:

1. Duplicate or missing IDs.
2. Invalid ID prefixes.
3. Missing required frontmatter fields.
4. Invalid controlled values.
5. Validated/review lifecycle contradictions.
6. Broken source and relationship links.
7. Filename and ID mismatches.
8. Warnings that remain after migration.

## Practical rule

The validator should support judgement, not replace it.

If a test failure reveals an ambiguous research or evidence issue, document the ambiguity rather than forcing a mechanical fix.
