### Release 9.1.0

### Summary of Changes

- Templates: Updated secrets and variables configuration in `templates/py-temp-pr-pub-no_docker-def.yaml` to use repository variables instead of secrets where appropriate, added new configuration variables (INSTALLER_USERID, INSTALLER_PWD, MYSQL_DATABASE, MYSQL_HOST, MYSQL_TCP_PORT, VENV_ENVIRONMENT), and removed PYPI_API_TOKEN_PROD secret.
- Workflows: Removed PYPI_API_TOKEN_PROD secret requirement from `.github/workflows/py-wf-pr-pub-no_docker-def.yaml`.
- Build: Bumped version to 10.0.0 in `pyproject.toml`.

### Change Statistics (vs master)

- Branch: `hendrik/urs-307-main_feature-devops-automation-fork-sync-templates`
- Files changed:
  - .github/workflows/py-wf-pr-pub-no_docker-def.yaml
  - templates/py-temp-pr-pub-no_docker-def.yaml
- Number of files changed: 2
- Insertions: 8
- Deletions: 6

______________________________________________________________________

### Release 9.0.0

### Summary of Changes

- Templates: Updated workflow references in legacy templates to use standardized naming convention with hyphens and "-all" suffixes:
  - `templates/legacy/py-temp-dep-pvt_no_docker-def.yaml`
  - `templates/legacy/py-temp-dep-pvt_with_docker-def.yaml`
  - `templates/legacy/py-temp-pub-pvt_no_docker-def.yaml`
  - `templates/legacy/py-temp-pypi-pub_custom_ci-def.yaml`
- Workflows: Standardized naming convention across workflows by renaming files to use hyphens instead of underscores and adding "-all" suffixes where appropriate. Updated workflow references throughout the codebase to match the new naming convention.
- Workflows: Added new public repository PR workflow `.github/workflows/py-wf-pr-pub-no_docker-def.yaml` for public repositories.
- Documentation: Updated README.md to reflect naming convention changes.
- Build: Bumped version to 9.0.0 in `pyproject.toml`.

### Change Statistics (vs master)

- Branch: `hendrik/urs-307-main_feature-devops-automation-fork-sync-templates`
- Files changed:
  - .github/workflows/00-new-release-pipeline.yaml
  - .github/workflows/all-pc-fork-all-merge-def.yaml
  - .github/workflows/all-pc-fork-pub-sync_with_upstream-def.yaml
  - .github/workflows/all-pc-fork-pvt-sync_with_upstream-def.yaml
  - .github/workflows/all-pc-notify-all-def.yaml
  - .github/workflows/all-pc-pr-all-cleanup_tag-def.yaml
  - .github/workflows/all-pc-pr-all-def.yaml
  - .github/workflows/all-pc-pr-all-detect_tag-def.yaml
  - .github/workflows/all-wf-fork-pub-scheduled_sync_with_upstream-def.yaml
  - .github/workflows/all-wf-fork-pvt-scheduled_sync_with_upstream-def.yaml
  - .github/workflows/iac-wf-fork-pvt-merge_no_docker-def.yaml
  - .github/workflows/legacy/py-temp-fork-pvt_merge_no_docker-def.yaml
  - .github/workflows/legacy/py-temp-fork-pvt_merge_with_docker-def.yaml
  - .github/workflows/legacy/py-wf-dep-pvt_no_docker-def.yaml
  - .github/workflows/legacy/py-wf-dep-pvt_with_docker-def.yaml
  - .github/workflows/legacy/py-wf-fork-merge_with_docker-def.yaml
  - .github/workflows/legacy/py-wf-pub-pvt_no_docker-def.yaml
  - .github/workflows/legacy/py-wf-pypi-pub_no_docker-def.yaml
  - .github/workflows/legacy/py-wf-pypi-pub_with_docker-def.yaml
  - .github/workflows/py-pc-build-all-def.yaml
  - .github/workflows/py-pc-ci-pub-no_docker-def.yaml
  - .github/workflows/py-pc-ci-pub-with_docker-def.yaml
  - .github/workflows/py-pc-ci-pvt-no_docker-def.yaml
  - .github/workflows/py-pc-precom-all-def.yaml
  - .github/workflows/py-pc-release-all-def.yaml
  - .github/workflows/py-wf-fork-pub-merge_no_docker-def.yaml
  - .github/workflows/py-wf-fork-pvt-merge_no_docker-def.yaml
  - .github/workflows/py-wf-pr-pub-no_docker-def.yaml
  - .github/workflows/py-wf-pr-pvt-no_docker-def.yaml
  - .github/workflows/py-wf-pr-pvt_straight_through-def.yaml
  - .github/workflows/py-wf-pr-pvt_with_docker-def.yaml
  - .github/workflows/py-wf-pr-pvt_with_native_docker-def.yaml
  - .github/workflows/py-wf-publish-pvt-build_release_notify_after_merge-def.yaml
  - .github/workflows/py-wf-publish-pvt-release_notify_after_merge-def.yaml
  - .github/workflows/react-pc-ci-pvt-with_docker-def.yaml
  - .github/workflows/react-pc-precom-all-def.yaml
  - .github/workflows/react-pc-release-all-def.yaml
  - .github/workflows/react-wf-pr-pvt-with_docker-def.yaml
  - .github/workflows/react-wf-publish-pvt-release_notify_after_merge-def.yaml
  - README.md
  - templates/all-temp-fork-pub-scheduled_sync_with_upstream-daily.yaml
  - templates/all-temp-fork-pub-scheduled_sync_with_upstream-daily.yaml.yaml
  - templates/all-temp-fork-pub-scheduled_sync_with_upstream-weekly.yaml
  - templates/all-temp-fork-pvt-scheduled_sync_with_upstream-daily.yaml
  - templates/all-temp-fork-pvt-scheduled_sync_with_upstream-monthly.yaml
  - templates/all-temp-fork-pvt-scheduled_sync_with_upstream-weekly.yaml
  - templates/iac-temp-fork-pvt-merge_no_docker-def.yaml
  - templates/legacy/py-temp-dep-pvt_no_docker-def.yaml
  - templates/legacy/py-temp-dep-pvt_with_docker-def.yaml
  - templates/legacy/py-temp-pub-pvt_no_docker-def.yaml
  - templates/legacy/py-temp-pypi-pub_custom_ci-def.yaml
  - templates/py-temp-fork-pub-merge_no_docker-def.yaml
  - templates/py-temp-fork-pvt-merge_no_docker-def.yaml
  - templates/py-temp-pr-pub-no_docker-def.yaml
  - templates/py-temp-pr-pvt-no_docker-def.yaml
  - templates/py-temp-pr-pvt-straight_through-def.yaml
  - templates/py-temp-pr-pvt-with_docker-def.yaml
  - templates/py-temp-pr-pvt-with_native_docker-def.yaml
  - templates/py-temp-pvt-publish-build_release_notify_after_merge-def.yaml.yaml
  - templates/py-temp-pvt-publish-release_notify_after_merge-def.yaml
  - templates/react-temp-pr-pvt-with_docker-def.yaml
  - templates/react-temp-publish-pvt-release_notify_after_merge-def.yaml
