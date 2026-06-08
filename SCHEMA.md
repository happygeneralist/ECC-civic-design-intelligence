# Repository schema

This file defines the common structure for notes in the research repository.

The schema is intended to make the repository queryable, reviewable and safe to use with LLM-assisted workflows.

Use `docs/Lifecycle_states.md` for guidance on valid combinations of `status`, `analysis_state` and `review_status`.

## General rules

Every structured note should have YAML frontmatter.

Every note should have:

```yaml
type:
id:
status:
analysis_state:
evidence_strength:
confidence:
creation_mode:
llm_generated:
human_reviewed:
review_status:
change_level:
tags:
```

Use lower case values for controlled fields unless the ID convention requires capitals.

## Core model

The repository distinguishes between evidence and analysis.

Evidence is captured as close to the source as possible.

Analysis objects are interpreted research objects created from evidence, researcher judgement and synthesis. They include user needs, behaviours, pain points, insights, themes, journeys, personas and opportunities.

The repository should support fast creation and incremental refinement of analysis objects without losing rigour.

The operating principle is:

```text
fast creation, slow validation
```

LLMs may create, decompose, merge, refactor, link and incrementally update analysis objects, provided the work remains status-controlled, evidence-linked where possible, and recorded in the changelog.

## Controlled values

### `status`

```yaml
status: captured | draft | assumption | reviewed | validated | deprecated
```

- `captured`: evidence or information has been recorded but not synthesised.
- `draft`: synthesis has been drafted but not reviewed.
- `assumption`: plausible but not directly supported by sufficient evidence.
- `reviewed`: checked by a human reviewer, but not necessarily validated.
- `validated`: supported by evidence and approved for use as a reliable finding.
- `deprecated`: superseded, withdrawn or no longer recommended for use.

### `analysis_state`

```yaml
analysis_state: captured | placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
```

- `captured`: source material or evidence has been captured.
- `placeholder`: an item exists to hold a possible pattern or object, but it is not yet fully formulated.
- `candidate`: the item appears useful but needs further analysis, evidence or refinement.
- `drafted`: the item has been formulated into a usable draft.
- `evidence_linked`: the item has at least one explicit evidence link, but may still need review.
- `reviewed`: a human has reviewed the item.
- `validated`: the item is reviewed and sufficiently supported to be treated as reliable.
- `deprecated`: the item has been superseded, rejected or withdrawn.

`analysis_state` is a workflow maturity field. `status` is the epistemic status of the claim.

### `evidence_strength`

```yaml
evidence_strength: none | weak | moderate | strong
```

- `none`: no supporting evidence is linked.
- `weak`: limited, indirect or single-source evidence.
- `moderate`: multiple relevant evidence items, but with limitations.
- `strong`: multiple credible evidence items across relevant sources or methods.

### `confidence`

```yaml
confidence: low | medium | high
```

Confidence is the researcher's current judgement about reliability. It should not be used as a substitute for evidence strength.

### `creation_mode`

```yaml
creation_mode: manual | llm_assisted | imported | migrated
```

- `manual`: created directly by a human contributor.
- `llm_assisted`: created or materially shaped with LLM support.
- `imported`: brought in from another source or system.
- `migrated`: created or updated as part of repository restructuring.

### `review_status`

```yaml
review_status: not_reviewed | needs_review | reviewed | rejected
```

### `change_level`

```yaml
change_level: none | minor | material | major
```

- `none`: no meaningful change recorded.
- `minor`: spelling, formatting, metadata tidy-up or link correction.
- `material`: changes the interpretation, wording, evidence links, confidence, status or evidence strength.
- `major`: substantially reframes, splits, merges, replaces or deprecates an item, changes validated content or affects published outputs.

### `need_level`

```yaml
need_level: capability | civic | experience | service | journey | task | page | interaction | content | solution_requirement
```

Use `need_level` to show the scope and hierarchy of a user need or closely related analysis object.

