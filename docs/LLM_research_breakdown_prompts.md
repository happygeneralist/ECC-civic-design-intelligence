# LLM research breakdown prompts

This file provides reusable prompts for breaking down research material into candidate problem-space objects.

Use these prompts with the repository schema, templates and writing rules.

## General rules for all prompts

The LLM must:

- keep evidence and interpretation separate
- avoid treating LLM output as evidence
- avoid validating anything
- mark unsupported items as assumptions or candidates
- use `creation_mode: llm_assisted`
- use `llm_generated: true`
- use `human_reviewed: false`
- use `review_status: not_reviewed` or `needs_review`
- preserve uncertainty
- avoid solution-led framing
- follow `docs/User_needs_writing_rules.md` when drafting user needs

## Prompt 1: first-pass breakdown

```text
Review the following anonymised research material and produce a first-pass problem-space breakdown.

Extract candidate:

- evidence items
- user needs
- behaviours
- pain points
- insights
- themes
- opportunities
- value dimensions

Do not validate anything.

For each item, include:

- suggested type
- draft title or formulation
- actor, if known
- journey stage, if known
- need_level, if it is a user need
- evidence_basis: none, indicative, traceable, substantiated or validated
- status
- analysis_state
- confidence
- review_status
- related evidence or source references, if available
- uncertainty or caveats

Use these defaults unless there is a clear reason not to:

status: assumption
analysis_state: candidate
evidence_basis: indicative
confidence: low
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed

Keep evidence and interpretation separate.
Do not create solution options.
```

## Prompt 2: extract candidate user needs

```text
Extract candidate user needs from this anonymised research material.

Follow the repository's user-needs writing rules:

- use action-oriented wording
- avoid cognitive verbs such as know, understand, learn or be aware of unless comprehension itself is the goal
- keep needs solution-agnostic
- use Jobs to Be Done tools where useful for context, progress, pains, gains and strategic opportunity framing
- avoid importing market-led JTBD assumptions uncritically into public service or SEND contexts
- set need_level where possible
- do not collapse experience, service, journey, page and interaction needs
- preserve emotional, social, civic and experience meaning where relevant

For each candidate need, include:

- need statement
- actor
- journey_stage
- need_level
- parent_needs or likely parent level, if inferable
- evidence_basis
- evidence_scope_fit
- wording_sensitivity
- confidence
- status
- analysis_state
- related evidence or source references
- wording rationale, if wording is sensitive
- uncertainty

Do not validate anything.
Mark weak or unlinked needs as assumptions or candidates.
```

## Prompt 3: extract behaviours

```text
Extract candidate behaviours from this anonymised research material.

A behaviour should describe something a person does, avoids, repeats, compensates for or attempts in context.

For each behaviour, include:

- behaviour statement
- actor
- journey_stage
- triggers or conditions
- related needs, pain points or insights if visible
- evidence_basis
- confidence
- status
- analysis_state
- related evidence or source references
- uncertainty

Keep behaviours separate from pain points, needs and solutions.
Do not validate anything.
```

## Prompt 4: extract pain points

```text
Extract candidate pain points from this anonymised research material.

A pain point should describe a barrier, burden, failure, friction, emotional cost or structural problem experienced by an actor.

For each pain point, include:

- pain point statement
- actor
- journey_stage
- likely cause or condition, if visible
- impact or burden
- related needs, behaviours or insights if visible
- evidence_basis
- confidence
- status
- analysis_state
- related evidence or source references
- uncertainty

Keep pain points separate from user needs and solutions.
Do not validate anything.
```

## Prompt 5: draft insights from evidence

```text
Draft candidate insights from the following evidence and analysis notes.

An insight should explain a pattern, not merely repeat evidence.

For each insight, include:

- title
- core claim
- supporting evidence
- contextual evidence
- contradictory or limiting evidence, if visible
- interpretation
- why it matters
- related user needs
- related behaviours
- related pain points
- related themes
- evidence_basis
- confidence
- status
- analysis_state
- uncertainty

Do not validate anything.
Do not turn implications into solution options.
```

## Prompt 6: propose need hierarchy

```text
Review the following candidate user needs and propose a lightweight needs hierarchy.

Use these levels:

- capability
- civic
- experience
- service
- journey
- task
- page
- interaction
- content

For each need, suggest:

- need_level
- likely parent need or parent level
- possible child needs
- related capabilities
- related civic needs
- related rights or outcomes, if visible
- evidence_scope_fit
- wording_sensitivity
- uncertainty

Do not force a complete hierarchy where evidence is thin.
Do not treat solution requirements as user needs.
```

## Prompt 7: identify evidence gaps

```text
Review these candidate objects and identify evidence gaps.

For each object, identify:

- whether the evidence is none, indicative, traceable, substantiated or validated
- whether evidence is direct, partial, contextual or weak for the level of claim
- missing evidence links
- missing source study links
- unsupported assumptions
- contradictory or limiting evidence to look for
- which objects should be deepened before being used for design, policy, prioritisation or stakeholder communication

Do not upgrade status or evidence basis.
```

## Prompt 8: create structured notes

```text
Using the relevant repository templates, create structured Markdown drafts for the selected candidate objects.

Use the correct template shape for each object type.

Set conservative default metadata:

status: assumption
analysis_state: candidate
evidence_basis: indicative
confidence: low
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed

If an item has a specific evidence link, use:

status: draft
analysis_state: evidence_linked
evidence_basis: traceable
review_status: needs_review

Do not validate anything.
Do not create solution options.
Include changelog entries for created notes.
```

## Prompt 9: review wording of user needs

```text
Review these candidate user needs for wording quality.

Check:

- whether the need is solution-agnostic
- whether the verb is appropriate
- whether cognitive verbs are justified
- whether the need is scoped at the right level
- whether JTBD language has been used appropriately for the context
- whether emotional, social, civic and experience meaning has been preserved
- whether one word change would alter the solution direction

For each need, suggest:

- keep as written
- minor wording refinement
- material rewording needed
- split into multiple needs
- merge with another need
- candidate parent or child need

Do not materially reword reviewed or validated needs without flagging that review is required.
```

## Prompt 10: deepen selected object

```text
Deepen this selected candidate object for use in a design, policy, prioritisation or stakeholder decision.

Do the following:

- inspect linked evidence
- identify whether the evidence directly supports the wording and level
- identify missing or weak evidence
- check related needs, behaviours, pain points and insights
- check parent and child needs where relevant
- identify contradictory or limiting evidence
- refine wording only if necessary
- propose evidence_basis, confidence and review_status
- add wording rationale if the object is a user need and wording is sensitive
- draft a changelog entry

Do not validate the object unless a human reviewer has explicitly completed validation.
```

## Practical use

For first-pass analysis, start with prompts 1 and 2.

For a page, service or policy question, use prompts 7, 9 and 10 to deepen only the objects that matter.