- Number of files changed: 62
- Insertions: 382
- Deletions: 331

______________________________________________________________________

### Release 8.0.2

### Summary of Changes

- Workflows: Updated `all-pc-fork-sync_with_upstream-def.yaml` to include authentication token in the upstream remote URL for accessing private repositories. Added logic to automatically select the appropriate token (`GH_REPO_ACCESS_BEE_MASTER` for BrightEdgeeServices or `GH_REPO_ACCESS_RTE_MASTER` for other organizations) based on the original owner.
- Build: Bumped version to 8.0.2 in `pyproject.toml`.

### Change Statistics (vs master)

- Branch: `main_feature-devops-automation-multi-frequency-fork-sync`
- Files changed:
  - .github/workflows/all-pc-fork-sync_with_upstream-def.yaml
- Number of files changed: 1
- Insertions: 11
- Deletions: 3

______________________________________________________________________

### Release 8.0.1

### Summary of Changes

- Workflows: Added validation step to `all-pc-fork-sync_with_upstream-def.yaml` to check for required repository variables (`ORIGINAL_OWNER` and `ORIGINAL_REPO_NAME`) before attempting to sync with upstream. Provides clear error messages with setup instructions if variables are missing.
- Templates: Fixed indentation formatting in `all-temp-fork-scheduled_sync_with_upstream-weekly.yaml`.
- Build: Bumped version to 8.0.1 in `pyproject.toml`.

### Change Statistics (vs master)

- Branch: `main_feature-devops-automation-multi-frequency-fork-sync`
- Files changed:
  - .github/workflows/all-pc-fork-sync_with_upstream-def.yaml
  - templates/all-temp-fork-scheduled_sync_with_upstream-weekly.yaml
- Number of files changed: 2
- Insertions: 15
- Deletions: 3

______________________________________________________________________

### Release 8.0.0

### Summary of Changes

