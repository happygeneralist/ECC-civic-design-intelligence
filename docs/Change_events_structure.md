# Change events structure

This document proposes a future structure for recording meaningful knowledge changes and LLM interventions without duplicating Git history.

The repository should not immediately overbuild a full event-sourcing system. The near-term goal is to create a clear place and pattern for change events so future tools can query them when needed.

Change events are optional and experimental until the repository has enough real examples to justify stronger validation.

## Purpose

Change events are structured records of knowledge-level change.

They are useful when a change affects:

- meaning
- evidence basis
- maturity
- lifecycle state
- review state
- interpretation
- relationships between knowledge objects
- LLM intervention and semantic risk
- resolved, dormant or recurring pain points

Git remains the technical source of truth for file diffs. Change events capture why a knowledge object changed and what that change means.

## Recommended folder structure

```text
011_Change_events/
  README.md
  LLM/
  Objects/
  Reviews/
```

Suggested use:

- `LLM/`: LLM-assisted semantic interventions
- `Objects/`: human-authored object evolution events, such as split, merge, supersede, deprecate, resolve or mark dormant
- `Reviews/`: review or validation decisions that affect maturity state

This folder should be optional at first. It should not become mandatory for every edit.

## Event naming pattern

Recommended filename pattern:

```text
YYYY-MM-DD_OBJECT-ID_event-summary.md
```

Examples:

```text
011_Change_events/LLM/2026-06-20_UN_001_need-wording-refinement.md
011_Change_events/Objects/2026-06-22_UN_003_superseded-by-UN_014.md
011_Change_events/Objects/2026-06-23_PP_001_marked-dormant.md
011_Change_events/Reviews/2026-06-23_UN_014_reviewed.md
```

If multiple events occur on the same object on the same day, add a short sequence suffix:

```text
2026-06-20_UN_001_02_evidence-basis-change.md
```

## Common event fields

Each event should include a short metadata block.

Example:

```markdown
# Change event: UN_003 superseded by UN_014

## Metadata

- Date: 2026-06-22
- Object: [[UN_003]]
- Object type: user_need
- Event type: superseded
- Change level: major
- Actor type: human
- Human reviewed: true
- Review status: reviewed

## Summary

UN_003 was superseded by UN_014 after review showed that the earlier need was too broad and mixed information access with interpretive decision support.

## Evidence or rationale

- [[EVID_001]]
- [[INS_002]]

## Resulting object changes

- UN_003 lifecycle state changed to `superseded`.
- UN_003 now links to `superseded_by: [[UN_014]]`.
- UN_014 now links to `supersedes: [[UN_003]]`.
```

## Pain point recurrence event example

```markdown
# Change event: PP_001 marked dormant

## Metadata

- Date: 2026-07-01
- Object: [[PP_001]]
- Object type: pain_point
- Event type: dormant
- Change level: material
- Actor type: human
- Human reviewed: true
- Review status: reviewed

## Summary

PP_001 was marked dormant because the current service model addresses the information-fragmentation issue. The pain point remains historically important because it may recur if ownership, content maintenance or access routes change.

## Resulting object changes

- Lifecycle state changed to `dormant`.
- Resolution state changed to `addressed_currently`.
- Recurrence risk set to `high`.

## Recurrence conditions

- University support information becomes outdated.
- Responsibility for maintaining content changes.
- Families report renewed difficulty comparing support options.
```

## Event types

Recommended event types:

```yaml
event_type: created
event_type: evidence_added
event_type: evidence_removed
event_type: relationship_changed
event_type: wording_refined
event_type: interpretation_changed
event_type: split
event_type: merged
event_type: superseded
event_type: deprecated
event_type: resolved
event_type: dormant
event_type: recurrence_risk_changed
event_type: review_completed
event_type: validation_changed
event_type: llm_intervention
```

## Change levels

Recommended change levels:

```yaml
change_level: administrative
change_level: minor
change_level: material
change_level: major
```

Definitions:

- `administrative`: no intended knowledge or meaning change
- `minor`: wording or presentation refinement without meaning change
- `material`: meaning, relationships, evidence basis, lifecycle state, recurrence risk or interpretation changed
- `major`: split, merge, supersede, deprecate or validation change

## Actor types

Recommended actor types:

```yaml
actor_type: human
actor_type: llm
actor_type: automated_validator
actor_type: migration
```

These help future queries distinguish between human judgement, LLM-assisted synthesis and mechanical migration.

## Relationship to object change logs

Object change logs and change events should not duplicate each other in full.

The object change log should contain a short human-readable summary:

```markdown
## Change log

- 2026-06-22: Superseded by UN_014 after review showed this need mixed information access and interpretive support.
```

The change event can contain the fuller rationale:

```text
011_Change_events/Objects/2026-06-22_UN_003_superseded-by-UN_014.md
```

This keeps the object readable while preserving a deeper audit trail where needed.

## Relationship to PR summaries

Pull request summaries are useful for batches and migrations.

Change events are useful for individual knowledge changes that matter independently of the PR.

For example:

- A PR migrating 20 notes does not need 20 detailed events if no meanings changed.
- A PR that rewrites a single user need because evidence reframed it should create a change event.
- A PR that marks a pain point dormant because an intervention now covers it may create a change event if recurrence risk matters.

## What should not become a change event

Avoid creating change events for:

- spelling changes
- formatting changes
- YAML field ordering
- ID normalisation with no meaning change
- filename changes with no meaning change
- batch migration housekeeping

These belong in Git and PR summaries.

## Query and dashboard opportunities

A future tool could query change events to answer:

- Which user needs have been superseded?
- Which needs have material LLM-assisted changes awaiting review?
- Which objects became more substantiated over time?
- Which pain points are unresolved?
- Which pain points are dormant but high risk?
- Which pain points are blocking value delivery?
- Which service changes addressed particular pain points?
- Which insights changed because new evidence was added?
- Which service decisions rely on stable or validated objects?

This supports dashboards that show coverage, unresolved pain, recurrence risk and value blockers.

## Initial implementation recommendation

Start with the folder and guidance only.

Use change events sparingly for:

1. material LLM-assisted changes
2. user need split, merge, supersede or deprecation
3. pain point resolution, dormancy or recurrence-risk changes
4. validation or review decisions that change maturity
5. significant evidence-basis changes

Do not require change events for every repository edit.