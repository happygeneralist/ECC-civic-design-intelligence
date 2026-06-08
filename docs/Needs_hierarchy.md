# Needs hierarchy

This file defines a lightweight MVP hierarchy for user needs and related civic needs work.

It is based on the principle that services are not the source of many needs. Services are one way institutions respond to broader experience, civic and capability needs.

## Purpose

The repository needs to support fast capture of user needs while also helping researchers and designers understand the level, scope and lineage of each need.

A need may be useful even if it is not yet fully evidenced or linked to specific quotes. The important thing is to make its level, evidence state and relationships visible.

## MVP hierarchy

Use this hierarchy as a practical starting point:

```text
capability / life need
↓
civic need
↓
experience need
↓
service need
↓
journey need
↓
task or page need
↓
interaction or content need
↓
solution requirement
```

## Need levels

Use the `need_level` field for user needs and closely related analysis objects.

```yaml
need_level: capability | civic | experience | service | journey | task | page | interaction | content | solution_requirement
```

### Capability need

Question: what must a person be able to be or do to live with dignity?

Examples:

- have practical reason
- have control over one's environment
- maintain affiliation and belonging
- live with dignity and safety

Capability needs are broad human-development commitments. They are not service requirements.

### Civic need

Question: what must institutions uphold so capabilities are realistically possible?

Examples:

- dignified access
- navigational agency
- redressability
- relational security
- structural sufficiency

Civic needs describe institutional obligations, not user preferences.

### Experience need

Question: what must the person be able to experience, preserve or recover before any specific service response?

Examples:

- feel that I have a future
- understand what is possible for someone like me
- feel safe asking for help without shame or blame
- maintain agency when other people are making decisions about me

Experience needs sit between civic/capability needs and service needs. A service may help meet them, but they should not be collapsed into service requirements.

### Service need

Question: what must a service enable across an end-to-end service relationship?

Examples:

- get joined-up support to plan a realistic pathway
- get clear and timely guidance across education, health and work transitions
- understand available support without navigating disconnected services alone

Service needs are still solution-agnostic. They describe what the service must enable, not the specific product, page or feature.

### Journey need

Question: what does the person need at a specific stage of a journey?

Examples:

- compare post-16 options before making a decision
- prepare for a transition review
- recover confidence after a previous pathway failed

Journey needs connect evidence and analysis to moments, stages and transitions.

### Task or page need

Question: what must the person understand or do in a specific task, page or content context?

Examples:

- understand whether this course is suitable for someone with my support needs
- know what evidence is required before starting an application
- understand what happens after I submit a form

Page-level and task-level needs can strongly shape content, interaction and information architecture. They should not be collapsed into broader service-level needs.

### Interaction or content need

Question: what must a component, content block, form field, filter, prompt or interaction support?

Examples:

- filter options by support type, location and entry requirements
- see an explanation of eligibility terms in plain language
- save progress when interrupted

This level is close to design execution but should still be framed as a need until it becomes a specific solution requirement.

### Solution requirement

Question: what must the specific product, service, policy, process or intervention do?

Examples:

- provide a plain-language eligibility checker
- include a save-and-return function
- expose support options, suitability and entry requirements on course pages

Solution requirements are implementation decisions. They should link back to needs rather than replace them.

## Required fields for MVP hierarchy

For structured user needs, include:

```yaml
need_level:
parent_needs:
```

Use these fields where useful:

```yaml
child_needs:
related_capabilities:
related_civic_needs:
related_rights:
related_outcomes:
```

Do not force every note to complete every field during loose capture. These fields can be added by an LLM or during review as the repository matures.

## Parent and child needs

Use parent and child links to show need lineage.

```yaml
parent_needs:
  - "[[UN_010]]"
child_needs:
  - "[[UN_024]]"
  - "[[UN_025]]"
```

A lower-level need should be traceable upwards where possible.

Example chain:

```text
Capability: control over one's environment
Civic need: navigational agency
Experience need: understand what is possible for someone like me
Service need: get joined-up support to plan a realistic pathway
Page need: understand whether this course fits my support needs
Solution requirement: show suitability, support options and eligibility clearly
```

## Do not collapse levels

Avoid collapsing page-level needs and service-level needs.

A service-level need explains what must be enabled across the service experience.

A page-level need explains what a person must understand or do in a specific context.

For example:

```text
Service need: I need joined-up support to plan a realistic pathway.
Page need: I need to know whether this course is suitable for someone with my support needs.
```

Both are valid. They operate at different levels and support different decisions.

## Evidence may support levels differently

Evidence does not support every level equally.

A quote about not understanding course eligibility may be direct evidence for a page-level information need, but only contextual evidence for a broader service-level need around pathway guidance.

Use this optional field when useful:

```yaml
evidence_scope_fit: direct | partial | contextual | weak
```

Definitions:

- `direct`: evidence directly supports this level and wording of need
- `partial`: evidence supports part of the need, but not the full formulation
- `contextual`: evidence helps explain the context but does not directly prove the need
- `weak`: evidence is relevant but too indirect to rely on without more work

This helps avoid overextending evidence from one level to another.

## Wording sensitivity

Small wording changes can change the solution vector.

For user needs, use this optional field when the wording carries design or strategic risk:

```yaml
wording_sensitivity: low | medium | high
```

For high-sensitivity needs, include:

```markdown
## Wording rationale

Why this wording was chosen and what alternative wording would imply.
```

Example:

```text
I need to know what options exist.
```

points towards information provision.

```text
I need to understand which options are appropriate for my child.
```

points towards interpretation, guidance and decision support.

## Garden model: visibility and tending

Staleness is not the current priority.

A need may be valuable even if it has not been touched recently. The immediate problem is lack of visibility, not too many needs.

Think of the repository as a garden:

- loose notes are seeds
- candidate needs are seedlings
- evidence-linked needs are growing plants
- reviewed and validated needs are mature plants
- tending means linking, pruning, splitting, merging, reviewing or deepening when the work requires it

Do not deprecate or hide a need merely because it has not been recently edited.

Instead, prioritise:

- visibility
- connection
- accurate scope
- evidence awareness
- deepening when a decision depends on it

## MVP rule

For now, keep the hierarchy lightweight.

The minimum useful fields are:

```yaml
need_level:
parent_needs:
```

Add richer civic, capability, rights and outcome links when they help the work, not as bureaucracy.