- `capability`: broad human-development requirement, such as dignity, agency, affiliation or control.
- `civic`: institutional obligation, such as dignified access, navigational agency or redressability.
- `experience`: what the person must be able to experience, preserve or recover before any specific service response.
- `service`: what a service must enable across an end-to-end service relationship.
- `journey`: what is needed at a specific journey stage or transition.
- `task`: what the person must do or understand in a specific task.
- `page`: what a page or bounded content context must help the person understand or do.
- `interaction`: what a component, form, filter, prompt or interaction must support.
- `content`: what a content item, explanation or message must support.
- `solution_requirement`: what a specific product, policy, process or intervention must do.

### `evidence_scope_fit`

```yaml
evidence_scope_fit: direct | partial | contextual | weak
```

Use this when evidence supports a need at one level more directly than another.

- `direct`: evidence directly supports this level and wording of need.
- `partial`: evidence supports part of the need, but not the full formulation.
- `contextual`: evidence helps explain context but does not directly prove the need.
- `weak`: evidence is relevant but too indirect to rely on without more work.

### Boolean fields

```yaml
llm_generated: true | false
human_reviewed: true | false
anonymisation_checked: true | false
```

## ID conventions

Use stable IDs. Do not renumber existing items just because the order changes.

```text
RS_001     research study
EVID_001   evidence item
UN_001     user need
BEH_001    behaviour
PP_001     pain point
INS_001    insight
TH_001     theme
PER_001    persona
JNY_001    journey
OPP_001    opportunity
REV_001    review note
CLM_001    claim
```

## Common fields for analysis objects

Use these fields across user needs, behaviours, pain points, insights, themes, journeys, personas and opportunities where relevant.

```yaml
type:
id:
actor:
journey_stage:
status:
analysis_state:
evidence_strength:
confidence:
creation_mode:
llm_generated:
human_reviewed:
review_status:
change_level:
supersedes:
superseded_by:
related_evidence:
related_needs:
related_behaviours:
related_pain_points:
related_insights:
related_themes:
tags:
```

This common structure allows rapid LLM-assisted creation while keeping maturity, evidence, review state and history visible.

## Needs hierarchy fields

Use these fields for user needs and closely related objects where useful.

```yaml
need_level:
parent_needs:
child_needs:
related_capabilities:
related_civic_needs:
related_rights:
related_outcomes:
evidence_scope_fit:
wording_sensitivity: low | medium | high
```

Minimum useful fields for structured user needs:

```yaml
need_level:
parent_needs:
```

Do not force every need to complete every hierarchy field during loose capture. These fields can be added by an LLM or during review as the repository matures.

See `docs/Needs_hierarchy.md` for guidance.

## Object types

### Research study

```yaml
type: research_study
id: RS_001
title:
research_lead:
date_range:
method:
participants:
setting:
status: captured | reviewed | validated | deprecated
analysis_state: captured | reviewed | validated | deprecated
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_insights:
tags:
```

A research study describes an activity or source collection. It should not contain raw identifiable data.

### Evidence

```yaml
type: evidence
id: EVID_001
source_study: "[[RS_001]]"
evidence_kind: quote | observation | survey_result | statistic | document_extract | desk_research | professional_judgement
actor:
context:
journey_stage:
date_collected:
method:
sensitivity: low | medium | high
anonymisation_checked: true | false
confidence: low | medium | high
status: captured | reviewed | deprecated
analysis_state: captured | reviewed | deprecated
creation_mode: manual | llm_assisted | imported | migrated
related_needs:
related_behaviours:
related_pain_points:
related_insights:
tags:
```

Evidence should preserve the meaning of what was captured. Participant quotes should not be rewritten except to remove or mask identifying information.

### User need

