# Research breakdown workflow

This file defines the practical workflow for turning new research material into candidate evidence, user needs, behaviours, pain points, insights, themes, opportunities and value dimensions.

It is designed for fast, safe research analysis using Obsidian, GitHub and LLM support.

## Purpose

The goal is to build visibility of the problem space quickly without pretending that every item is fully evidenced or reviewed.

Use this workflow when you need to break down research at pace and create a useful map of what may be going on.

## Core principle

```text
capture quickly -> structure with LLM support -> mark uncertainty honestly -> deepen only when needed
```

The repository should support incomplete-but-visible knowledge. Candidate needs, behaviours, pain points and insights are valuable if their status, evidence basis and review state are clear.

## First-pass workflow

### 1. Add material to the inbox

Add loose material to `000_Inbox/`.

Use `Templates/Loose_capture_template.md` where helpful.

Acceptable material includes:

- anonymised research notes
- meeting or workshop notes
- source summaries
- first-pass synthesis
- pasted anonymised excerpts
- LLM extraction outputs

Do not add raw transcripts, recordings, identifiable participant data or unredacted case details.

### 2. Create a source or study note when useful

If the material belongs to a distinct research activity, create or update a research study note in `001_Research_studies/`.

Use `Templates/Research_study_template.md`.

If structured objects are created from an inbox note or source summary, preserve a trace back to the source.

Use links such as:

```yaml
source_note: "[[000_Inbox/example_note]]"
source_study: "[[RS_000]]"
```

If the object is not linked to specific quotes yet, source-level traceability is still useful.

### 3. Ask the LLM to structure the material

Use the prompt patterns in `docs/LLM_research_breakdown_prompts.md`.

Ask the LLM to extract candidate:

- evidence items
- user needs
- behaviours
- pain points
- insights
- themes
- opportunities
- value dimensions

The LLM should not validate anything.

### 4. Create structured notes only for useful objects

Do not create a note for every possible fragment.

Create structured notes when an item is useful enough to keep, link, review or deepen later.

Use the relevant template:

- `Templates/Evidence_template.md`
- `Templates/User_need_template.md`
- `Templates/Behaviour_template.md`
- `Templates/Pain_point_template.md`
- `Templates/Insight_template.md`
- `Templates/Theme_template.md`
- `Templates/Opportunity_template.md`
- `Templates/Value_dimension_template.md`

### 5. Use honest default metadata

Use `evidence_basis` as the primary indicator of whether an object is none, indicative, traceable, substantiated or validated.

Use `evidence_strength` only as a secondary field while it remains in the schema.

For LLM-created candidate objects without direct evidence links, use:

```yaml
status: assumption
analysis_state: candidate
evidence_basis: indicative
evidence_strength: none
confidence: low
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed
```

For LLM-created objects linked to specific evidence, use:

```yaml
status: draft
analysis_state: evidence_linked
evidence_basis: traceable
evidence_strength: weak
confidence: low | medium
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: needs_review
```

Do not use:

```yaml
evidence_basis: validated
```

unless a human reviewer has explicitly completed validation.

### 6. Do not force quote-linking up front

It is acceptable to create a candidate user need or insight from a source-level reading of research before it is linked to every quote.

This creates breadth and visibility.

Deepen later when the item is needed for design, policy, prioritisation, technical analysis or stakeholder communication.

### 7. Deepen when consequences increase

Deepen a candidate object when it will be used for:

- page or content design
- service design
- policy challenge
- prioritisation
- stakeholder-facing synthesis
- value assessment
- technical or data requirements
- review or validation

Deepening may include:

- linking specific evidence
- checking wording
- linking parent and child needs
- connecting to civic or capability needs
- checking contradictory evidence
- adding review notes
- promoting status only when justified

### 8. Resolve the inbox note

After a first-pass breakdown, do not leave the inbox note in an ambiguous state.

Choose one of these outcomes:

- keep the inbox note as source context and link structured objects back to it
- move useful objects into structured folders
- archive or delete temporary LLM output that no longer has value
- add a follow-up note explaining what still needs processing

The inbox is a staging area, not a permanent store of unresolved analysis.

## User needs breakdown rules

When creating user needs, follow:

- `docs/User_needs_writing_rules.md`
- `docs/Needs_hierarchy.md`
- `docs/Lifecycle_states.md`

In particular:

- keep needs solution-agnostic
- use action-oriented wording
- avoid cognitive verbs unless justified
- set `need_level` where possible
- do not collapse experience, service, page and interaction needs
- preserve emotional, social and civic meaning where relevant
- record wording rationale when small wording changes would change the solution direction

LLM-generated user needs are candidate formulations, not final wording.

Do not treat a generated need as stable until it has been reviewed for wording, level, evidence basis and solution-vector risk.

## Evidence handling

Evidence should remain close to the source.

The LLM may suggest evidence items, but should not rewrite participant quotes except for anonymisation suggestions.

If a candidate object is not directly linked to evidence, make that visible with:

```yaml
evidence_basis: indicative
```

If it is linked to a study or source but not a specific excerpt, make that clear in the note body.

## Problem-space focus

This repository is focused on the problem space.

It should capture:

- evidence
- needs
- behaviours
- pain points
- insights
- themes
- journeys
- opportunities
- value dimensions

Do not turn this workflow into solution tracking.

Opportunities and value dimensions may create future connection points for solution-mapping work, but solution options should not be treated as research findings in this repository.

## First-pass output checklist

After a first-pass breakdown, check:

- [ ] No raw identifiable data has been added.
- [ ] Candidate objects are marked as candidate or assumption.
- [ ] LLM-generated objects are marked as LLM-generated.
- [ ] Evidence basis is not overstated.
- [ ] No object is marked with `evidence_basis: validated` unless a human reviewer has explicitly validated it.
- [ ] User needs are solution-agnostic.
- [ ] LLM-generated user needs are treated as candidate formulations, not final wording.
- [ ] Need levels are added where possible.
- [ ] Important uncertainty is visible.
- [ ] Structured objects preserve a trace back to the source note or study where possible.
- [ ] Material needing later review is easy to find.
- [ ] The inbox note has an explicit next state: retained as source context, moved into structured notes, archived/deleted, or marked for follow-up.

## Changelog guidance

First-pass candidate creation does not need heavy changelog detail.

Use changelogs for:

- material wording changes
- evidence links added or removed
- status or analysis-state changes
- splits, merges or supersessions
- review outcomes
- validation decisions

## Practical rule

Do not try to finish the map in one pass.

Create enough structure to see the problem space, then deepen the parts that matter when the work demands it.
