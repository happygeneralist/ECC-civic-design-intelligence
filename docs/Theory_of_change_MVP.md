# Theory of change MVP

This document describes the minimum viable theory of change for the civic design intelligence system.

It explains how a structured research repository can improve public-service decision-making by turning fragmented evidence into traceable, reusable and contestable civic knowledge.

It also explains why computable user needs, civic needs, capabilities and outcome links matter for responsible simulation, AI-assisted analysis and future civic intelligence work.

## Summary

Public institutions cannot make consistently good decisions about services, policy, operations or public outcomes if their understanding of people's needs, civic responsibilities, pain points, evidence, capabilities and value gaps is fragmented or unstable.

Civic design intelligence creates an operational knowledge layer that helps institutions preserve, review, connect and evolve what they know.

The core theory of change is:

> If public institutions can maintain structured, traceable and reviewable knowledge about user needs, civic needs, pain points, evidence, behaviours, capabilities, value gaps and service conditions, then they can make better design, policy, operational and strategic decisions, because decision-makers can see what is known, what is assumed, what is contested, where needs are being erased, where value is blocked and where public outcomes remain unsupported.

## The problem

Public-service knowledge is often spread across:

- research reports
- slide decks
- complaints
- service data
- frontline knowledge
- policy documents
- inspection findings
- design histories
- lived experience
- partner and third-sector evidence
- individual staff memory

This creates recurring problems:

- user needs are captured once and then lost
- civic needs are implicit rather than named
- capability or life needs are separated from operational decisions
- pain points are treated as anecdotal rather than structural
- research findings are flattened into recommendations too early
- evidence strength is unclear
- assumptions look like facts
- decisions become disconnected from the knowledge that informed them
- the same research questions are repeated
- institutional memory disappears when people move roles
- AI, simulations or automation tools may operate over weak, outdated or untraceable knowledge

The result is that institutions may make decisions without knowing whether they are acting on reviewed evidence, weak assumptions, contested claims or outdated understanding.

## Needs erasure

A central failure mode is needs erasure.

Needs erasure happens when a person's real need, civic entitlement, capability requirement or life condition is lost, flattened, mistranslated or made invisible as work moves through institutional processes.

Examples include:

- reducing a life or capability need to a narrow service transaction
- treating a civic need as a preference or complaint
- converting a need into a solution requirement too early
- recording a pain point without preserving the underlying need it blocks
- designing around organisational categories rather than people's lives
- optimising a process while ignoring the outcome it is meant to support
- using AI or simulation against data that does not represent the needs that matter

The repository should help prevent needs erasure by keeping user needs, civic needs, experience needs, service needs, capability links and outcome relationships visible across the knowledge base.

This connects the theory of change to the Lives to be Lived framing: public services should be assessed by whether they help people live lives with dignity, agency, safety, belonging and realistic possibility, not only by whether transactions complete or processes appear efficient.

## Intended change

The repository should help public institutions move from fragmented research material to a shared civic knowledge base.

The intended change is:

> Public-service teams can make better decisions because they have a clearer, more traceable and more current understanding of needs, pain, evidence, capabilities, value and outcomes.

This does not mean every decision will be perfect. It means the knowledge basis for decisions becomes more visible, challengeable and improvable.

## Inputs

The system can use inputs such as:

- anonymised research evidence
- interviews, observations and quotes
- public or partner contributions
- frontline professional knowledge
- service data and operational signals
- complaints, appeals and case reviews
- inspection, Ombudsman and regulatory findings
- academic and sector research
- policy, statutory guidance and local procedures
- previous design histories and decision records
- LLM-assisted synthesis, where clearly labelled and reviewed

Inputs do not automatically become validated knowledge. They must be captured, linked, reviewed and interpreted with appropriate status metadata.

## Activities

The repository supports the following activities:

1. Capture anonymised evidence and source material.
2. Separate evidence from interpretation.
3. Code evidence into structured knowledge objects.
4. Create and maintain user needs, civic needs, behaviours, pain points, insights, themes, value dimensions and capability links.
5. Link objects to evidence, maturity, lifecycle state and review status.
6. Link lower-level needs to higher-level experience, civic and capability needs where useful.
7. Preserve links between needs, capabilities, service conditions and intended outcomes.
8. Record material changes in object change logs.
9. Preserve assumptions and uncertainty rather than hiding them.
10. Link knowledge objects to decisions, service changes, design histories, policy questions or simulation assumptions.
11. Use LLMs carefully to support structuring and synthesis, without treating them as evidence or allowing them to validate claims.
12. Keep immature or unclear material in an inbox rather than forcing premature structure.

## Outputs

The immediate outputs are:

- structured evidence notes
- persistent user needs
- persistent civic needs
- capability or life-need links
- pain point objects
- behaviour objects
- insight objects
- value dimensions
- themes
- object change logs
- review states
- maturity states
- links between evidence, needs, capabilities, pain, value and decisions
- links between needs and outcomes
- dashboards or views that show coverage, gaps and unresolved issues

These outputs are not the final value. They are the infrastructure that allows better judgement, decision-making, simulation and institutional learning.

## Computable needs and simulation readiness

Future civic AI and simulation work needs more than data. It needs a structured account of what matters.

A simulation that does not include user needs, civic needs, capabilities, service constraints and outcome relationships may optimise for the wrong variables.

For example, a simulation may show that a process is faster, cheaper or more efficient while missing that it has:

- erased a user's need for agency
- weakened a civic need for redressability
- reduced a person's ability to understand their realistic options
- shifted burden onto families or frontline professionals
- improved a local metric while worsening a life outcome

Computable needs do not mean reducing human need to simplistic scores. They mean making needs structured enough that they can be linked, queried, compared, tested and used as constraints in analysis.

Minimum useful computable relationships include:

```yaml
need_level:
parent_needs:
child_needs:
related_capabilities:
related_civic_needs:
related_rights:
related_outcomes:
related_pain_points:
related_value_dimensions:
evidence_basis:
review_status:
lifecycle_state:
```

These relationships make it possible to ask questions such as:

- Which outcomes depend on this need being met?
- Which capabilities are weakened if this pain point remains unresolved?
- Which civic needs are unsupported by current service capabilities?
- Which solution options address task needs but fail to support higher-level life or civic needs?
- Which assumptions would a simulation need to include before its output could be trusted?
- Where is needs erasure likely to occur as evidence moves into policy, design or delivery?

This is why the repository treats needs as first-class objects rather than prose fragments inside reports.

## Short-term outcomes

In the short term, the repository should help teams:

- find relevant evidence more easily
- see what is known, assumed, contested or missing
- avoid duplicating research unnecessarily
- preserve meaning when research is broken into objects
- distinguish user needs from civic needs
- connect service needs to capability and life needs
- treat pain points as ongoing conditions or risks
- identify where evidence is weak
- identify where services are failing to deliver value
- explain why a decision is being made
- challenge solution-led or politically preferred decisions with evidence
- reduce the risk of needs erasure
- use AI more safely by grounding synthesis in traceable material

## Medium-term outcomes

Over time, the repository should help institutions:

- maintain institutional memory
- make research reusable across teams and decisions
- connect operational pain to public outcomes
- identify recurring value gaps
- prioritise work based on evidence and civic need
- understand when local context materially changes interpretation
- expose assumptions and uncertainties earlier
- support open design histories and decision records
- make public-service knowledge more inspectable and contestable
- integrate public, professional and third-sector contributions safely
- develop simulation-ready knowledge without prematurely reducing complex human needs to metrics

## Long-term outcomes

In the long term, civic design intelligence should contribute to:

- better public-service decisions
- more accountable use of evidence
- reduced harm, burden and exclusion
- stronger connection between lived experience and institutional action
- better alignment between services, policy, operations and public outcomes
- more responsible use of AI and simulation in public-service contexts
- improved public trust through inspectable reasoning
- a reusable model for civic knowledge infrastructure across public services
- reduced needs erasure in institutional decision-making

## Impact

The intended impact is not only better documentation.