- Templates: Renamed `py-temp-fork-scheduled_sync_with_upstream-def.yaml` to `all-temp-fork-scheduled_sync_with_upstream-daily.yaml` to clearly indicate daily scheduling frequency and make it language-agnostic.
- Templates: Added new weekly scheduled sync template `all-temp-fork-scheduled_sync_with_upstream-weekly.yaml` for repositories that require weekly synchronization with upstream.
- Templates: Added new monthly scheduled sync template `all-temp-fork-scheduled_sync_with_upstream-monthly.yaml` for repositories that require monthly synchronization with upstream.
- Workflows: Renamed `py-wf-fork-scheduled_sync_with_upstream-def.yaml` to `all-wf-fork-scheduled_sync_with_upstream-def.yaml` to make it language-agnostic.
- Workflows: Renamed `py-pc-fork-sync_with_upstream-def.yaml` to `all-pc-fork-sync_with_upstream-def.yaml` to make it language-agnostic.
- Documentation: Updated README.md to document the three new multi-frequency fork sync templates and updated naming convention to include "all" as a language option.
- Build: Bumped version to 8.0.0 in `pyproject.toml`.

### Change Statistics (vs master)

- Branch: `main_feature-devops-automation-multi-frequency-fork-sync`
- Files changed:
  - .github/workflows/all-pc-fork-sync_with_upstream-def.yaml
  - .github/workflows/all-wf-fork-scheduled_sync_with_upstream-def.yaml
  - .github/workflows/legacy/linear-issue.md
  - .github/workflows/legacy/linear-project-description.md
  - .github/workflows/legacy/linear-sub-issue.md
  - .github/workflows/legacy/py-pc-fork-sync_with_upstream-def.yaml
  - .github/workflows/legacy/py-wf-fork-scheduled_sync_with_upstream-def.yaml
  - README.md
  - linear-issue.md
  - templates/all-temp-fork-scheduled_sync_with_upstream-daily.yaml
  - templates/all-temp-fork-scheduled_sync_with_upstream-monthly.yaml
  - templates/all-temp-fork-scheduled_sync_with_upstream-weekly.yaml
- Number of files changed: 12
- Insertions: 555
- Deletions: 160

______________________________________________________________________

### Release 7.1.7

### Summary of Changes

- CI: Improved robustness of the ESLint 9 patching script by switching to a here-doc approach. This resolves `IndentationError` and potential quoting issues in CI environments.
- Build: Bumped version to 7.1.7 in `pyproject.toml`.

______________________________________________________________________

### Release 7.1.6

### Summary of Changes

- CI: Fixed a bug in the ESLint 9 patching script where `ruamel.yaml` was introducing trailing whitespace in `.pre-commit-config.yaml`, causing the `trailing-whitespace` hook to fail in CI. Added a cleanup step to remove trailing whitespace after patching.
- Build: Bumped version to 7.1.6 in `pyproject.toml`.

______________________________________________________________________

### Release 7.1.5

### Summary of Changes

- CI: Fixed a `SyntaxError` in the ESLint 9 patching script caused by incorrect quoting in an f-string within a shell-executed Python command.

______________________________________________________________________

### Release 7.1.4

### Summary of Changes

- CI: Fixed a bug in the ESLint 9 patching script where `typescript-eslint` was not added if `@typescript-eslint/*` packages were already present due to substring matching. Changed to exact dependency name matching.

______________________________________________________________________

### Release 7.1.3

### Summary of Changes

- CI: Improved ESLint 9 support in pre-commit workflows by automatically adding `typescript-eslint` when TypeScript is detected in the environment.
- CI: Enhanced project-level dependency installation to include ALL `additional_dependencies` defined in the ESLint pre-commit hook, ensuring flat configuration files can correctly resolve all imported plugins and configs.
- CI: Optimized patching logic to preserve formatting and indents in `.pre-commit-config.yaml`.

______________________________________________________________________

### Release 7.1.2

### Summary of Changes

- CI: Added `--legacy-peer-deps` to the project-level ESLint dependency installation step in pre-commit workflows to resolve peer dependency conflicts.

______________________________________________________________________

### Release 7.1.1

### Summary of Changes

- CI: Enhanced "Patch Pre-Commit Config for ESLint 9" to use `ruamel.yaml` for preserving formatting and to include `globals` dependency.
- CI: Added project-level installation of ESLint 9 dependencies (`@eslint/js`, `globals`) in pre-commit workflows to resolve module resolution errors in `eslint.config.js`.
- CI: Added `actions/setup-node@v4` to `py-pc-precom-all-def.yaml` to support ESLint 9 dependency installation.
- CI: Added `git add .pre-commit-config.yaml` to pre-commit workflows to stage auto-patched configurations and avoid hook failures.
- Build: Bumped version to 7.1.1 in `pyproject.toml`.

______________________________________________________________________

### Release 7.1.0

### Summary of Changes

