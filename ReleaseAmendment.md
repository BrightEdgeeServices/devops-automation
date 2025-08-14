feature

## Overview

- Date: 2025-08-15 00:29 (local)

## Summary of Changes

- Release pipeline hardening in `.github/workflows/00-new-release-pipeline.yaml`:
  - Push trigger now ignores `pr` tags to avoid unintended pipeline runs on temporary PR tags.
- Release notes amendment workflow polish in `.github/workflows/01-amend-release-notes.yaml`:
  - Standardized release header formatting to use "# Release {version}" with a space for consistent Markdown rendering.
- Version bumped in `pyproject.toml` from 2.3.0 to 2.4.0 to reflect the new release.
- Documentation updated in `ReleaseNotes.md` to capture these changes.
- Removed an unused placeholder file (`dummy.txt`).

## Notes / Impact

- Reduces accidental pipeline executions from PR-related tags and improves readability of generated release notes.
- No changes required for downstream consumers; repositories reusing these workflows will inherit the improvements automatically.