The intended impact is that public institutions become better able to understand, preserve, challenge and act on what is known about people's needs, civic responsibilities, capabilities and public outcomes.

The repository should help institutions move from episodic research and fragmented insight to continuous civic learning.

## Core causal chain

The MVP causal chain is:

1. Evidence is captured safely and separately from interpretation.
2. Evidence is linked to structured knowledge objects.
3. Knowledge objects make needs, pain points, behaviours, value gaps, civic responsibilities and capability implications visible.
4. Need hierarchy links prevent lower-level service or content needs from erasing higher-level life, capability or civic needs.
5. Review and maturity states make the strength of knowledge clearer.
6. Change logs preserve how understanding evolves.
7. Decision-makers can use the knowledge base to understand what is known, uncertain, contested or unresolved.
8. Simulations, AI-assisted analysis and solution assessments can use structured needs and capability links as constraints rather than relying only on service data or process metrics.
9. Decisions become better grounded in evidence and public value.
10. Outcomes and new evidence feed back into the repository.
11. The institution learns over time.

## Assumptions

This theory of change depends on several assumptions:

- Teams will use the repository as part of real decision-making, not only as a documentation archive.
- Knowledge objects will be maintained with enough discipline to remain trustworthy.
- Review states will be used conservatively.
- Evidence will be captured safely and ethically.
- People will not overclaim confidence, validation or certainty.
- The repository will remain lightweight enough to use in practice.
- Public and partner contributions will be triaged before affecting canonical knowledge.
- LLMs will support structuring and synthesis without replacing human review.
- Decision-makers will be willing to consider evidence that challenges preferred solutions.
- Computable needs will be treated as structured civic knowledge, not as simplistic quantification of human life.

## Risks

Key risks include:

- the repository becomes too heavy to maintain
- objects are created without enough evidence
- immature knowledge is treated as validated
- semantic meaning is changed without adequate review
- LLM-generated synthesis is over-trusted
- public contributions are flattened, ignored or mishandled
- sensitive material is exposed
- decision-makers use the repository performatively rather than substantively
- the system becomes a documentation exercise rather than a decision-support capability
- computable needs are over-reduced into metrics that erase meaning
- simulations optimise for what is measurable rather than what matters

## Mitigations

The MVP should reduce these risks by:

- keeping the schema lightweight
- separating evidence from interpretation
- using conservative status values
- preserving assumptions and uncertainty
- using object change logs only when meaning changes
- relying on Git for routine edit history
- using LLM intervention logs for material semantic LLM changes
- keeping unclear material in the inbox
- avoiding premature validation
- linking knowledge objects to decisions and value where useful
- preserving need hierarchy links where they affect interpretation or outcomes
- treating capability and outcome links as meaning-preserving infrastructure rather than bureaucracy
- reviewing the model through real SEND pathway-planning use

## MVP success indicators

The MVP is working if teams can answer questions such as:

- What user needs have we identified?
- What civic needs are implicated?
- What capability or life needs are connected?
- What evidence supports each need?
- Which pain points are active, unresolved, recurring or resolved?
- Where is evidence weak or contested?
- Which service areas are affected?
- Where is value blocked?
- What assumptions are we relying on?
- What has changed in our understanding?
- Which decisions have used this knowledge?
- Which outcomes are unsupported by current service responses?
- Where might needs erasure be happening?
- What would a simulation need to include before its output could be trusted?
- What still needs research, review or validation?

The MVP is not working if the repository only stores documents without improving traceability, judgement, prioritisation, simulation readiness or decision-making.

## Boundary of the MVP

The MVP should not attempt to build a full civic AI system, public contribution platform, automated decision system, simulation platform or complete institutional knowledge graph.

The MVP should focus on the smallest useful loop:

> capture evidence -> structure knowledge -> link meaning -> support decisions -> record change -> learn from new evidence

## Relationship to the broader vision

The broader vision is a civic learning infrastructure that supports open government, public contestability, responsible AI, simulation readiness and institutional transformation.

The MVP does not need to realise that full vision immediately.

It should preserve the architecture needed for that future by creating stable, traceable and reviewable knowledge objects now.