- CI: Added standardized GitHub Actions workflows for React projects, including Pre-commit, CI (Docker-based), and Pull Request automation.
- CI: Renamed Python-specific PR workflows to a generic naming convention (`all-pc-pr-*`) to support both Python and React.
- CI: Updated `react-pc-ci-pvt-with_docker-def.yaml` to use `--legacy-peer-deps` for `npm ci` to resolve React 19 peer dependency conflicts.
- CI: Added a "Patch Pre-Commit Config for ESLint 9" step to pre-commit workflows to automatically include `@eslint/js` in `mirrors-eslint` hooks.
- CI: Added Node.js setup to `react-pc-precom-all-def.yaml`.
- Templates: Added a new React PR template `templates/react-temp-pr-pvt-with_docker-def.yaml`.
- Maintenance: Fixed invalid workflow references in `.github/workflows/00-new-release-pipeline.yaml`.
- Build: Bumped version to 7.1.0 in `pyproject.toml`.

### Change Statistics (vs master)

- Branch: `main_feature-devops-automation-Support-React-Workflows`
- Files changed:
  - .github/workflows/00-new-release-pipeline.yaml
  - .github/workflows/all-pc-pr-all-cleanup_tag-def.yaml
  - .github/workflows/all-pc-pr-all-def.yaml
  - .github/workflows/all-pc-pr-all-detect_tag-def.yaml
  - .github/workflows/react-pc-ci-pvt-with_docker-def.yaml
  - .github/workflows/react-pc-precom-all-def.yaml
  - .github/workflows/py-pc-precom-all-def.yaml
  - .github/workflows/react-wf-pr-pvt-with_docker-def.yaml
  - pyproject.toml
  - templates/react-temp-pr-pvt-with_docker-def.yaml

______________________________________________________________________

### Release 7.0.2

### Summary of Changes

- CI: Updated `.github/workflows/py-pc-ci-pvt_with_native_docker-def.yaml` to include hardcoded token references for `rtecommon` and `rtedb` repositories in Poetry configuration.
- Build: Bumped version to 7.0.2 in `pyproject.toml`.

### Change Statistics (vs master)

- Branch: `main_feature-devops-automation-Fix-rtecommon-rtedb-auth-in-CI`
- 2 files changed, 3 insertions, 1 deletion
- Files changed:
  - .github/workflows/py-pc-ci-pvt_with_native_docker-def.yaml
  - pyproject.toml

______________________________________________________________________

### Release 7.0.1

### Summary of Changes

- CI: Introduced native Docker support in CI workflows to accommodate integration tests requiring a live Docker engine.
- CI: Added `.github/workflows/py-pc-ci-pvt_with_native_docker-def.yaml` for private CI jobs using native Docker.
- CI: Added `.github/workflows/py-wf-pr-pvt_with_native_docker-def.yaml` as a reusable PR workflow for native Docker
  environments.
- Templates: Added `templates/py-temp-pr-pvt-with_native_docker-def.yaml` to provide a starting point for repositories
  requiring native Docker CI.
- Maintenance: Updated version references and configuration across multiple workflow scripts for consistency.
- Build: Bumped version to 7.0.1 in `pyproject.toml`.

### Change Statistics (vs master)

- Branch: `hendrik/rte-175-main_feature-devops-automation-fix-native-docker-ci`
- 27 files changed, 374 insertions, 45 deletions
- Files changed:
  - .github/workflows/01-pre-commit.yaml
  - .github/workflows/02-amend-release-notes.yaml
  - .github/workflows/03-merge.yaml
  - .github/workflows/04-publish-release.yaml
  - .github/workflows/05-send-notice.yaml
  - .github/workflows/py-pc-build-all-def.yaml
  - .github/workflows/py-pc-ci-pub-no_docker-def.yaml
  - .github/workflows/py-pc-ci-pub-with_docker-def.yaml
  - .github/workflows/py-pc-ci-pvt-no_docker-def.yaml
  - .github/workflows/py-pc-ci-pvt_with_docker-def.yaml
  - .github/workflows/py-pc-ci-pvt_with_native_docker-def.yaml
  - .github/workflows/py-pc-notify-def.yaml
  - .github/workflows/py-pc-pr-def.yaml
  - .github/workflows/py-pc-precom-all-def.yaml
  - .github/workflows/py-pc-release-def.yaml
  - .github/workflows/py-wf-pr-pvt_with_native_docker-def.yaml
  - .pre-commit-config.yaml
  - poetry.lock
  - pyproject.toml
  - templates/py-temp-pr-pvt-with_native_docker-def.yaml
  - templates/py-temp-pub-build_release_notify_after_merge-def copy.yaml
  - (and 6 hidden IDE configuration files in .github/.idea/)

