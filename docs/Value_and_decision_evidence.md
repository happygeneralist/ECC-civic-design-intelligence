# Value and decision evidence

This file explains how the repository supports value-based decision-making, not only user-needs analysis.

## Purpose

The repository should provide the human intelligence needed to design good services, challenge weak or harmful solution ideas, and answer policy, ministerial, product and service questions with evidence.

It should help teams explain:

- what people need
- what creates or destroys value
- what trade-offs are visible
- which solutions are likely to help
- which solutions are unsupported, risky or premature
- what evidence supports or challenges a proposed direction

The purpose is not to support politics. The purpose is to provide a defensible evidence base for better service, policy and design decisions.

## Value is part of the evidence model

Value is not the same as user preference or stakeholder enthusiasm.

Value is created when a policy, service, product, content pattern, process or intervention helps meet real needs, reduce burden, improve outcomes, protect capabilities, or make a system work better for the people affected by it.

In public service and SEND contexts, value may include:

- reducing burden
- improving access
- preserving agency
- reducing harm
- improving trust
- improving transparency
- improving flow through a system
- increasing fairness
- protecting rights
- improving capability
- supporting better institutional decisions

## Why value needs to be explicit

Teams may be asked to pursue a solution because it sounds politically attractive, operationally convenient or intuitively obvious.

A value model helps make the reasoning visible.

It should allow the team to say:

```text
This proposed solution appears attractive, but the evidence suggests it will not create enough value, or may create harm, compared with other options.
```

Or:

```text
The evidence points to a different problem. The proposed solution may not address the user need, civic need, system constraint or value driver that matters most.
```

## Value objects

The repository may use value objects to describe what matters when comparing solutions.

Suggested type:

```yaml
type: value_dimension
id: VAL_001
title:
value_statement:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_basis: none | indicative | traceable | substantiated | validated
related_needs:
related_pain_points:
related_behaviours:
related_insights:
related_capabilities:
related_civic_needs:
related_outcomes:
related_evidence:
tags:
```

Example:

```yaml
type: value_dimension
id: VAL_001
title: Reduce avoidable administrative burden
value_statement: "Reduce work that does not help people achieve the outcome or improve the service."
related_needs:
  - "[[UN_024]]"
related_outcomes:
  - "improved access"
  - "reduced delay"
```

## Solution options

Solutions should be tracked separately from user needs and value dimensions.

Suggested type:

```yaml
type: solution_option
id: SOL_001
title:
solution_type: policy | service | product | content | data | technical | operational | partnership
status: idea | assessing | not_recommended | recommended | deferred | implemented | deprecated
related_needs:
related_value_dimensions:
related_evidence:
expected_value:
risks:
assumptions:
recommendation:
tags:
```

A solution option is not a user need. It is a possible response to needs, evidence and value drivers.

## Evidence basis

Use `evidence_basis` to describe how defensible a need, insight, value dimension or solution assessment is.

```yaml
evidence_basis: none | indicative | traceable | substantiated | validated
```

Definitions:

- `none`: no clear evidence connection yet
- `indicative`: appears in analysis or synthesis, but is not clearly linked to specific evidence
- `traceable`: can be traced to a study, source, quote, observation or data point
- `substantiated`: supported by multiple relevant evidence items, patterns or linked analysis objects
- `validated`: reviewed and strong enough to use for the relevant decision, with evidence, wording and scope checked

Use `evidence_basis` carefully. It is not a claim of absolute truth. It describes how well the object can be traced, defended and used.

## Challenging proposed solutions

When a proposed solution is being assessed, ask:

- What need does this claim to address?
- Is that need traceable, substantiated or validated?
- Which capability, civic need or outcome does it support?
- What value dimensions does it improve?
- What value dimensions might it harm?
- What evidence supports the solution?
- What evidence challenges the solution?
- What assumptions would need to be true for this solution to work?
- Are there higher-value alternatives?
- Is the system ready for this solution?

## Recommendation levels

Use clear recommendation language for solution assessments.

```yaml
recommendation: not_recommended | weak_candidate | promising | recommended | needs_more_evidence | not_yet
```

Definitions:

- `not_recommended`: evidence suggests the solution is unlikely to create enough value or may create harm
- `weak_candidate`: plausible but weakly supported
- `promising`: worth exploring or prototyping
- `recommended`: supported enough for the relevant decision
- `needs_more_evidence`: decision should wait for more evidence
- `not_yet`: may become useful after enabling conditions are met

## Value scoring

Value scores can be useful, but they should not hide judgement.

If scoring is used, keep the rationale visible.

A simple scoring model may include:

```yaml
value_score:
weighted_value_score:
score_rationale:
```

But every score should link back to value dimensions, evidence and assumptions.

## Evidence against a solution is valuable

The repository should not only store evidence that supports solutions.

Evidence that challenges or weakens a solution is especially important when responding to policy pressure or ministerial direction.

Use sections such as:

```markdown
## Evidence supporting this solution

## Evidence challenging this solution

## Risks and harms

## Assumptions

## Recommendation
```

## Relationship to user needs

Validated user needs linked to experience, civic and capability needs are among the strongest artefacts in the repository.

They help show not just what people asked for, but what must be protected, enabled or repaired.

A strong chain might look like:

```text
research evidence
-> user need
-> experience need
-> civic need
-> human capability
-> value dimension
-> solution assessment
```

This allows the team to challenge solution-led thinking with a clearer account of what the evidence actually supports.

## Public service caution

In public services, users often cannot choose whether they interact with the system. They may also be affected by decisions made by ministers, policymakers, institutions or delivery organisations.

That means value should not be framed only as adoption, satisfaction or market fit.

Value should also consider:

- burden
- harm
- fairness
- agency
- rights
- inclusion
- system readiness
- institutional responsibility
- long-term capability

## Practical rule

Use the repository to make value visible, traceable and contestable.

Do not treat a solution as good because it is politically preferred, operationally convenient or easy to describe.

Show what the evidence says, what the evidence does not yet say, and what value is likely to be created or lost.
