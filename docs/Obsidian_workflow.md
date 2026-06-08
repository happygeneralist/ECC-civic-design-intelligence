# Obsidian workflow

This repository can be used as an Obsidian vault for day-to-day research analysis and synthesis.

Obsidian is the working environment. GitHub is the audit trail.

## Workflow overview

```text
capture evidence -> code evidence -> draft synthesis -> review -> validate -> publish outputs
```

## Daily workflow

1. Open the repository as an Obsidian vault.
2. Review the dashboard notes or Dataview queries.
3. Capture new anonymised evidence in `002_Evidence/`.
4. Link evidence to a research study.
5. Code evidence into needs, behaviours, pain points or themes.
6. Draft insights from linked evidence.
7. Mark new synthesis as draft or assumption.
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

## Code evidence

Coding means identifying what the evidence suggests about:

- what people need
- what people do
- where they experience friction or burden
- what patterns are emerging
- what might require further research

Coding can be uncertain. If a code is plausible but not yet well-supported, mark it as an assumption.

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

## Related user needs

## Changelog
```

## Review queues

Use Dataview queries to create review dashboards.

### Draft insights

```dataview
TABLE status, evidence_strength, confidence, review_status
FROM "006_Insights"
WHERE status = "draft" OR status = "assumption"
SORT file.mtime DESC
```

### Assumptions

```dataview
TABLE type, actor, journey_stage, evidence_strength, review_status
FROM ""
WHERE status = "assumption"
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
TABLE actor, journey_stage, status, evidence_strength
FROM "003_User_needs"
WHERE !related_evidence OR length(related_evidence) = 0
SORT file.mtime DESC
```

### LLM-generated notes needing review

```dataview
TABLE type, status, evidence_strength, confidence
FROM ""
WHERE llm_generated = true AND human_reviewed = false
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

Use backlinks to see what depends on a piece of evidence or an insight.

Before changing or deprecating a note, check backlinks to understand downstream impact.

## Suggested dashboard notes

Create a `Dashboards/` folder if useful.

Suggested dashboards:

```text
Dashboards/Assumptions.md
Dashboards/Draft insights.md
Dashboards/Evidence gaps.md
Dashboards/Validated SEND insights.md
Dashboards/LLM review queue.md
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
