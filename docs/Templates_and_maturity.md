# Templates and maturity

This file explains how loose capture, LLM-supported structuring and templates work together.

## Purpose

The repository should support lean agile discovery and development.

That means contributors should be able to move quickly, capture messy material, use an LLM to structure it, and then mature the useful parts over time without losing rigour.

The workflow is:

```text
loose capture -> LLM-supported structuring -> template-governed candidate objects -> selective review -> validation where needed
```

## Core principle

Humans should not have to manually complete every metadata field during discovery.

LLMs may help create structure, metadata, links and candidate analysis objects.

Templates provide consistency so the repository remains queryable, reviewable and adaptable as the team learns.

## Three levels of maturity

### 1. Loose capture

Loose capture is allowed and expected.

Examples:

- rough research notes
- workshop notes
- meeting reflections
- pasted anonymised snippets
- early synthesis notes
- daily notes
- imported summaries

Loose capture does not need full metadata.

The priority is to avoid losing useful signals while keeping raw identifiable data out of the repository.

A loose note might only have:

```yaml
type: loose_note
creation_mode: manual
status: captured
tags:
```

or no frontmatter at all if it is temporary and clearly held in an inbox or working area.

### 2. LLM-supported structuring

The LLM can turn loose notes into structured outputs.

The LLM may propose:

- candidate user needs
- candidate behaviours
- candidate pain points
- candidate insights
- candidate themes
- candidate opportunities
- suggested evidence links
- tags
- actors
- journey stages
- review states
- changelog entries

The LLM should not validate these outputs.

Default metadata for LLM-created candidate objects:

```yaml
status: assumption
analysis_state: candidate
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed
evidence_strength: none
confidence: low
change_level: none
```

If the LLM links the object to relevant evidence, use:

```yaml
status: draft
analysis_state: evidence_linked
evidence_strength: weak
review_status: needs_review
```

### 3. Template-governed maturation

Once an object is worth keeping, it should use the relevant template.

Templates should help the LLM and human contributors create consistent notes without making early capture bureaucratic.

A template should include:

- frontmatter schema
- plain-English guidance
- required sections
- optional sections
- review checklist
- changelog pattern
- examples of good and weak phrasing where useful

## Minimum metadata versus review metadata

Not every field must be complete at creation.

### Minimum metadata for fast candidate objects

```yaml
type:
id:
status:
analysis_state:
creation_mode:
related_evidence:
tags:
```

### Review metadata

These fields should be completed before review or validation:

```yaml
evidence_strength:
confidence:
llm_generated:
human_reviewed:
review_status:
change_level:
supersedes:
superseded_by:
```

If a field is unknown, leave it blank or mark uncertainty explicitly. Do not invent metadata to make a note look complete.

## Template maturity

Templates should be treated as living research infrastructure.

They should evolve as the repository matures, but changes to templates should be deliberate because they shape future analysis.

Template changes should be recorded in `CHANGELOG.md` when they affect:

- required metadata
- review workflow
- object definitions
- status or analysis-state use
- evidence standards
- LLM behaviour

## Suggested template structure

Each analysis template should follow this general pattern:

```markdown
---
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
tags:
---

# Title

## Working formulation

## Evidence basis

## Interpretation

## What remains uncertain

## Related objects

## Review notes

## Changelog
```

## Template use by maturity stage

### Placeholder

Use a lightweight structure.

Purpose: hold a possible pattern without overworking it.

### Candidate

Use the relevant object template, but allow incomplete fields.

Purpose: make the object visible in dashboards and available for linking.

### Drafted

Complete the working formulation and interpretation sections.

Purpose: make the object usable for internal synthesis.

### Evidence-linked

Add explicit evidence links and explain how they support the object.

Purpose: prepare for review.

### Reviewed

Add review notes and update review metadata.

Purpose: show that a human has checked the object.

### Validated

Complete evidence strength, confidence, review status and changelog.

Purpose: allow the object to be used as a reliable finding.

## LLM prompt pattern

Use prompts that ask the LLM to structure, not to finalise.

Example:

```text
Review this loose research note and extract candidate user needs, behaviours, pain points and insights. Use the repository schema. Mark unsupported items as assumptions. Add suggested evidence links where possible. Do not validate anything. Include review status and changelog entries.
```

## What good looks like

A good LLM-structured candidate object is:

- useful enough to keep
- clearly marked as candidate or draft
- linked to evidence where possible
- honest about uncertainty
- easy to review later
- consistent with the relevant template

A poor LLM-structured object is:

- overconfident
- unsupported
- solution-led
- missing review state
- not linked to evidence
- difficult to trace back to the original note

## Practical rule

Loose capture should be easy.

Structured analysis should be consistent.

Validation should be deliberate.
