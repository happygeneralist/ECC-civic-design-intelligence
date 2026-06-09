# Evidence standards

This file defines what counts as evidence in the repository and how evidence should be handled.

## Principle

Evidence is material that has been captured, observed, measured or sourced. Interpretation of evidence should happen in linked synthesis notes, not be hidden inside evidence records.

The repository is not limited to primary research. Evidence may come from research, lived experience, academic studies, statutory and regulatory reports, complaints, inspections, policy, operational data, professional knowledge and public or partner contributions.

Inputs are evidence sources. User needs, civic needs, pain points, behaviours, risks, insights and opportunities are knowledge objects created from, linked to or challenged by those sources.

## Evidence kinds

Use the `evidence_kind` field to classify evidence.

```yaml
evidence_kind: quote | observation | survey_result | statistic | document_extract | desk_research | professional_judgement | public_contribution | partner_contribution | operational_record
```

## Evidence kind definitions

### Quote

A direct anonymised participant quote.

Quotes should preserve meaning and wording as far as possible. Edit only for anonymisation, clarity of redaction or agreed ethical reasons.

### Observation

A researcher observation from a session, service interaction, workshop or fieldwork context.

Observations should separate what was observed from what the researcher inferred.

### Survey result

A finding from survey data, such as a response pattern, proportion, ranking or coded free-text theme.

Survey results should include sample information where available.

### Statistic

A numeric data point from research, administrative data, public data, literature or analysis.

Statistics require a source, date or method note. Unsupported statistics should be marked as low confidence or assumption until sourced.

### Document extract

A relevant extract from a policy, service document, report, guidance note or operational document.

Document extracts should include source title, date and link or reference where possible.

### Desk research

A finding from secondary research, literature, policy analysis or public sources.

Desk research should be clearly distinguished from primary research with users.

### Professional judgement

A claim or interpretation from a practitioner, professional, stakeholder or subject matter expert.

Professional judgement can be valuable but should not automatically be treated as user evidence.

### Public contribution

A contribution, correction, challenge or account submitted by a member of the public, service user, family member, carer or resident.

Public contributions can reveal missing needs, understated pain points, gaps between official process and lived experience, or evidence that a knowledge object needs to be challenged or refined.

Public contributions should be triaged for relevance, safety, privacy, identifiability and sensitivity before they are linked to canonical knowledge objects.

### Partner contribution

A contribution, correction, challenge or account from a third-sector organisation, advocate, partner agency, community organisation or other external partner.

Partner contributions can provide system-level knowledge, cross-case patterns, advocacy evidence, professional context or challenge to institutional assumptions.

Partner contributions should preserve the contributor's intended meaning while making the evidence basis, scope and limitations explicit.

### Operational record

A relevant operational signal, case pattern, service metric, demand pattern, escalation theme, complaints pattern or frontline record.

Operational records can indicate friction, demand failure, delay, risk, unmet need or implementation failure. They should include source, time period and method notes where possible.

## Evidence source examples

Evidence may come from:

- primary research and lived-experience research
- academic studies and literature reviews
- Ofsted, CQC, Ombudsman and other statutory or regulatory reports
- complaints, appeals, tribunal findings and case reviews
- policy, legislation, statutory guidance and local procedures
- operational data, service metrics and demand data
- frontline practitioner knowledge
- voluntary-sector and advocacy reports
- public, family, carer or resident contributions
- previous service design, discovery and delivery work
- design histories and decision records

A source may support, challenge, refine or supersede a knowledge object. It should not automatically become a validated finding.

## Evidence metadata

Evidence notes should include:

```yaml
type: evidence
id:
source_study:
evidence_kind:
actor:
context:
journey_stage:
date_collected:
method:
sensitivity:
anonymisation_checked:
confidence:
status:
related_needs:
related_behaviours:
related_pain_points:
related_insights:
tags:
```

For external public or partner contributions, add optional metadata where useful:

```yaml
contribution_source: public | partner | professional | third_sector | statutory_report | academic | operational | policy
contribution_state: submitted | triaged | linked | candidate | under_review | accepted | partially_accepted | deferred | not_accepted | sensitive_restricted
contributor_type:
source_title:
source_date:
source_url:
```

Do not introduce these fields casually across the MVP unless they are useful for the worked example. They describe the direction for contribution-aware evidence handling.

## Confidence

Use confidence to record the current reliability judgement for the evidence item.

```yaml
confidence: low | medium | high
```

### Low confidence

Use when:

- the source is unclear
- the evidence is anecdotal or isolated
- the context is incomplete
- the claim is a statistic without a visible source
- the evidence may be ambiguous

### Medium confidence

Use when:

- the source is clear
- the context is mostly clear
- the item is relevant and plausible
- limitations remain

### High confidence

Use when:

- the source is clear
- the context is clear
- anonymisation has been checked
- the item is directly relevant
- limitations are understood

## Evidence strength versus confidence

Evidence strength applies mainly to synthesis objects such as user needs, behaviours, pain points and insights.

Confidence applies to the reliability of an individual evidence item or interpretation.

A single high-confidence quote may still provide only weak evidence for a broad insight.

## Source requirements

Every evidence item should link to a source study or source reference where possible.

If the source is unknown, use:

```yaml
source_study:
confidence: low
status: captured
```

Then add a note explaining what is missing.

Do not invent source studies or references.

## Anonymisation

Before evidence is treated as reviewed, check that it does not include:

- names
- addresses
- contact details
- school names where identifying
- rare or unique combinations of details
- exact dates where unnecessary
- case details that could identify a person

Use:

```yaml
anonymisation_checked: true | false
sensitivity: low | medium | high
```

## Public and partner contribution safety

External contributions may include sensitive, identifiable or legally risky material. Before making a contribution public or linking it to canonical objects, check for:

- names or direct identifiers
- identifiable child, family, school or professional details
- special category data
- safeguarding concerns
- allegations about identifiable people
- legal sensitivity
- consent or permission issues
- rare combinations of details that may identify a person or case

Open by default does not mean publishing unsafe detail. Preserve meaning while reducing unnecessary identifiability.

## What evidence can support

### Can support validated findings

- multiple anonymised quotes with clear source context
- well-documented observations
- survey results with clear method and sample
- sourced statistics
- triangulated desk research
- statutory, regulatory or inspection findings with clear scope and date
- public, partner or professional contributions that have been triaged, contextualised and triangulated

### Usually supports draft or assumption only

- single ambiguous quote
- unsupported statistic
- professional judgement without user evidence
- untriaged public or partner contribution
- LLM-generated summary
- notes with unclear source
- early pattern without review

## LLM-generated material

LLM-generated material is not evidence.

An LLM can summarise evidence, suggest codes or draft interpretations, but the evidence remains the underlying quote, observation, data point or source.

Use LLM-generated content to create:

- draft notes
- assumption notes
- suggested links
- review prompts
- research gaps

Do not use LLM output alone to validate an insight or user need.

## Contradictory evidence

Do not ignore contradictory evidence.

When evidence conflicts, record the tension in the relevant synthesis note.

Useful headings:

```markdown
## Supporting evidence

## Contradictory or limiting evidence

## What remains uncertain
```

## Evidence changelog

Evidence notes should record material changes.

Examples:

```markdown
## Changelog

- 2026-06-08: Created from anonymised quote. Source study linked. Confidence: medium.
- 2026-06-10: Added anonymisation check and linked to [[UN_003]].
```
