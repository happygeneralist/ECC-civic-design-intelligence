# Civic design intelligence system

This document captures the strategic vision for the repository as an open civic design intelligence system.

## Definition

A civic design intelligence system is open knowledge infrastructure for public-service needs, evidence, pain and decisions.

It turns fragmented evidence and lived experience into traceable, reusable and contestable knowledge objects that can support public-service design, policy, operations, accountability and open government.

## Why this matters

Public-service understanding is often fragmented across research reports, inspection findings, complaints, Ombudsman decisions, academic studies, operational data, practitioner knowledge, design histories, service documentation and lived experience.

The repository should help maintain a shared understanding of:

- what people need
- what public institutions must uphold
- where people experience pain, burden, harm or exclusion
- where evidence is strong, weak, contested or missing
- which decisions have been made and what knowledge they relied on
- where public-service value is blocked or unsupported

The goal is not only to store research. The goal is to maintain public-service intelligence that can evolve, be challenged and be reused across decisions.

## Core idea

The system separates three layers:

1. **Evidence and contribution layer**  
   Research, public reports, inspections, academic studies, complaints, operational evidence, professional knowledge and lived experience.

2. **Canonical knowledge layer**  
   Reviewed or explicitly status-labelled objects such as user needs, civic needs, pain points, behaviours, risks, evidence, insights, opportunities and outcomes.

3. **Decision and history layer**  
   Design histories, policy records, service improvement decisions and operational decisions that reference stable knowledge objects rather than rewriting them.

This separation lets external insight strengthen the system without directly overwriting the canonical layer.

## Inputs are broader than primary research

Primary research is only one input.

Useful evidence may also come from:

- academic studies and literature reviews
- Ofsted, CQC, Ombudsman and other statutory or regulatory reports
- complaints, appeals, tribunal findings and case reviews
- policy, legislation, statutory guidance and local procedures
- operational data, service metrics and demand data
- frontline practitioner knowledge
- voluntary-sector and advocacy reports
- public or family contributions
- previous service design, discovery and delivery work
- design histories and decision records

Each input should be handled as a source or evidence contribution. It should not automatically become canonical knowledge.

## Public and partner contribution

The long-term vision includes a partner or public-facing contribution system where people and organisations can correct, challenge or enrich the repository.

Potential contributors include:

- children, young people, parents, carers and residents
- third-sector organisations and advocates
- frontline professionals and practitioners
- partner agencies
- researchers and policy specialists
- public-service teams

These contributions may reveal that an official model of the service does not match lived experience. That is a feature of the system, not a problem to suppress.

## Contribution handling principle

Submitted material should be treated as evidence input, not automatic truth.

A contribution may:

- support an existing object
- challenge an existing object
- refine wording or scope
- provide contradictory evidence
- identify a missing need or pain point
- suggest that an object should be superseded
- reveal a sensitivity, safeguarding or privacy issue

The repository should preserve the distinction between:

- submitted knowledge
- candidate knowledge
- reviewed knowledge
- validated knowledge
- deprecated or superseded knowledge

## Suggested contribution states

Future contribution workflows may use states such as:

```yaml
contribution_state: submitted | triaged | linked | candidate | under_review | accepted | partially_accepted | deferred | not_accepted | sensitive_restricted
```

These states are not part of the current MVP schema unless introduced separately. They describe the intended direction for future public or partner contribution workflows.

## Public contestability

The system should make public-service knowledge contestable.

Contestability means that people outside the institution have a structured way to say:

- this need is missing
- this pain point is understated
- this process does not work as described
- this evidence is out of date
- this framing misrepresents lived experience
- this decision did not address the relevant civic need

Contestability does not mean every contribution is accepted. It means that challenges can be captured, linked, reviewed and responded to transparently.

## Relationship to design histories

The repository should integrate with x-gov-style design histories or equivalent public decision records.

A design history should explain what changed and why. It should not need to restate every user need, civic need, pain point or evidence item in full.

Instead, design history entries should reference stable first-class objects.

Example:

```markdown
We changed the pathway entry screen because:

- [[UN_014]] Families need to understand what support is available before formal assessment.
- [[PP_021]] Families are repeatedly asked to provide the same information.
- [[CN_006]] The local area must provide timely, lawful and transparent access to SEND support.
- [[EVID_033]] Ombudsman report on assessment delays.
```

This keeps decisions connected to the knowledge base while avoiding duplication and drift.

## Open government alignment

The system should support open government by making public-service knowledge more:

- transparent
- inspectable
- participatory
- traceable
- accountable
- reusable

Where possible, knowledge objects and decision records should be public by default. However, public access must be balanced with privacy, safeguarding, legal and ethical constraints.

SEND-related material may involve children, disability, family circumstances, trauma, legal disputes or rare combinations of details. Open does not mean unsafe disclosure.

## Safety and privacy

The repository must not expose identifiable or sensitive personal material.

Public or partner contribution workflows should include triage for:

- personal identifiers
- special category data
- safeguarding concerns
- defamation or allegations about identifiable people
- legal sensitivity
- case details that could identify a child, family, school or professional
- consent and permission boundaries

The canonical layer should preserve meaning while reducing unnecessary identifiability.

## MVP implication

The current MVP does not need to build the full public contribution system.

It should preserve the future architecture by:

- using stable IDs for first-class objects
- keeping evidence separate from interpretation
- marking maturity and review status conservatively
- supporting contradictory and limiting evidence
- using object-level change logs for material meaning changes
- avoiding direct overwrite of reviewed objects without review
- allowing future design histories to reference stable objects
- leaving immature or unclear material in an inbox rather than forcing it into the schema

## Naming

Use **civic design intelligence system** as the strategic name for the overall system.

Use **repository** when referring to this Git-based Obsidian implementation.

Use **canonical knowledge layer** when referring to reviewed or explicitly status-labelled first-class objects.

Use **contribution layer** when referring to future public, partner or professional submissions that need triage and review before they affect the canonical layer.
