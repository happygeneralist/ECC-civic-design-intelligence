# Changelog

This changelog records repository-level changes.

Use entry-level changelogs inside individual notes for changes to specific evidence, needs, behaviours, pain points, insights or review notes.

## 2026-06-09

### Added

- Added `docs/index.html` as a GOV.UK-style GitHub Pages overview for the civic design intelligence system.
- Added `scripts/build-stats.mjs` to generate repository object counts from numbered markdown object folders and available frontmatter.
- Added `.github/workflows/build-pages-stats.yml` to rebuild `docs/stats.json` on pushes to `main` and on manual workflow dispatch.
- Added `docs/Safe_research_ingestion_MVP.md` to define the minimum conventions for breaking a small SEND pathway-planning research sample into structured objects.
- Added `docs/Object_change_logs.md` to define when object-level changelog entries are required and when Git and pull request summaries are enough.
- Added `Templates/Civic_need_template.md` so civic needs can be created as first-class analysis objects during the MVP.

### Changed

- Updated `README.md` to reference civic needs, the safe-ingestion MVP and the object changelog convention.
- Updated `CONTRIBUTING.md` to clarify safe ingestion, civic needs and object-level changelog rules.

### Notes

- This includes an administrative platform change for stakeholder visibility through GitHub Pages and generated repository statistics.
- Generated stats count missing metadata explicitly and do not infer review, validation, lifecycle state or evidence strength.
- No existing research objects were migrated or semantically changed.
- No existing object was promoted, validated, deprecated or marked as reviewed.
- Object-level changelog entries were not added because the change does not alter the interpretation of existing research objects.

## 2026-06-08

### Added

- Added repository documentation entry point in `README.md`.
- Added repository schema in `SCHEMA.md`.
- Added LLM operating rules in `llm-instructions.md`.
- Added practical governance rules in `GOVERNANCE.md`.
- Added contribution workflow in `CONTRIBUTING.md`.
- Added global changelog.
- Added supporting documentation for review process, Obsidian workflow, evidence standards and LLM safety model.

### Notes

- This is a documentation-only change.
- Existing research notes, evidence notes, insights and templates have not been migrated to the new schema yet.
- A follow-up migration should normalise IDs, statuses, evidence strength and review metadata across existing notes.
