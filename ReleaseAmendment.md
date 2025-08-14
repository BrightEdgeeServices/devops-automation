feature

## Overview

- Date: 2025-08-14 16:31 (local)
- Branch: `hendrik/bee-25-new-py-temp-pub-pvt_no_docker-defyaml-github-action`
- Compared to: `master`

## Summary of Changes

- Refactored and modularized the publish-after-merge pipeline into reusable workflows:
  - Added `.github/workflows/py-pc-build-def.yaml` (builds with Poetry)
  - Added `.github/workflows/py-pc-release-def.yaml` (derives tag from `pyproject.toml` and creates GitHub Release)
  - Added `.github/workflows/py-pc-notify-def.yaml` (sends release notification email)
  - Updated wrapper `.github/workflows/py-wf-pub-after_merge-def.yaml` to orchestrate Build → Release → Notify
- Introduced new end-to-end New Release Pipeline wrapper with gated stages:
  - `.github/workflows/00-new-release-pipeline.yaml` now detects `pr` tag, amends release notes, merges, publishes, sends notice, and cleans up tag
  - Uses reusable actions: `py-pc-pr-detect_tag-def.yaml` and `py-pc-pr-cleanup_tag-def.yaml`
- Split and standardized pre-commit workflow naming:
  - Renamed `01-pre-commit.yaml` to `02-pre-commit.yaml` and wired into the new pipeline
- Added supporting wrappers for merge, publish, and notify:
  - `.github/workflows/03-merge.yaml`, `.github/workflows/04-publish-release.yaml`, `.github/workflows/05-send-notice.yaml`
- Replaced legacy combined workflow with modular equivalents:
  - Replaced `.github/workflows/py-pc-rel-build_notify-def.yaml` with `.github/workflows/py-pc-notify-def.yaml`
- Updated PR pipeline to consume reusable PR tag detection and cleanup actions
  - `.github/workflows/py-wf-pr-pvt_no_docker-def.yaml`
- Updated Release notes automation to compute semantic version bump and prepend notes
  - `.github/workflows/01-amend-release-notes.yaml`
- Bumped project metadata and release notes
  - `pyproject.toml`, `ReleaseNotes.md`

## Notes / Impact

- Consumers should switch to the new modular publish-after-merge pattern via `.github/workflows/py-wf-pub-after_merge-def.yaml`.
- Ensure repository secrets are configured: `GH_REPO_ACCESS_BEE_MASTER`, `GH_REPO_ACCESS_RTE_MASTER`, `RELEASE_EMAIL_USER`, `RELEASE_EMAIL_PASSWORD`.
- The first line of this file is intentionally the release classification for automation and will be skipped when appending to ReleaseNotes.md.