______________________________________________________________________

# Release 7.0.0

## Summary of Changes

- Build: Bump version to 7.0.0 in project metadata.
- Templates: Add new publish build and release notify template copy in `templates/py-temp-pub-build_release_notify_after_merge-def copy.yaml`.
- Templates: Update publish build and release notify template in `templates/py-temp-pub-build_release_notify_after_merge-def.yaml` to correct version references in notifications.
- Templates: Update publish release notify template in `templates/py-temp-pvt-publish_release_notify_after_merge-def.yaml` to correct version references in notifications.

## Change Statistics (vs master)

- Branch: `hendrik/rte-153-main_feature-devops-automation-straight-through-processing`
- 3 files changed, 25 insertions, 2 deletions
- Files changed:
  - templates/py-temp-pub-build_release_notify_after_merge-def copy.yaml
  - templates/py-temp-pub-build_release_notify_after_merge-def.yaml
  - templates/py-temp-pvt-publish_release_notify_after_merge-def.yaml

______________________________________________________________________

# Release 6.0.0

## Summary of Changes

- Build: Bump version to 6.0.0 in project metadata.
- Templates: Add new publish release notification template in `templates/py-temp-pvt-publish_release_notify_after_merge-def.yaml`.
- Templates: Update PR straight-through template in `templates/py-temp-pr-pvt-straight_through-def.yaml` to align with reusable workflow changes.
- Templates: Update publish build and release notify template in `templates/py-temp-pub-build_release_notify_after_merge-def.yaml` to match renamed workflow.
- CI: Add reusable workflow for release notification after merge in `.github/workflows/py-wf-publish-pvt-release_notify_after_merge-def.yaml`.
- CI: Rename publish after-merge workflow to `.github/workflows/py-wf-publish-pvt-build_release_notify_after_merge-def.yaml` for clarity and consistency.
- CI: Update PR straight-through reusable workflow in `.github/workflows/py-wf-pr-pvt_straight_through-def.yaml`.

## Change Statistics (vs master)

- Branch: `hendrik/rte-153-main_feature-devops-automation-straight-through-processing`
- 6 files changed, 80 insertions, 5 deletions
- Files changed:
  - .github/workflows/py-wf-pr-pvt_straight_through-def.yaml
  - .github/workflows/py-wf-publish-pvt-build_release_notify_after_merge-def.yaml
  - .github/workflows/py-wf-publish-pvt-release_notify_after_merge-def.yaml
  - templates/py-temp-pr-pvt-straight_through-def.yaml
  - templates/py-temp-pub-build_release_notify_after_merge-def.yaml
  - templates/py-temp-pvt-publish_release_notify_after_merge-def.yaml

______________________________________________________________________

# Release 5.0.0

## Summary of Changes

- Build: Bump version to 5.0.0 in project metadata.
- Templates: Remove outdated PR straight-through template in `templates/py-temp-pr-pvt-straight_through-def.yaml`.
- CI: Tweak release pipeline in `.github/workflows/00-new-release-pipeline.yaml`.
- CI: Update PR tag detection workflow in `.github/workflows/py-pc-pr-detect_tag-def.yaml` for improved reliability.
- CI: Remove deprecated PR straight-through reusable workflow in `.github/workflows/py-wf-pr-pvt_straight_through-def.yaml`.
- Chore: Refresh `.pre-commit-config.yaml` hooks and versions.

## Change Statistics (vs master)

- Branch: `HEAD (detached)`
- 5 files changed, 14 insertions, 153 deletions
- Files changed:
  - .github/workflows/00-new-release-pipeline.yaml
  - .github/workflows/py-pc-pr-detect_tag-def.yaml
  - .github/workflows/py-wf-pr-pvt_straight_through-def.yaml
  - .pre-commit-config.yaml
  - templates/py-temp-pr-pvt-straight_through-def.yaml

______________________________________________________________________

# Release 4.0.0

## Summary of Changes

- Build: Bump version to 4.0.0 in project metadata.
- Templates: Update PR template with Docker in `templates/py-temp-pr-pvt-with_docker-def.yaml` to use repository variables for non-sensitive settings and align secret passthrough.
- CI: Update private CI workflow with Docker in `.github/workflows/py-pc-ci-pvt_with_docker-def.yaml` to export additional environment variables to the `.env` file, ensure Python is set up via `actions/setup-python@v6`, and install Docker Compose on the runner.
- CI: Synchronize PR reusable workflow secret passthrough in `.github/workflows/py-wf-pr-pvt_with_docker-def.yaml` for consistency with the template and CI.

## Change Statistics (vs master)

