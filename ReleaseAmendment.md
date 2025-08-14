feature

# Release Amendment for 2.0.1

## Overview

- Date: 2025-08-14 02:32 (local)
- Branch: `hendrik/bee-25-new-py-temp-pub-pvt_no_docker-defyaml-github-action`
- Compared to: `master`

This document summarizes the differences between the current branch and `master` for the 2.0.1 release.

## Pipeline Refactor

- Refactored publish-after-merge pipeline into modular reusable workflows:
  - Introduced separate workflows for Build, Release, and Notify.
    - New: `.github/workflows/py-pc-build-def.yaml` (installs deps with Poetry and builds artifacts)
    - New: `.github/workflows/py-pc-release-def.yaml` (creates GitHub Release; derives tag from `pyproject.toml` with optional input)
    - New: `.github/workflows/py-pc-notify-def.yaml` (sends email notification using `betterfor/action-send-mail`)
  - Updated wrapper workflow to orchestrate the three jobs in sequence (Build → Release → Notify):
    - `.github/workflows/py-wf-pub-after_merge-def.yaml` now calls the new modular workflows and forwards required secrets/inputs.
  - Deprecated and removed the combined workflow:
    - Deleted: `.github/workflows/py-pc-rel-build_notify-def.yaml`

## Enhancements and Standardization

- Tag computation: Release workflow now robustly derives tag `v{version}` from `[project].version` or `[tool.poetry].version` in `pyproject.toml`, with optional override via `inputs.tag_name`.
- Python versions: Build/Notify matrices target Python 3.13; Release uses Python 3.12 for tag computation.
- Secrets and permissions normalized across reusable workflows (`GH_REPO_ACCESS_BEE_MASTER`, `GH_REPO_ACCESS_RTE_MASTER`, `RELEASE_EMAIL_USER`, `RELEASE_EMAIL_PASSWORD`).

## CI Workflow Touch-ups (Minor)

- `.github/workflows/01-pre-commit.yaml`
- `.github/workflows/03-publish-new-release.yaml`
- `.github/workflows/py-pc-ci-pub_no_docker-def.yaml`
- `.github/workflows/py-pc-ci-pub_with_docker-def.yaml`
- `.github/workflows/py-pc-ci-pvt_no_docker-def.yaml`
- `.github/workflows/py-pc-ci-pvt_with_docker-def.yaml`
- `.github/workflows/py-pc-pr-def.yaml`
- `.github/workflows/py-pc-precom-def.yaml`

## Configuration Updates

- `pyproject.toml`: Bumped project version to `2.0.1`; maintained project metadata and dev tooling groups.
- `.pre-commit-config.yaml`: Minor adjustment to align with repo standards.

## Change Statistics (vs master)

- 13 files changed, 132 insertions, 222 deletions
- Key file movements:
  - Deleted: `.github/workflows/py-pc-rel-build_notify-def.yaml`
  - Added: `.github/workflows/py-pc-release-def.yaml`

## Notes / Impact

- Repositories consuming the publish-after-merge template should switch to the updated wrapper (`py-wf-pub-after_merge-def.yaml`), which now uses the three modular workflows on `master` of this repo.
- Ensure required secrets (`GH_REPO_ACCESS_BEE_MASTER`, `GH_REPO_ACCESS_RTE_MASTER`, `RELEASE_EMAIL_USER`, `RELEASE_EMAIL_PASSWORD`) are configured in consuming repositories.
- Release notes for the GitHub Release are still read from `ReleaseNotes.md`; this amendment documents the delta vs `master` for `2.0.1`.
