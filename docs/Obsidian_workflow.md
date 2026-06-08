# Obsidian workflow

This repository can be used as an Obsidian vault for day-to-day research analysis and synthesis.

Obsidian is the working environment. GitHub is the audit trail.

## Workflow overview

```text
capture evidence -> create candidate analysis objects -> link evidence -> review -> validate -> publish outputs
```

The repository should support fast-moving research breakdown without losing rigour.

The operating principle is:

```text
fast creation, slow validation
```

This means many candidate or placeholder analysis objects may be created quickly, especially with LLM support. They do not all need immediate review. The important thing is that their status, evidence strength, review state and history are visible.

## Daily workflow

1. Open the repository as an Obsidian vault.
2. Review the dashboard notes or Dataview queries.
3. Capture new anonymised evidence in `002_Evidence/`.
4. Link evidence to a research study.
5. Use manual analysis or LLM support to create candidate user needs, behaviours, pain points, insights, themes or opportunities.
6. Link evidence to the analysis objects where possible.
7. Mark new synthesis as placeholder, candidate, draft or assumption as appropriate.
8. Review and promote only when evidence supports it.
9. Commit changes to GitHub through a branch or pull request.

## Capture evidence

Create one evidence note for each meaningful quote, observation, survey result or data point.

Evidence should remain close to the source. Do not over-interpret in the evidence note.

Use links to connect evidence to:

- source study
- actor
- journey stage
- user needs
- behaviours
- pain points
- insights
- themes
- opportunities

## Create analysis objects

Analysis objects are interpreted research objects created from evidence, researcher judgement and synthesis.

They include:

- user needs
- behaviours
- pain points
- insights
- themes
- journeys
- personas
- opportunities

These objects may be created manually or with LLM support.

When breaking down research quickly, it is acceptable to create placeholders or candidates that are not yet fully reviewed.

Use:

```yaml
status: assumption | draft
analysis_state: placeholder | candidate | drafted | evidence_linked
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed | needs_review
```

## Code evidence

Coding means identifying what the evidence suggests about:

- what people need
- what people do
- where they experience friction or burden
- what patterns are emerging
- what opportunities might exist
- what might require further research

Coding can be uncertain. If a code is plausible but not yet well-supported, mark it as an assumption or candidate.

## Incremental updates

Analysis objects are allowed to evolve.

Use minor changes for wording, formatting, metadata or link corrections that do not change meaning.

Use material changes when the interpretation, actor, scope, evidence base, confidence, status or evidence strength changes.

Use major changes when an item is split, merged, substantially reframed, replaced, deprecated or affects validated/published outputs.

Every material or major change should have an entry-level changelog.

Example:

```markdown
## Changelog

- 2026-06-08: Reframed from a general information need to a parent decision-support need after linking [[EVID_014]]. Status remains draft.
- 2026-06-09: Split into [[UN_024]] and [[UN_025]] because new evidence separated emotional readiness from pathway information.
```

## Draft insights

An insight should explain a pattern, not merely repeat evidence.

Draft insight structure:

```markdown
# Insight title

## Claim

## Evidence base

## Interpretation

## What we are confident about

## What remains uncertain

## Implications

## Related user needs, behaviours and pain points

## Changelog
```

## Review queues

Use Dataview queries to create review dashboards.

### Candidate analysis objects

```dataview
TABLE type, analysis_state, status, evidence_strength, confidence, review_status
FROM ""
WHERE analysis_state = "placeholder" OR analysis_state = "candidate"
SORT file.mtime DESC
```

### Draft or assumption-based analysis objects

```dataview
TABLE type, analysis_state, evidence_strength, confidence, review_status
FROM ""
WHERE status = "draft" OR status = "assumption"
SORT file.mtime DESC
```

### Weak evidence

```dataview
TABLE type, actor, journey_stage, confidence
FROM ""
WHERE evidence_strength = "weak" OR evidence_strength = "none"
SORT file.mtime DESC
```

### Evidence without source study

```dataview
TABLE actor, evidence_kind, confidence, status
FROM "002_Evidence"
WHERE !source_study
SORT file.mtime DESC
```

### User needs without evidence

```dataview
TABLE actor, journey_stage, status, analysis_state, evidence_strength
FROM "003_User_needs"
WHERE !related_evidence OR length(related_evidence) = 0
SORT file.mtime DESC
```

### Behaviours without evidence

```dataview
TABLE actor, journey_stage, status, analysis_state, evidence_strength
FROM "004_Behaviours"
WHERE !related_evidence OR length(related_evidence) = 0
SORT file.mtime DESC
```

### Pain points without evidence

```dataview
TABLE actor, journey_stage, status, analysis_state, evidence_strength
FROM "005_Pain_point"
WHERE !related_evidence OR length(related_evidence) = 0
SORT file.mtime DESC
```

### LLM-generated notes needing review

```dataview
TABLE type, analysis_state, status, evidence_strength, confidence
FROM ""
WHERE llm_generated = true AND human_reviewed = false
SORT file.mtime DESC
```

### Material or major changes needing review

```dataview
TABLE type, status, analysis_state, review_status
FROM ""
WHERE change_level = "material" OR change_level = "major"
SORT file.mtime DESC
```

### Validated insights

```dataview
TABLE actor, journey_stage, evidence_strength, confidence
FROM "006_Insights"
WHERE status = "validated"
SORT file.name ASC
```

## Backlinks and graph use

Use backlinks to see what depends on a piece of evidence or an analysis object.

Before changing, splitting, merging or deprecating a note, check backlinks to understand downstream impact.

## Suggested dashboard notes

Create a `Dashboards/` folder if useful.

Suggested dashboards:

```text
Dashboards/Candidate analysis objects.md
Dashboards/Assumptions.md
Dashboards/Draft insights.md
Dashboards/Evidence gaps.md
Dashboards/Validated SEND insights.md
Dashboards/LLM review queue.md
Dashboards/Material changes.md
```

## Working with branches

Use Obsidian for editing, but commit through GitHub or Git.

Recommended branch workflow:

1. Create a branch for the work.
2. Make a focused set of changes.
3. Review changed files before committing.
4. Open a pull request.
5. Record risks and review needs in the PR body.
6. Merge only after review.

## What to avoid

Avoid:

- committing raw transcripts
- committing temporary Obsidian workspace noise unless intentional
- adding untitled notes
- using inconsistent IDs
- treating LLM output as evidence
- changing validated notes without checking backlinks and changelogs
- hiding candidate or assumption status from analysis objects