- Branch: `hendrik/bee-26-feature-devops_automation-py-temp-pr-pvt-with_docker-defyaml`
- 3 files changed, 56 insertions, 40 deletions
- Files changed:
  - .github/workflows/py-pc-ci-pvt_with_docker-def.yaml
  - .github/workflows/py-wf-pr-pvt_with_docker-def.yaml
  - templates/py-temp-pr-pvt-with_docker-def.yaml

______________________________________________________________________

# Release 3.0.1

## Summary of Changes

- Build: Bump version to 3.0.1 in project metadata.
- CI: Update private CI workflow with Docker in `.github/workflows/py-pc-ci-pvt_with_docker-def.yaml`.

## Change Statistics (vs master)

- Branch: `hendrik/bee-26-feature-devops_automation-py-temp-pr-pvt-with_docker-defyaml`
- 1 file changed, 22 insertions, 0 deletions
- Files changed:
  - .github/workflows/py-pc-ci-pvt_with_docker-def.yaml

______________________________________________________________________

# Release 3.0.0

## Summary of Changes

- Build: Bump version to 3.0.0 in project metadata.
- Templates: Update PR template with Docker to accept new MySQL port variables:
  - MYSQL_TCP_PORT_EXTERNAL
  - MYSQL_TCP_PORT_LOCAL_PROD
- CI: Extend reusable workflows with Docker to pass through new MySQL port secrets:
  - .github/workflows/py-pc-ci-pvt_with_docker-def.yaml
  - .github/workflows/py-wf-pr-pvt_with_docker-def.yaml

## Change Statistics (vs master)

- Branch: `hendrik/bee-26-feature-devops_automation-py-temp-pr-pvt-with_docker-defyaml`
- 3 files changed, 14 insertions, 0 deletions
- Files changed:
  - .github/workflows/py-pc-ci-pvt_with_docker-def.yaml
  - .github/workflows/py-wf-pr-pvt_with_docker-def.yaml
  - templates/py-temp-pr-pvt-with_docker-def.yaml

______________________________________________________________________

# Release 2.8.1

## Summary of Changes

- Build: Bump version to 2.8.1 in project metadata.
- CI: Update PR workflow with Docker in `.github/workflows/py-wf-pr-pvt_with_docker-def.yaml`.
- Docs: Update `README.md` with improved guidance.

## Change Statistics (vs master)

- Branch: `hendrik/bee-26-feature-devops_automation-py-temp-pr-pvt-with_docker-defyaml`
- 2 files changed, 10 insertions, 10 deletions
- Files changed:
  - .github/workflows/py-wf-pr-pvt_with_docker-def.yaml
  - README.md

______________________________________________________________________

# Release 2.8.0

## Summary of Changes

- Build: Bump version to 2.8.0 in project metadata.
- CI: Update private CI workflow with Docker in `.github/workflows/py-pc-ci-pvt_with_docker-def.yaml`.

## Change Statistics (vs master)

- Branch: `hendrik/bee-25-new-py-temp-pub-pvt_no_docker-defyaml-github-action`
- 1 file changed, 1 insertion, 0 deletions
- Files changed:
  - .github/workflows/py-pc-ci-pvt_with_docker-def.yaml

______________________________________________________________________

# Release 2.7.0

## Summary of Changes

- Build: Bump version to 2.7.0 in project metadata.
- CI: Update publish CI workflow with Docker in `.github/workflows/py-pc-ci-pub-with_docker-def.yaml`.
- Templates: Minor adjustment to PR template with Docker in `templates/py-temp-pr-pvt-with_docker-def.yaml`.
- Docs: Update `README.md` with refined instructions.

## Change Statistics (vs master)

- Branch: `hendrik/bee-25-new-py-temp-pub-pvt_no_docker-defyaml-github-action`
- 3 files changed, 52 insertions, 20 deletions
- Files changed:
  - .github/workflows/py-pc-ci-pub-with_docker-def.yaml
  - README.md
  - templates/py-temp-pr-pvt-with_docker-def.yaml

______________________________________________________________________

# Release 2.6.0

## Summary of Changes

- Build: Bump version to 2.6.0 in project metadata.
- CI: Update new release pipeline configuration in `.github/workflows/00-new-release-pipeline.yaml`.
- CI: Enhance amend release notes workflow in `.github/workflows/02-amend-release-notes.yaml`.
- CI: Adjust private CI workflows and pre-commit workflow for better consistency:
  - `.github/workflows/py-pc-ci-pvt-no_docker-def.yaml`
  - `.github/workflows/py-pc-ci-pvt_with_docker-def.yaml`
  - `.github/workflows/py-pc-precom-all-def.yaml`
  - `.github/workflows/py-wf-pr-pvt-no_docker-def.yaml`