```yaml
type: user_need
id: UN_001
actor:
journey_stage:
need:
need_level: capability | civic | experience | service | journey | task | page | interaction | content | solution_requirement
parent_needs:
child_needs:
related_capabilities:
related_civic_needs:
related_rights:
related_outcomes:
evidence_scope_fit: direct | partial | contextual | weak
wording_sensitivity: low | medium | high
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_behaviours:
related_pain_points:
related_insights:
importance: low | medium | high
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

A user need should describe what a person needs to achieve, understand, decide, access, feel or recover from. It should not be written as a solution, feature request or organisational objective.

User needs may be created as placeholders or candidates during rapid research breakdown. They can be incrementally updated as new evidence or thinking emerges, provided the changelog records material changes.

Do not collapse page-level needs, service-level needs and experience-level needs. They operate at different levels and support different decisions.

### Behaviour

```yaml
type: behaviour
id: BEH_001
actor:
journey_stage:
behaviour:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_needs:
related_pain_points:
related_insights:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

A behaviour should describe something a person does, avoids, repeats, compensates for or attempts in context.

Behaviours may be drafted quickly from evidence, but should remain candidates until the pattern has been reviewed and linked to appropriate evidence.

### Pain point

```yaml
type: pain_point
id: PP_001
actor:
journey_stage:
pain_point:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_needs:
related_behaviours:
related_insights:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

A pain point should describe a barrier, burden, failure, friction, emotional cost or structural problem experienced by an actor.

Pain points may be captured as candidates while breaking down research. They should not be treated as validated until reviewed and evidenced.

### Insight

```yaml
type: insight
id: INS_001
title:
actor:
journey_stage:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_needs:
related_behaviours:
related_pain_points:
related_themes:
claims:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

An insight is a research-backed interpretation that explains why something is happening and why it matters. It should include evidence, interpretation, uncertainty and implications.

### Theme

```yaml
type: theme
id: TH_001
title:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_needs:
related_behaviours:
related_pain_points:
related_insights:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

A theme groups related evidence and analysis objects. A theme should not imply validation of all items within it.

### Opportunity

```yaml
type: opportunity
id: OPP_001
title:
actor:
journey_stage:
opportunity:
status: draft | assumption | reviewed | validated | deprecated
analysis_state: placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
creation_mode: manual | llm_assisted | imported | migrated
related_evidence:
related_needs:
related_behaviours:
related_pain_points:
related_insights:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
change_level: none | minor | material | major
supersedes:
superseded_by:
tags:
```

An opportunity suggests a possible area for design, service or policy intervention. It is not a decision or commitment.

### Review note

```yaml
type: review_note
id: REV_001
reviewed_item:
reviewer:
review_date:
review_outcome: approved | changes_requested | rejected | deferred
status:
analysis_state:
evidence_strength:
confidence:
change_level:
tags:
```

Review notes should document material decisions, especially when an item is promoted, downgraded, deprecated, split, merged or materially changed.

## Entry-level changelog

Every structured note should include an entry-level changelog section.

```markdown
## Changelog

- YYYY-MM-DD: Created as LLM-assisted candidate. Status: assumption. Analysis state: candidate. Evidence strength: weak. Review status: not reviewed.
```

Record material changes to claims, wording, status, analysis state, confidence, evidence strength, evidence links, splitting, merging, supersession and review outcomes.

## Fast-moving analysis workflow

Analysis objects may be created before they are fully reviewed.

This is expected and useful when breaking down research at scale.

Use this progression:

```text
placeholder -> candidate -> drafted -> evidence_linked -> reviewed -> validated
```

Not all objects need to reach validation. Some may remain as candidates, assumptions or weak signals until they become important enough to review.

## Needs visibility and tending

Staleness is not the current priority.

A need may remain valuable even if it has not been recently edited. The immediate problem is lack of visibility, not too many needs.

Prioritise making needs visible, connected, scoped and evidence-aware. Tend the repository by linking, pruning, splitting, merging, reviewing or deepening needs when the work requires it.

## Splitting, merging and supersession

When an analysis object is split, merged, replaced or substantially reframed, record the relationship.

```yaml
supersedes:
  - "[[UN_004]]"
superseded_by:
  - "[[UN_024]]"
change_level: major
```

Use changelog entries to explain what changed and why.
