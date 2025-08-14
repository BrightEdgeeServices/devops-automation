feature

## Overview

- Date: 2025-08-14 17:11 (local)
- Branch: `hendrik/bee-25-new-py-temp-pub-pvt_no_docker-defyaml-github-action`
- Compared to: `master`

## Summary of Changes

- Improved release notes automation in `.github/workflows/01-amend-release-notes.yaml`:
  - When prepending the amendment to `ReleaseNotes.md`, the workflow now ignores the first line of `ReleaseAmendment.md` (used for semantic version selection).
  - After successfully appending the amendment, the workflow resets `ReleaseAmendment.md` to a two-line template prompting authors to add a snippet and start with `bug`, `feature` or `hotfix`.
  - The commit step now includes both `ReleaseNotes.md` and `ReleaseAmendment.md` (along with `pyproject.toml` when version is bumped), ensuring all related changes are pushed together.

## Notes / Impact

- This change streamlines the release process by separating the classification hint from the actual notes added to `ReleaseNotes.md`.
- Teams can keep using the first line in `ReleaseAmendment.md` to drive semantic version bumps via Poetry.
- No consumer code changes are required; workflows will pick up the new behavior automatically in repositories that reuse this action.