- CI: Add PR workflow variant with Docker in `.github/workflows/py-wf-pr-pvt_with_docker-def.yaml`.
- Templates: Add PR template with Docker in `templates/py-temp-pr-pvt-with_docker-def.yaml`.
- Templates: Minor updates to existing templates:
  - `templates/legacy/py-temp-dep-pvt_with_docker-def.yaml`
  - `templates/py-temp-pr-pvt-no_docker-def.yaml`
- Docs: Update `README.md` and refresh `ReleaseNotes.md` for this release.
- Chore: Remove obsolete helper files: `ReleaseAmendment.md` and `prompts_ai/ReleaseNotes.txt`.

## Change Statistics (vs master)

- Branch: `hendrik/bee-25-new-py-temp-pub-pvt_no_docker-defyaml-github-action`
- 14 files changed, 261 insertions, 93 deletions
- Files changed:
  - .github/workflows/00-new-release-pipeline.yaml
  - .github/workflows/02-amend-release-notes.yaml
  - .github/workflows/py-pc-ci-pvt-no_docker-def.yaml
  - .github/workflows/py-pc-ci-pvt_with_docker-def.yaml
  - .github/workflows/py-pc-precom-all-def.yaml
  - .github/workflows/py-wf-pr-pvt-no_docker-def.yaml
  - .github/workflows/py-wf-pr-pvt_with_docker-def.yaml
  - README.md
  - ReleaseAmendment.md
  - ReleaseNotes.md
  - prompts_ai/ReleaseNotes.txt
  - templates/legacy/py-temp-dep-pvt_with_docker-def.yaml
  - templates/py-temp-pr-pvt-no_docker-def.yaml
  - templates/py-temp-pr-pvt-with_docker-def.yaml

______________________________________________________________________

# Release 2.5.12

## Summary of Changes

- Build: Bump version to 2.5.13 in project metadata.
- CI: Update new release pipeline configuration in `.github/workflows/00-new-release-pipeline.yaml`.
- CI: Enhance amend release notes workflow in `.github/workflows/02-amend-release-notes.yaml`.
- CI: Streamline private CI workflow (no docker) in `.github/workflows/py-pc-ci-pvt-no_docker-def.yaml`.
- CI: Simplify pre-commit workflow in `.github/workflows/py-pc-precom-all-def.yaml`.
- CI: Tweak PR workflow for private repositories (no docker) in `.github/workflows/py-wf-pr-pvt-no_docker-def.yaml`.
- Docs: Update README with clearer release notes instructions and workflow usage guidance.
- Docs: Refresh `ReleaseAmendment.md` and `ReleaseNotes.md` content for this release.

## Change Statistics (vs master)

- Branch: `hendrik/bee-25-new-py-temp-pub-pvt_no_docker-defyaml-github-action`
- 9 files changed, 102 insertions, 52 deletions
- Files changed:
  - .github/workflows/00-new-release-pipeline.yaml
  - .github/workflows/02-amend-release-notes.yaml
  - .github/workflows/py-pc-ci-pvt-no_docker-def.yaml
  - .github/workflows/py-pc-precom-all-def.yaml
  - .github/workflows/py-wf-pr-pvt-no_docker-def.yaml
  - README.md
  - ReleaseAmendment.md
  - ReleaseNotes.md
  - pyproject.toml

______________________________________________________________________

# Release 2.5.11

## Summary of Changes

- Build: Bump version to 2.5.10 in project metadata.
- Docs: Prepare amendment file to be prefixed to the release notes.
- Maintenance: Minor repository housekeeping updates.

## Change Statistics (vs master)

- 4 files changed, 16 insertions, 11 deletions

______________________________________________________________________

# Release 2.5.9

## Summary of Changes

- Secrets: Update VENV_ENVIRONMENT GitHub Actions secret type for improved consistency and security.

## Change Statistics (vs master)

- 4 files changed, 8 insertions, 3 deletions

______________________________________________________________________

# Release 2.5.7

- Update VENV_ENVIRONMENT GitHub Actions secret

______________________________________________________________________

# Release 2.5.6

The first line must be *bug*, *feature* or *hotfix*

______________________________________________________________________

# Release 2.5.5

