# Review process

This file defines how repository items move from capture, placeholder or draft into reviewed and validated states.

## Review purpose

Review protects the repository from:

- unsupported claims
- overconfident synthesis
- hidden assumptions
- evidence drift
- accidental loss of caveats
- unsafe handling of participant material
- LLM-generated material being treated as evidence
- candidate analysis objects being mistaken for validated findings

## Review states

The repository uses three related fields: `status`, `analysis_state` and `review_status`.

### Status

```yaml
status: captured | draft | assumption | reviewed | validated | deprecated
```

`status` describes the epistemic state of the item: how reliable or claim-like it is.

### Analysis state

```yaml
analysis_state: captured | placeholder | candidate | drafted | evidence_linked | reviewed | validated | deprecated
```

`analysis_state` describes workflow maturity: where the item is in the analysis lifecycle.

### Review status

```yaml
review_status: not_reviewed | needs_review | reviewed | rejected
```

`review_status` describes whether a human review has happened and what is needed next.

## Promotion path

### Evidence

```text
captured -> reviewed -> deprecated, if no longer usable
```

Evidence is usually not `validated` in the same sense as an insight or user need. It is captured, anonymised, checked and reviewed.

### Analysis objects

Analysis objects include user needs, behaviours, pain points, insights, themes, journeys, personas and opportunities.

They may move through this path:

```text
placeholder -> candidate -> drafted -> evidence_linked -> reviewed -> validated
```

They may also remain as placeholders, candidates or assumptions if they are useful but not yet important enough to review.

This is expected in a fast-moving repository.

## Review checklist for evidence

- [ ] The source study is identified or the missing source is explicitly noted.
- [ ] The evidence kind is clear.
- [ ] The actor is clear where known.
- [ ] The quote, observation or data point is anonymised.
- [ ] No raw transcript, recording or identifiable participant data is included.
- [ ] The confidence level is appropriate.
- [ ] Links to related notes are accurate.
- [ ] The changelog has been updated if the evidence has changed.

## Review checklist for analysis objects

Use this checklist for user needs, behaviours, pain points, insights, themes, journeys, personas and opportunities.

- [ ] The object type is correct.
- [ ] The actor and journey stage are clear where relevant.
- [ ] The object is marked with the correct `status`.
- [ ] The object is marked with the correct `analysis_state`.
- [ ] The evidence strength is appropriate.
- [ ] The confidence level is appropriate.
- [ ] Evidence links are present where available.
- [ ] Lack of evidence is visible where evidence is missing.
- [ ] Assumptions are explicitly labelled.
- [ ] Related objects are linked where useful.
- [ ] Material or major changes are recorded in the changelog.
- [ ] Split, merged or superseded objects have `supersedes` / `superseded_by` links where relevant.

## Review checklist for user needs

- [ ] The need is framed from the user's perspective.
- [ ] The need is not a solution, feature or organisational goal.
- [ ] The actor and journey stage are clear.
- [ ] The need links to relevant evidence, or is marked as an assumption, placeholder or candidate.
- [ ] Evidence strength is appropriate.
- [ ] Confidence is appropriate.
- [ ] Related behaviours, pain points and insights are linked where relevant.
- [ ] The status and analysis state are justified.
- [ ] The changelog is up to date.

## Review checklist for behaviours

- [ ] The behaviour describes something a person does, avoids, repeats or compensates for.
- [ ] The behaviour is linked to evidence, or marked as an assumption, placeholder or candidate.
- [ ] The actor and journey stage are clear.
- [ ] Barriers, triggers or conditions are separated from the behaviour itself.
- [ ] Evidence strength and confidence are appropriate.
- [ ] The status and analysis state are justified.
- [ ] The changelog is up to date.

## Review checklist for pain points

- [ ] The pain point describes a barrier, burden, failure, friction or emotional cost.
- [ ] It is linked to evidence, or clearly marked as an assumption, placeholder or candidate.
- [ ] It is not written as a proposed solution.
- [ ] The affected actor is clear.
- [ ] The service, system or journey context is clear where known.
- [ ] Evidence strength and confidence are appropriate.
- [ ] The status and analysis state are justified.
- [ ] The changelog is up to date.

## Review checklist for insights

- [ ] The core claim is clear.
- [ ] The insight explains why something is happening and why it matters.
- [ ] Major claims link to evidence.
- [ ] Contradictory or limiting evidence has been considered.
- [ ] Assumptions are explicitly labelled.
- [ ] Design, service or policy implications are separated from evidence.
- [ ] Evidence strength and confidence are appropriate.
- [ ] The item has not been over-promoted.
- [ ] The status and analysis state are justified.
- [ ] The changelog is up to date.

## Review checklist for LLM-generated or LLM-assisted content

- [ ] `creation_mode: llm_assisted` is present where appropriate.
- [ ] `llm_generated: true` is present where the object was generated or materially shaped by an LLM.
- [ ] `human_reviewed: false` remains until a human review has happened.
- [ ] The item is not marked as validated.
- [ ] Claims are traceable to evidence or marked as assumptions.
- [ ] Placeholder and candidate states are visible.
- [ ] No participant quote has been silently rewritten.
- [ ] No caveats have been removed.
- [ ] Evidence strength has not been upgraded without review.
- [ ] The proposed changelog entry is accurate.

## Recording review decisions

For small changes, record the decision in the item's changelog.

For material or major changes, create a review note or add a detailed review section.

Example:

```markdown
## Review

- Review date: 2026-06-08
- Reviewer:
- Outcome: changes requested
- Rationale: Claim is plausible but only linked to one weak evidence item.
- Required action: Keep as candidate assumption until additional evidence is added.
```

## Validation threshold

An item may be marked as validated only when:

- it has been reviewed by a human
- it links to relevant evidence
- evidence strength is at least moderate, unless a clear exception is documented
- the claim is precise enough to test or challenge
- limitations are documented
- the changelog records the promotion

## Deprecation

Use `deprecated` when an item is superseded, contradicted, duplicated or no longer safe to use.

Deprecated notes should not be deleted unless there is a safety, legal or data protection reason. Prefer preserving the audit trail.
