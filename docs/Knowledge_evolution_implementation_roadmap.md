# Knowledge evolution implementation roadmap

This roadmap describes a staged implementation approach for knowledge evolution, user need persistence, pain point recurrence and LLM intervention logging.

The aim is to establish useful governance without slowing down the current research migration work.

## Stage 1: Agree the model

Review and agree the core distinctions:

- Git history is the technical audit trail.
- Object change logs are the human-readable knowledge evolution trail.
- LLM intervention logs are the semantic-risk and governance trail.

Agree that first-class objects, especially user needs, should be persistent, traceable and supersedable.

Agree that pain points should remain visible when resolved, dormant or at risk of recurring, because they can indicate coverage, regression risk and blocked value delivery.

## Stage 2: Establish minimum viable practice

Start with lightweight working rules before changing the schema.

Minimum viable practice:

1. Use PR summaries for administrative migration batches.
2. Add lightweight object change logs only where meaning changes.
3. Start with user needs as the first-class object requiring change-log discipline.
4. Do not create change events for metadata cleanup.
5. Use LLM intervention logs only for material semantic risk.
6. Treat resolved or dormant pain points as useful service intelligence, not waste.

## Stage 3: Update templates lightly

Start with user needs only.

Update the user need template to include:

```markdown
## Change log

- YYYY-MM-DD: Created/captured. Source: [study/evidence/insight]. Status: captured.
```

Do not add complex event structures to every template yet.

Possible optional frontmatter additions for user needs:

```yaml
lifecycle_state: active
maturity_state: captured
last_meaningful_change:
supersedes:
superseded_by:
deprecation_reason:
```

Only require fields that are useful now. Optional fields should remain optional until the repository has more examples.

Avoid adding `version` until there is a clear rule for when it increments. If versioning is introduced later, increment only for material or major meaning changes, not administrative edits.

## Stage 4: Add LLM operating rules

Before any LLM-assisted edit to first-class objects, require the LLM to state:

```text
Planned change type:
Expected semantic risk:
LLM intervention log required: yes/no
```

After the edit, require:

```text
Meaning changed: yes/no/possibly
Evidence relationships changed: yes/no
Review status changed: yes/no
LLM intervention log created: yes/no
```

This does not require tooling immediately. It can begin as a working convention in chats and PR descriptions.

Add the rule that LLMs must not mark objects as validated or reviewed unless a human has explicitly completed that review.

## Stage 5: Create the change-events folder

Create:

```text
011_Change_events/
  README.md
  LLM/
  Objects/
  Reviews/
```

At first, use this only for:

- material LLM-assisted changes
- user need split, merge, supersede or deprecation
- pain point resolution, dormancy or recurrence-risk changes
- evidence-basis changes
- review or validation decisions

Do not log administrative changes here.

Treat the folder as optional and experimental until real examples show what needs to be validated.

## Stage 6: Add pain point recurrence fields cautiously

Once examples exist, update the pain point template with optional fields such as:

```yaml
lifecycle_state: active | resolved | dormant | deprecated
resolution_state: unresolved | partially_addressed | addressed_currently | no_longer_observed
recurrence_risk: low | medium | high
recurrence_conditions:
```

Do not require these immediately for all existing pain points.

Use them first where they support product/service analysis, such as identifying unresolved pain, value blockers or recurrence risk.

## Stage 7: Add validator checks cautiously

Only add validator rules once the pattern has been tested manually.

Possible future checks:

- if `lifecycle_state: superseded`, require `superseded_by`
- if `lifecycle_state: deprecated`, require `deprecation_reason`
- if `lifecycle_state: dormant`, allow but do not require `recurrence_risk`
- if `semantic_change_review: needs_review`, require `review_status: needs_review`
- if `last_change_actor: llm_assisted` and `change_level: material`, require either a PR-level LLM note or a linked change event

Avoid strict validation too early. The goal is to support research governance, not block useful work with premature schema constraints.

## Stage 8: Query and reporting layer

Once examples exist, build queries or scripts to report:

- user needs by maturity
- superseded and deprecated needs
- LLM-assisted material changes awaiting review
- objects with evidence basis changes
- unresolved pain points
- dormant pain points that may recur
- pain points blocking value delivery
- needs that underpin product or service decisions
- validated needs not yet covered by interventions or service responses

This is where the strategy becomes a source of product and service intelligence.

## Recommended first implementation PR

A practical first implementation PR could include:

1. `011_Change_events/README.md`
2. `011_Change_events/LLM/.gitkeep`
3. `011_Change_events/Objects/.gitkeep`
4. `011_Change_events/Reviews/.gitkeep`
5. A small update to `Templates/User_need_template.md` adding `## Change log`
6. A short note in `docs/Repository_validation.md` explaining that change-event validation is future work

Do not add strict validator rules in this first implementation PR.

## What not to do yet

Do not immediately:

- create detailed change logs for every existing object
- require LLM event logs for every administrative migration
- force every template to include complex history structures
- build a central ledger before there are real examples
- make the validator enforce rules before the team understands the workflow
- add versioning before there is a clear version-increment rule
- treat resolved pain points as if they should be deleted

## Success criteria

This system is working when:

- user needs can evolve without losing their lineage
- deprecated, resolved or dormant pain points remain historically visible
- LLM-assisted semantic changes are reviewable
- Git is not duplicated inside notes
- future analysis can distinguish mature knowledge from unreviewed synthesis
- dashboards can show unresolved pain, recurrence risk and blocked value delivery
- the process is light enough that people actually use it