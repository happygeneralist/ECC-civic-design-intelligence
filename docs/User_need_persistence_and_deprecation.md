# User need persistence and deprecation strategy

User needs are first-class research objects in this repository.

They are not simple labels, tickets or content requirements. They represent an interpretation of evidence about what people need to achieve, avoid, access, understand, decide or sustain. Because of that, their evolution matters.

This document defines how user needs should persist, evolve, be superseded and be deprecated.

## Core principle

User needs should be persistent, traceable and supersedable.

They should not be casually deleted because the team's understanding changes. If a user need is wrong, incomplete, too broad or later solved, the repository should preserve that history so future work can understand what changed and why.

Use these words carefully:

- Persistent: the object remains part of the research record.
- Traceable: the evidence and reasoning behind the object can be followed.
- Supersedable: a better or more mature framing can replace it without erasing the earlier framing.
- Deprecated: the object is no longer recommended for active use, but remains part of the historical record.

Avoid describing user needs as strictly immutable. They can and should evolve. The important rule is that meaningful evolution should not be silent.

## Why persistence matters

Small changes to a user need can imply large changes in possible solutions.

For example:

```text
I need information about available options.
```

is not equivalent to:

```text
I need help identifying which options match my child's needs and aspirations.
```

The first framing may imply content, search or navigation. The second may imply interpretation, brokerage, relational support, confidence-building, planning tools or professional judgement.

When wording changes in this way, the change should be visible.

## Status values and lifecycle use

Recommended user need lifecycle values should distinguish between active, mature and retired knowledge states.

Recommended values:

```yaml
status: captured
status: reviewed
status: validated
status: superseded
status: deprecated
```

Meanings:

- `captured`: recorded as a candidate or working user need
- `reviewed`: reviewed by a human and accepted as useful
- `validated`: strongly supported by evidence and review
- `superseded`: replaced by one or more better-framed needs
- `deprecated`: retained for history but no longer recommended for active use

Deprecation is not deletion.

## Superseding user needs

When a user need is replaced by a better framing, keep the original note and link the relationship.

Example:

```yaml
status: superseded
superseded_by:
  - "[[UN_014]]"
supersedes:
```

The new need can include:

```yaml
supersedes:
  - "[[UN_003]]"
superseded_by:
```

The old need should explain why it was superseded:

```markdown
## Change log

- 2026-06-20: Superseded by UN_014 after evidence showed that the problem was not simply access to information but interpretive support for comparing options.
```

## Deprecating user needs

A user need should be deprecated when it is no longer recommended for active use but remains relevant as historical or contextual knowledge.

Deprecation may happen when:

- a need was based on weak or misleading assumptions
- a need has been solved in the current service context
- a need is no longer active for a specific population or phase
- the framing is no longer appropriate
- the need has been replaced by stronger evidence or a better segmentation

A solved pain point or addressed user need should not necessarily be deleted. It may return if the service, policy, access route or environment changes.

Example:

```yaml
status: deprecated
deprecation_reason: Addressed by revised pathway-planning support model, but retained because the issue may recur if support conditions change.
```

The body should preserve the rationale:

```markdown
## Deprecation note

This user need is not currently active in the revised service model, but it remains historically important. It should be reconsidered if families again report difficulty identifying suitable pathway options.
```

## Merging user needs

When two or more user needs are merged, keep the original notes and mark them as superseded.

Example:

```yaml
status: superseded
superseded_by:
  - "[[UN_021]]"
```

The new need should record:

```yaml
supersedes:
  - "[[UN_007]]"
  - "[[UN_008]]"
```

The change log should explain the reasoning:

```markdown
## Change log

- 2026-06-20: Merged with UN_008 because review showed both needs described the same underlying decision-support need from different evidence fragments.
```

## Splitting user needs

When a need is too broad, split it rather than overwriting it.

Original need:

```yaml
status: superseded
superseded_by:
  - "[[UN_022]]"
  - "[[UN_023]]"
```

Change log:

```markdown
## Change log

- 2026-06-20: Split into UN_022 and UN_023 after evidence showed separate needs around emotional readiness and information overload.
```

## Lightweight user need change log

Every mature or first-class user need should eventually include a lightweight change log.

Recommended format:

```markdown
## Change log

- 2026-06-08: Created from migrated pathway-planning material. Status: captured.
- 2026-06-14: Linked to EVID_001 and BEH_001. Evidence basis remains indicative.
- 2026-06-20: Refined wording to clarify that the need is interpretive decision support, not generic signposting. Change level: material.
```

Do not write a long narrative for every small edit. The change log should capture meaningful stages in the maturity of the object.

## Frontmatter fields for persistence

Recommended fields for user needs:

```yaml
version: 1
status: captured
analysis_state: captured
evidence_basis: indicative
review_status: not_reviewed
last_meaningful_change:
supersedes:
superseded_by:
deprecation_reason:
```

Only use `supersedes`, `superseded_by` and `deprecation_reason` when relevant.

## What not to do

Avoid:

- silently overwriting meaningful user need wording
- deleting superseded or deprecated needs without a strong reason
- upgrading evidence basis because wording sounds plausible
- letting LLM-polished wording replace evidence-derived language without review
- treating solved needs or pain points as if they never existed

## Strategic value

Persistent user needs allow the repository to support deeper analysis:

- which needs have matured over time
- which needs were reframed by evidence
- which needs have been solved but may recur
- which needs are still weak or assumption-led
- which needs underpin product, service or policy decisions

The history of the need is part of the knowledge.