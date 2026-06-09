# Knowledge evolution strategy

This repository is not only a place to store research outputs. It is a place to preserve how research understanding matures over time.

Git provides the technical history of file changes. It shows what changed in the repository, when, and in which commit. That is necessary, but it is not sufficient for research governance. The repository also needs a lightweight way to explain how important knowledge objects changed as evidence was added, interpreted, challenged, refined, split, merged, superseded or deprecated.

This document defines the strategic approach for preserving that knowledge history without duplicating Git.

## Core principle

Structured research objects should be persistent, traceable and supersedable.

They should not be treated as disposable notes that can be silently overwritten whenever the wording changes. This is especially important for first-class objects such as user needs, pain points, behaviours and insights, where small wording changes can imply materially different product, service or policy responses.

A previous framing may later prove incomplete, too broad, too narrow or misdirected. That does not make it useless. It becomes part of the history of how the team understood the problem space.

## Minimum viable practice

Default to lightweight. Escalate only when meaning, evidence basis, maturity, lifecycle or governance changes.

Use this decision rule:

```text
If the change affects how the object should be interpreted, used, trusted or acted on, record it.

If the change only affects how the object is stored, formatted or validated, do not create a semantic change record unless it affects meaning.
```

For now:

1. Add lightweight change logs only to first-class objects when meaning changes, starting with user needs.
2. Use PR summaries for administrative migration batches.
3. Do not create change-event files for routine metadata cleanup.
4. Create LLM intervention logs only for material or risky semantic changes.
5. Keep solved, dormant or deprecated objects visible when they may matter for future service, product or policy reasoning.
6. Do not add strict validator rules until there are real examples and a stable workflow.

## Three layers of history

The repository should distinguish between three different kinds of history.

### 1. Git history

Git is the technical audit trail.

It records:

- exact file diffs
- commits
- branches
- pull requests
- dates
- authors

Git should remain the source of truth for file-level version control. The repository should not try to recreate Git inside Markdown files.

### 2. Object change logs

Object change logs describe the knowledge-level evolution of a structured object.

They answer questions such as:

- Why did this user need change?
- What evidence changed the interpretation?
- Was the object split, merged, superseded or deprecated?
- Did the evidence basis become stronger or weaker?
- Did a change affect the implied intervention space?

These change logs should be human-readable and lightweight. They should not contain every edit.

### 3. LLM intervention logs

LLM intervention logs describe when and how an LLM changed or attempted to change meaning.

They answer questions such as:

- Did an LLM rewrite evidence-derived language?
- Did it change the framing of a user need?
- Did it generalise or narrow the interpretation?
- Did it change confidence, evidence basis or review status?
- Does the change need human review?

These logs are not a replacement for Git. They are a semantic and governance record.

## Separate state, maturity and review

Avoid forcing one field to do too many jobs.

In future schema work, distinguish between:

```yaml
lifecycle_state: active | superseded | deprecated | resolved | dormant
maturity_state: captured | reviewed | validated
review_status: not_reviewed | needs_review | reviewed | rejected
evidence_basis: none | indicative | traceable | substantiated | validated
```

This matters because an object can be both mature and no longer active. For example, a user need may once have been validated but later become superseded by a better-framed need.

If the repository keeps a single `status` field for now, treat it as a pragmatic current-state field and recognise that it may need to split later.

## What should be logged in object change logs

Object change logs should record meaningful evolution, not mechanical edits.

Record changes such as:

- new evidence added
- evidence removed or challenged
- user need wording materially refined
- actor, need level or journey stage changed
- relationships to evidence, behaviours, pain points or insights changed
- evidence basis changed
- review status changed
- object split, merged, superseded or deprecated
- pain point marked resolved, dormant or recurring
- meaning changed because new research reframed the problem

Do not normally record detailed entries for:

- YAML formatting
- ID format normalisation
- filename cleanup
- spelling or punctuation changes
- moving loose notes to the inbox
- adding required lifecycle metadata without changing meaning

Those can be covered by Git history, PR summaries or a single administrative change entry.

## Lightweight change log format

Structured first-class objects should eventually include a short `## Change log` section.

Recommended format:

```markdown
## Change log

- 2026-06-08: Migrated to structured metadata. No substantive change to statement or interpretation.
- 2026-06-14: Linked to additional parent interview evidence and behaviour BEH_001.
- 2026-06-20: Refined wording after evidence showed the need was interpretive decision support, not generic information access.
```

The log should tell the story of the object's maturity. It should not become a detailed file-diff history.

## Change levels

Use change levels to distinguish administrative updates from meaningful knowledge changes.

Recommended levels:

```yaml
change_level: administrative
change_level: minor
change_level: material
change_level: major
```

Definitions:

- `administrative`: schema, metadata, ID, folder or formatting change with no intended meaning change
- `minor`: wording or clarity change that preserves the same meaning
- `material`: change to meaning, relationships, evidence basis, actor, level or interpretation
- `major`: split, merge, supersede, deprecate, validation change or major reframing

## Change types

Recommended change types:

```yaml
change_type:
  - created
  - metadata_normalised
  - evidence_added
  - evidence_removed
  - relationship_changed
  - wording_refined
  - interpretation_changed
  - split
  - merged
  - superseded
  - deprecated
  - resolved
  - dormant
  - recurrence_risk_changed
  - review_status_changed
  - validation_status_changed
```

A future validator or tool can use these values to support consistent querying.

## Relationship to dashboards and service intelligence

The purpose of knowledge evolution is not documentation for its own sake. It should support product, service and civic decision-making.

A future dashboard or query layer should be able to show:

- where user needs are well evidenced
- where user needs remain weak or unreviewed
- where pain points are unresolved
- where pain points are resolved but have high recurrence risk
- where pain blocks value delivery
- where service changes have addressed a need or pain point
- where validated needs are not yet covered by interventions
- where LLM-assisted interpretations are still awaiting review

This is why solved or dormant pain points should not simply be deleted. They can become useful signals for coverage, regression risk and future monitoring.

## Relationship to status and evidence basis

Object status and evidence basis are current-state fields. They should describe the latest accepted state of the object.

The change log explains how that state was reached.

For example:

```yaml
status: captured
evidence_basis: traceable
review_status: needs_review
last_meaningful_change: 2026-06-20
```

The body can then explain:

```markdown
## Change log

- 2026-06-20: Evidence basis changed from indicative to traceable after interview quote EVID_004 was linked. Review still pending.
```

## Recommended near-term implementation

Do not overbuild a full event-sourcing system immediately.

Start with:

1. Add lightweight `## Change log` guidance to first-class templates, starting with user needs.
2. Create a separate LLM intervention logging pattern for material LLM-assisted changes.
3. Add a change-events folder as an optional and experimental structure for future use.
4. Keep Git as the technical source of truth.
5. Use PR summaries for migration/admin batches.
6. Delay strict validation until there are examples and the workflow is understood.

## Strategic intent

The goal is not bureaucratic traceability. The goal is to preserve the reasoning behind research maturity and make the current state of value delivery easier to understand.

This enables future users of the repository to ask:

- Which needs became stronger over time?
- Which needs were superseded by better evidence?
- Which assumptions have not yet been reviewed?
- Which pain points are unresolved or recurring?
- Which pain points are resolved but at risk of returning?
- Which interpretations were LLM-assisted and still need human review?
- Which service decisions were based on mature, traceable needs?
- Where is value blocked by unresolved pain?

The repository should make those questions answerable.