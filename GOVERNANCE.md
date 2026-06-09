# Repository governance

This file defines the practical governance rules for the research repository.

For the legal basis and data protection rationale, see `docs/Governance_legal_basis.md`.

## Governance purpose

The repository exists to support evidence-based service design and public decision-making by making anonymised research knowledge reusable, traceable and reviewable.

It is also intended to form part of a wider civic design intelligence system: open knowledge infrastructure for public-service needs, evidence, pain and decisions.

Governance should ensure that:

- evidence is handled safely
- assumptions are clearly marked
- analysis objects remain traceable to evidence where possible
- fast-moving draft work does not get mistaken for validated findings
- external contributions can challenge or enrich the knowledge base without directly overwriting canonical objects
- material changes are reviewed or made visible for review
- LLM-generated and LLM-assisted content is controlled
- validated findings are not changed without a clear review trail

## Operating principle

The repository should support:

```text
fast creation, slow validation
```

Fast creation means contributors and LLMs may create candidate or placeholder analysis objects quickly while breaking down research.

Slow validation means these objects are not treated as reliable findings until their evidence, interpretation, status and review state justify it.

## Open civic intelligence principle

The repository should be open, inspectable and contestable where it is safe and appropriate to do so.

People outside the institution may hold better knowledge about how a service is actually experienced. This includes families, residents, third-sector organisations, advocates, frontline professionals, partner agencies and researchers.

External knowledge should be welcomed as evidence input, challenge or correction. It should not bypass triage, safeguarding, privacy checks, evidence assessment or human review.

## Roles

### Repository owner

Responsible for repository structure, access, permissions and overall quality.

### Research lead

Responsible for research integrity, interpretation quality and whether evidence supports a finding.

### Contributor

May add evidence, draft notes, suggest links, create candidate analysis objects and create synthesis outputs within the repository rules.

### External contributor

May submit evidence, corrections, lived experience, professional knowledge, partner intelligence or challenges to existing objects.

External contributors do not directly change canonical knowledge objects unless a governed contribution workflow and appropriate permissions exist. Their contributions should be triaged, linked, reviewed and incorporated where appropriate.

### Reviewer

Reviews draft, candidate or assumption-based material and decides whether it can be promoted, revised, rejected, deprecated or kept as an assumption.

### LLM assistant

May help capture structure, classify, summarise, link, create, decompose, merge, refactor and incrementally update analysis objects, but cannot validate research findings.

## What may be stored

The repository may store:

- anonymised quotes
- anonymised observations
- survey findings
- coded evidence
- study summaries
- academic, sector, statutory, regulatory, Ombudsman, inspection, policy and operational evidence
- triaged public, partner or professional contributions
- user needs
- civic needs
- behaviours
- pain points
- insights
- themes
- personas
- journeys
- opportunities
- review notes
- synthesis outputs

## What must not be stored

The repository must not store:

- raw transcripts
- audio or video recordings
- names or direct identifiers of participants
- contact details for participants
- identifiable special category data
- unredacted case details
- unsupported claims presented as validated findings

## Evidence and analysis

Evidence and analysis must be kept distinct.

Evidence notes should capture what was observed, said, measured or sourced.

Analysis objects are interpreted research objects created from evidence, researcher judgement and synthesis. They include user needs, civic needs, behaviours, pain points, insights, themes, journeys, personas and opportunities.

A claim without evidence may still be useful, but it must be marked as an assumption, candidate or placeholder as appropriate.

## External contribution governance

External contributions may support, challenge, refine or contradict existing objects.

Before they affect canonical knowledge, they should be assessed for:

- relevance
- source clarity
- sensitivity
- identifiability
- safeguarding concerns
- legal risk
- evidence strength
- relationship to existing objects
- whether they introduce contradiction, uncertainty or a need for review

External contributions may lead to:

- a new evidence note
- a candidate user need, civic need, behaviour, pain point, insight or risk
- an update to supporting, contradictory or limiting evidence
- a material change to an existing object
- a decision to defer, reject or restrict the contribution

Material changes caused by external contributions should be recorded in the relevant object changelog.

## Validation authority

Only a human reviewer may mark an item as validated.

An item can be validated only when:

- the claim is clear
- linked evidence supports the claim
- uncertainty and limitations are documented
- anonymisation has been checked where relevant
- the item has been reviewed
- the changelog has been updated

## Change control

Changes are classified as:

- `minor`: spelling, formatting, metadata correction or link fix
- `material`: changes interpretation, wording, linked evidence, confidence, status, analysis state or evidence strength
- `major`: substantially reframes, splits, merges, replaces or deprecates an item, alters validated content or affects published outputs

Material and major changes require a review trail.

## LLM-assisted changes

LLM-assisted changes must follow `llm-instructions.md`.

LLMs may create and alter analysis objects, including user needs, behaviours, pain points, insights, themes, journeys, personas and opportunities.

LLMs may create placeholder, candidate, drafted and evidence-linked objects at speed.

They must not:

- validate findings
- upgrade evidence strength on reviewed or validated items
- remove caveats
- materially alter validated notes without review
- silently rewrite participant evidence
- hide the fact that an item was LLM-assisted

LLM-generated content should be marked with:

```yaml
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed
```

For unsupported but useful candidate objects, use:

```yaml
status: assumption
analysis_state: candidate
evidence_strength: none
confidence: low
```

## Pull request expectations

Repository changes should be made through branches and pull requests where possible.

A pull request should explain:

- what changed
- why it changed
- whether research content changed
- whether assumptions were introduced
- whether placeholder or candidate objects were created
- whether evidence links were added or changed
- whether any status, analysis state or evidence strength changed
- whether any external contribution was used to support, challenge or change an object
- whether any items were split, merged, superseded or deprecated
- what still requires review

## Audit and review

The repository should be reviewed periodically for:

- unsupported validated claims
- weakly sourced analysis objects
- assumptions that have not been reviewed
- candidate objects that have become important but remain unreviewed
- evidence without source studies or source references
- external contributions that remain untriaged
- notes missing required metadata
- identifiable or sensitive material
- broken or inconsistent IDs
- missing changelog entries for material changes

Findings from audits should be recorded in `CHANGELOG.md` or review notes, depending on scope.