This is a bug test

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
  - Added `.github/workflows/py-pc-build-all-def.yaml` (builds with Poetry)
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
  - `.github/workflows/py-wf-pr-pvt-no_docker-def.yaml`
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
    - New: `.github/workflows/py-pc-build-all-def.yaml` (installs deps with Poetry and builds artifacts)
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
- `.github/workflows/py-pc-ci-pub-no_docker-def.yaml`
- `.github/workflows/py-pc-ci-pub-with_docker-def.yaml`
- `.github/workflows/py-pc-ci-pvt-no_docker-def.yaml`
- `.github/workflows/py-pc-ci-pvt_with_docker-def.yaml`
- `.github/workflows/py-pc-pr-def.yaml`
- `.github/workflows/py-pc-precom-all-def.yaml`

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
- `py-pc-ci-pvt-no_docker-def`
  - Add creation of `logs` directory
- `py-pc-dep-with_docker-def.yaml`
  - Add `RELEASE_EMAIL_PASSWORD` and `RELEASE_EMAIL_USER` environment variables.
- `py-wf-dep-pvt_with_docker-def.yaml`
  - Add `RELEASE_EMAIL_PASSWORD` and `RELEASE_EMAIL_USER` environment variables.
  - Add `INSTALLER_USERID`, `INSTALLER_PWD`, `MYSQL_DATABASE`, `MYSQL_HOST`, `MYSQL_PASSWORD`, `MYSQL_ROOT_PASSWORD`, `MYSQL_TCP_PORT`, `MYSQL_USER`, `PROJECT_NAME`
- `py-temp-dep-pvt_no_docker-def.yaml`
  - Rename job `python-template-deploy-private-no-docker` to `py-temp-dep-pvt_no_docker-def`
- `py-temp-dep-pvt_with_docker-def.yaml`
  - Rename job `python-template-deploy-private-with-docker` to `py-temp-dep-pvt_with_docker-def`
  - Add `RELEASE_EMAIL_PASSWORD` and `RELEASE_EMAIL_USER` environment variables.
- `py-temp-fork-pvt-merge_no_docker-def.yaml`
  - Rename job `python-template-merge-with-local-fork` to `py-temp-fork-pvt-merge_no_docker-def`
- `py-temp-fork-pvt-merge_no_docker-def.yaml`
  - Rename job `python-template-fork-merge-with-docker` to `py-temp-fork-pvt-merge_no_docker-def`
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
  - py-temp-fork-pvt-merge_no_docker-def.yaml
  - py-temp-fork-pvt_merge_with_docker-def.yaml
  - py-temp-fork-scheduled_sync_with_upstream-def.yaml

______________________________________________________________________

# Release 1.3.0

- Update py-pc-ci-pub-no_docker-def.yaml with Poetry configuration for private repositories
- Update SetupGitHubAccess to auto create new branches.

______________________________________________________________________

# Release 1.2.2

- Update py-wf-pypi-pub_no_docker-def.yaml with PYPI_API_TOKEN_PROD secret variable
- Update py-pc-pypi-default.yaml with BEE and RTE master token variables
- Add py-pc-pypi-default.yaml Poetry config secrets
- Add py-pc-ci-pub-no_docker-def.yaml Poetry config secrets

______________________________________________________________________

# Release 1.2.1

- Fix and remove Docker sections from py-pc-ci-pvt-no_docker-def
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

# Release 5.0.0

﻿# Release 6.0.0

## Summary of Changes

- Build: Bump version to 6.0.0 in project metadata.
- Templates: Add new publish release notification template in `templates/py-temp-pvt-publish_release_notify_after_merge-def.yaml`.
- Templates: Update PR straight-through template in `templates/py-temp-pr-pvt-straight_through-def.yaml` to align with reusable workflow changes.
- Templates: Update publish build and release notify template in `templates/py-temp-pub-build_release_notify_after_merge-def.yaml` to match renamed workflow.
- CI: Add reusable workflow for release notification after merge in `.github/workflows/py-wf-publish-pvt-release_notify_after_merge-def.yaml`.
- CI: Rename publish after-merge workflow to `.github/workflows/py-wf-publish-pvt-build_release_notify_after_merge-def.yaml` for clarity and consistency.
- CI: Update PR straight-through reusable workflow in `.github/workflows/py-wf-pr-pvt_straight_through-def.yaml`.

## Change Statistics (vs master)

- Branch: `hendrik/rte-153-main_feature-devops-automation-straight-through-processing`
- 6 files changed, 80 insertions, 5 deletions
- Files changed:
  - .github/workflows/py-wf-pr-pvt_straight_through-def.yaml
  - .github/workflows/py-wf-publish-pvt-build_release_notify_after_merge-def.yaml
  - .github/workflows/py-wf-publish-pvt-release_notify_after_merge-def.yaml
  - templates/py-temp-pr-pvt-straight_through-def.yaml
  - templates/py-temp-pub-build_release_notify_after_merge-def.yaml
  - templates/py-temp-pvt-publish_release_notify_after_merge-def.yaml

______________________________________________________________________

# Release 5.0.0
