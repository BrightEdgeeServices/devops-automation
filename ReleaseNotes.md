# Release 2.5.5

The first line must be *bug*, *feature* or *hotfix*

______________________________________________________________________

# Release 2.5.4

## Overview

- Date: 2025-09-02 02:18 (local)
- Branch: `hendrik/bee-25-new-py-temp-pub-pvt_no_docker-defyaml-github-action`
- Compared to: `master`

## Summary of Changes

- Hotfix: Clean up/remove temporary `pr` tag in workflows to prevent unintended retriggers and ensure clean pipeline
  runs.
- Pipeline: Keep push trigger ignoring `pr` tags in `.github/workflows/00-new-release-pipeline.yaml` for safer releases.
- Docs: Tidied amendment template for release notes.

## Change Statistics (vs master)

- 24 files changed, 830 insertions, 38 deletions

______________________________________________________________________

# Release 2.5.3

This is a bug test

______________________________________________________________________

# Release 2.5.2

This is a bug test

______________________________________________________________________

# Release 2.5.1

This is a bug test

______________________________________________________________________

# Release 2.5.0

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

______________________________________________________________________

# Release 2.4.0

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

______________________________________________________________________

# Release 2.3.0

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

______________________________________________________________________

# Release 2.2.0

- Experimented with automation

______________________________________________________________________

#Release 2.1.0

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

______________________________________________________________________

# Release 2.0.0

______________________________________________________________________

# Release 1.4.2

# New Actions

- `py-temp-pub-pvt_no_docker-def.yaml`
  - Publish packages for use by other packages.
- `py-wf-pub-pvt_no_docker-def.yaml`
  - Used by `py-temp-pub-pvt_no_docker-def.yaml`
  - Describe the workflow
- `py-pc-pub-no_docker-def.yaml`
  - Used by `py-pc-pub-no_docker-def.yaml`
  - Describe th process

# Updated Actions

- `py-pc-ci-pvt_with_docker-def.yaml`
  - Update "Configure Poetry" step.
  - Fixed "Configure Poetry" step.
  - Add creation of `logs` directory
- `py-pc-ci-pvt_no_docker-def`
  - Add creation of `logs` directory
- `py-pc-dep-with_docker-def.yaml`
  - Add `RELEASE_EMAIL_PASSWORD` and `RELEASE_EMAIL_USER` environment variables.
- `py-wf-dep-pvt_with_docker-def.yaml`
  - Add `RELEASE_EMAIL_PASSWORD` and `RELEASE_EMAIL_USER` environment variables.
  - Add `INSTALLER_USER_ID`, `INSTALLER_USER_PWD`, `MYSQL_DATABASE`, `MYSQL_HOST`, `MYSQL_PASSWORD`, `MYSQL_ROOT_PASSWORD`, `MYSQL_TCP_PORT`, `MYSQL_USER`, `PROJECT_NAME`
- `py-temp-dep-pvt_no_docker-def.yaml`
  - Rename job `python-template-deploy-private-no-docker` to `py-temp-dep-pvt_no_docker-def`
- `py-temp-dep-pvt_with_docker-def.yaml`
  - Rename job `python-template-deploy-private-with-docker` to `py-temp-dep-pvt_with_docker-def`
  - Add `RELEASE_EMAIL_PASSWORD` and `RELEASE_EMAIL_USER` environment variables.
- `py-temp-fork-pvt_merge_no_docker-def.yaml`
  - Rename job `python-template-merge-with-local-fork` to `py-temp-fork-pvt_merge_no_docker-def`
- `py-temp-fork-pvt_merge_no_docker-def.yaml`
  - Rename job `python-template-fork-merge-with-docker` to `py-temp-fork-pvt_merge_no_docker-def`
- `py-temp-fork-scheduled_sync_with_upstream-def.yaml`
  - Rename `scheduled-fork-update-pull-template` to `py-temp-fork-scheduled_sync_with_upstream-def`
- `py-temp-pypi-pub_no_docker-def.yaml`
  - Rename job `python-template-pypi-public-no-docker` to `py-temp-pypi-pub_no_docker-def`
- `py-temp-pypi-pub_with_docker-def.yaml`
  - Rename job `python-template-pypi-public-with-docker` to `py-temp-pypi-pub_with_docker-def`

______________________________________________________________________

# Release 1.4.1

- Add PYPI_API_TOKEN_PROD in py-wf-pypi-pub_with_docker-def.yaml

______________________________________________________________________

# Release 1.4.0

- Removed the .github/ISSUE_TEMPLATE directory.
  This will force the repository to use the
  BrightEdgeeServices/.github/ISSUE_TEMPLATE directory, centralizing the maintenance of templates.
- Add workflow to automate the update of forked repositories:
  - py-pc-fork-merge-def.yaml
  - py-pc-fork-sync_with_upstream-def.yaml
  - py-wf-fork-merge_no_docker-def.yaml
  - py-wf-fork-merge_with_docker-def.yaml
  - py-wf-fork-scheduled_sync_with_upstream-def.yaml
  - py-temp-fork-pvt_merge_no_docker-def.yaml
  - py-temp-fork-pvt_merge_with_docker-def.yaml
  - py-temp-fork-scheduled_sync_with_upstream-def.yaml

______________________________________________________________________

# Release 1.3.0

- Update py-pc-ci-pub_no_docker-def.yaml with Poetry configuration for private repositories
- Update SetupGitHubAccess to auto create new branches.

______________________________________________________________________

# Release 1.2.2

- Update py-wf-pypi-pub_no_docker-def.yaml with PYPI_API_TOKEN_PROD secret variable
- Update py-pc-pypi-default.yaml with BEE and RTE master token variables
- Add py-pc-pypi-default.yaml Poetry config secrets
- Add py-pc-ci-pub_no_docker-def.yaml Poetry config secrets

______________________________________________________________________

# Release 1.2.1

- Fix and remove Docker sections from py-pc-ci-pvt_no_docker-def
- Configure secrets variables so that it is inherited/transferred between the reusable workflows.

______________________________________________________________________

# Release 1.2.0

- Update the secrets' references.
- Add the ISSUE_TEMPLATEs

______________________________________________________________________

# Release 1.1.0

- Update badges.
- Change the name of 00-deployment-pipeline.yaml to Production Pipeline
- Remove version reference from target custom workflows
- Add a pub_custom_ci workflow
  - py-temp-pypi-pub_custom_ci-def.yaml
  - py-wf-pypi-pub_custom_ci-def.yaml.yaml

______________________________________________________________________

# Release 1.0.0

- Rename all workflow scripts to shorten the names.
- Update workflow scripts
- Format workflow scripts
- Install automation scripts

______________________________________________________________________

# Release 0.2.0

- Implement reusable GitHub workflows.
- templates:
  - python-template-deploy.yaml
  - python-template-pypi.yaml

______________________________________________________________________

# Release 0.1.0

- No Release Notes will be kept according to a group decision.

______________________________________________________________________
