# ECC Research Repository

This repository is an Obsidian-compatible research and insights repository for SEND-related service design, policy and decision-support work.

It is intended to help researchers, designers, product/service teams and decision-makers capture anonymised evidence, connect it to user needs, behaviours, pain points, insights, value dimensions and solution assessments, and maintain a clear audit trail for how research knowledge develops over time.

The repository is not only for designing good services. It should also provide the human intelligence needed to challenge weak, harmful or solution-led decisions with a defensible evidence base.

## What this repository is for

Use this repository to store and work with:

- research study summaries
- anonymised evidence, quotes, observations and data points
- user needs
- behaviours
- pain points
- insights
- themes
- personas
- journeys
- value dimensions
- solution options and assessments
- review notes
- synthesis outputs

The repository should support evidence-based service design, reduce duplicated research, make value visible, and make it easier to understand what is known, what is assumed, what is contested, and what still needs validation.

## What this repository is not for

Do not store:

- raw transcripts
- recordings
- identifiable participant data
- special category personal data that has not been anonymised
- unsupported claims presented as validated findings
- LLM-generated synthesis without clear status and review metadata
- politically preferred solution ideas presented as evidence-backed recommendations

## Repository structure

```text
001_Research_studies/   Research activities and study summaries
002_Evidence/           Anonymised quotes, observations and data points
003_User_needs/         User needs and need summaries
004_Behaviours/         Observed or inferred behaviours
005_Pain_point/         Pain points and barriers
006_Insights/           Draft, reviewed and validated insights
007_Themes/             Cross-cutting themes
008_Personas/           Personas or archetypes where appropriate
009_Journeys/           Journey maps and journey-stage analysis
Templates/              Templates for creating structured notes
docs/                   Supporting documentation and governance material
```

## Core principle

Every meaningful claim should be traceable to evidence, or clearly marked as an assumption.

The repository distinguishes between:

- captured evidence
- draft synthesis
- assumptions
- reviewed analysis
- validated findings
- value dimensions
- solution options and recommendations
- deprecated or superseded material

## How to use this repository

1. Capture anonymised evidence in `002_Evidence/`.
2. Link evidence to studies, actors, journey stages and tags.
3. Code evidence into user needs, behaviours and pain points.
4. Draft insights from linked evidence.
5. Connect needs and insights to value dimensions where useful.
6. Assess solution options against needs, value, evidence, risks and assumptions.
7. Review assumptions, evidence basis and confidence.
8. Promote reviewed work to validated status only when the evidence supports it.
9. Record meaningful changes in both entry-level changelogs and the global `CHANGELOG.md`.

## Working with Obsidian

This repository is designed to work as an Obsidian vault. Use links, backlinks, properties and Dataview queries to navigate between evidence, needs, behaviours, insights, value dimensions and solution assessments.

See `docs/Obsidian_workflow.md` for the recommended workflow.

## Working with LLMs

LLMs may be used to help classify, link, summarise and draft research material, but they must not be treated as evidence.

LLMs must not mark anything as validated, upgrade evidence strength, remove caveats or materially change validated research claims without human review.

See `llm-instructions.md` and `docs/LLM_safety_model.md`.

## Key documentation

- `SCHEMA.md` defines object types, required fields and controlled values.
- `GOVERNANCE.md` defines repository governance and review responsibilities.
- `CONTRIBUTING.md` defines how to add and update material safely.
- `CHANGELOG.md` records repository-level changes.
- `docs/Evidence_standards.md` defines what counts as evidence.
- `docs/Review_process.md` defines review and validation steps.
- `docs/Value_and_decision_evidence.md` defines how value, solution assessment and decision evidence are handled.
