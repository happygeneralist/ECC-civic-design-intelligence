# LLM intervention logging strategy

LLMs can be useful for migration, synthesis and structuring work, but they can also silently change meaning.

This is especially risky in a research repository where language is not merely presentation. Language can carry evidence, emotion, uncertainty, relational context, power dynamics and implied intervention choices.

This document defines when LLM-assisted changes should be logged separately from Git history and object change logs.

## Core principle

LLM-assisted changes should be classified by semantic risk before they are treated as accepted knowledge.

An LLM edit is not automatically wrong, but it is also not automatically trustworthy. When an LLM changes meaning, evidence relationships or interpretation, the repository should preserve a record of that intervention and mark it for human review where appropriate.

## Why Git is not enough

Git records exact file changes. It does not explain semantic intent or risk.

Git can show that a sentence changed from one wording to another. It cannot reliably answer:

- Did the meaning change?
- Did the LLM narrow or expand the implied solution space?
- Did the LLM remove evidence-specific language?
- Did it turn uncertainty into confidence?
- Did it collapse several different needs into one tidy statement?
- Did a human accept the change?

LLM intervention logs exist to answer those questions.

## Common LLM risks in this repository

LLMs may unintentionally:

- polish away specificity
- generalise concrete evidence
- rewrite participant language into organisational language
- remove emotional or relational nuance
- turn uncertainty into overconfidence
- convert civic or systemic needs into simple content or usability needs
- make evidence sound more coherent than it is
- merge distinct needs, behaviours or pain points
- change actor, level, journey stage or problem framing
- infer relationships that are plausible but not evidence-linked

These are semantic risks, not formatting risks.

## Semantic change classification

Every LLM-assisted edit should be classified before or during the work.

Recommended values:

```yaml
semantic_change: none
semantic_change: possible
semantic_change: material
```

Definitions:

- `none`: metadata, formatting, folder movement or ID normalisation only
- `possible`: wording changed, but the intended meaning is the same
- `material`: meaning, interpretation, evidence basis, relationships, actor, level or implied intervention space changed

## When an LLM intervention log is required

Create an LLM intervention log when an LLM does any of the following:

- rewrites a user need statement
- rewrites evidence-derived language
- summarises raw evidence into an insight
- merges or splits user needs, pain points, behaviours, insights or themes
- changes evidence basis, confidence, status or review status
- adds or removes relationships to evidence, needs, behaviours, pain points or insights
- changes actor, journey stage, need level or civic/service framing
- turns a loose note into a structured object where interpretation is required
- produces a material synthesis used for product, service or policy reasoning

An LLM intervention log is usually not required for:

- YAML formatting
- ID format normalisation
- filename cleanup
- moving loose notes to the inbox
- adding lifecycle fields without changing wording or interpretation
- fixing casing or spelling

Administrative changes can be recorded in the PR summary or a lightweight object change-log entry.

## Low-friction logging modes

Do not create standalone event files for every LLM-assisted action.

Use the lightest mode that preserves the right level of governance:

1. **PR-level LLM note**: for small batches where there is possible semantic risk but no major first-class object rewrite.
2. **Object change-log entry**: for a meaningful but simple update to one object.
3. **Standalone LLM intervention log**: for material semantic changes to first-class objects, especially user needs, evidence-derived insights or maturity changes.

Use standalone event files when the event is likely to need future querying or review.

## Human review rules

If `semantic_change: possible`, the object should normally be marked:

```yaml
review_status: needs_review
```

unless a human immediately reviews and accepts the change.

If `semantic_change: material`, the object must be marked:

```yaml
review_status: needs_review
human_reviewed: false
```

unless a human review occurs as part of the same change.

For first-class objects such as user needs, material LLM-assisted changes should not be treated as validated until reviewed.

## Validation guardrails

LLMs should not upgrade research maturity.

Recommended rules:

- LLMs may set `status: captured` or equivalent migration/current-state values during migration.
- LLMs may set `review_status: needs_review` when semantic risk exists.
- LLMs may not set `review_status: reviewed` unless a human has explicitly reviewed the change.
- LLMs may not set `maturity_state: validated`.
- LLMs may not set `evidence_basis: validated`.
- LLMs may not mark an LLM-assisted material interpretation as accepted without human review.

This prevents plausible language from being mistaken for validated knowledge.

## Recommended LLM intervention log format

LLM intervention logs should live outside the edited object. They should be append-only records of semantic intervention.

Recommended location:

```text
011_Change_events/LLM/
```

Recommended filename pattern:

```text
YYYY-MM-DD_OBJECT-ID_short-description.md
```

Example:

```text
011_Change_events/LLM/2026-06-20_UN_001_need-wording-refinement.md
```

Suggested content:

```markdown
# LLM intervention: UN_001 need wording refinement

## Metadata

- Date: 2026-06-20
- Object: [[UN_001]]
- Object type: user_need
- Actor type: llm
- Actor: ChatGPT
- Human reviewed: false
- Review status: needs_review
- Semantic change: material
- Risk level: material

## Change intent

Clarify the user need statement based on linked evidence.

## Semantic diff

**Before meaning:** The need was framed as access to information.

**After meaning:** The need is framed as interpretive decision support.

**What changed:** The implied intervention space expanded from content or navigation to guided support, comparison and decision scaffolding.

**Reviewer question:** Does the linked evidence justify this broader interpretation?

## Potential risk

This change may alter the implied intervention space from content provision to relational or guided support.

## Evidence considered

- [[EVID_001]]
- [[BEH_001]]

## LLM risk checklist

- Preserved user language: partially
- Changed uncertainty: no
- Changed solution space: yes
- Changed actor: no
- Changed level: possible
- Changed evidence basis: no

## Review notes

Pending human review.
```

## Semantic diff practice

For material LLM changes, record a semantic diff rather than a file diff.

Use this pattern:

```markdown
## Semantic diff

**Before meaning:**

**After meaning:**

**What changed:**

**Risk:**

**Reviewer question:**
```

The semantic diff should explain what changed in interpretation, not repeat the Git diff.

## LLM risk checklist

When an LLM changes wording or interpretation, check:

```yaml
preserved_user_language: yes | no | partially | not_applicable
changed_uncertainty: yes | no | unclear
changed_solution_space: yes | no | unclear
changed_actor: yes | no
changed_level: yes | no | unclear
changed_evidence_basis: yes | no
changed_relationships: yes | no
```

This helps reviewers see whether the LLM has changed the problem framing.

## What the log should capture

The intervention log should describe semantic effects, not duplicate the Git diff.

It should capture:

- change intent
- semantic change classification
- evidence considered
- meaning risks
- review status
- whether the change affects solution space
- whether participant/user language was preserved
- whether uncertainty changed

## What the log should not become

The LLM intervention log should not become:

- a copy of the full file diff
- a long transcript of the chat
- a replacement for Git history
- a mandatory burden for every tiny edit
- a place for the LLM to rewrite the object again

Keep it focused on meaning and governance.

## Operating model for LLM-assisted edits

Before editing, the LLM should state:

```text
Planned change type:
Expected semantic risk:
LLM intervention log required: yes/no
```

After editing, the LLM should report:

```text
Meaning changed: yes/no/possibly
Evidence relationships changed: yes/no
Review status changed: yes/no
LLM intervention log created: yes/no
```

This gives the human reviewer a clear governance checkpoint.

## Suggested fields for affected objects

The edited object may include latest-state fields such as:

```yaml
last_meaningful_change: 2026-06-20
last_change_actor: llm_assisted
last_change_type: wording_refined
semantic_change_review: needs_review
```

These fields point to the state of the object. The detailed audit remains in the event log.

## Strategic purpose

The goal is not to make LLM use difficult. The goal is to prevent silent semantic drift.

LLMs can help create useful structure and synthesis. But in this repository, synthesis is an epistemic act. It changes what the team thinks it knows.

Material LLM changes therefore need a visible trace.