# DevOps Platform Repository

| **Category** | **Status and Links**                                                                                                                                       |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General      | [![][general_maintenance_y_img]][general_maintenance_y_lnk] [![][general_semver_pic]][general_semver_link] [![][general_license_img]][general_license_lnk] |
| CD/CI        | [![][cicd_codestyle_img]][cicd_codestyle_lnk]                                                                                                              |
| PyPI         | [![][pypi_py_versions_img]][pypi_py_versions_lnk] [![][pypi_format_img]][pypi_format_lnk] [![][pypi_downloads_img]][pypi_downloads_lnk]                    |
| Github       | [![][gh_issues_img]][gh_issues_lnk] [![][gh_last_commit_img]][gh_last_commit_lnk]                                                                          |

## Short description

This repository provides reusable GitHub Actions workflows, workflow templates, and automation prompts used to standardize CI/CD implementation across projects.

## Module Overview

### Key Features

- Reusable workflow implementations for CI, PR, publish, fork, and maintenance pipelines.
- Template workflows in `templates/` that delegate execution to reusable workflows in `.github/workflows/`.
- Prompt templates in `ai_prompts/` for release-note generation and Linear issue/project drafting.
- Poetry and pre-commit based project tooling defined in `pyproject.toml` and `.pre-commit-config.yaml`.

### Project Structure

- `.github/workflows/` - Reusable workflow definitions executed by GitHub Actions.
- `templates/` - Template workflow files to copy into downstream repositories.
- `ai_prompts/` - Prompt templates for release updates, issue creation, and project planning.
- `legacy/` - Repository-local output location used by prompt workflows.
- `ReleaseNotes.md` - Historical release log for this repository.

## Getting Started

1. Clone the repository and ensure `Python 3.10+`, `poetry`, and `git` are installed.
2. Run `poetry install` to install project dependencies.
3. Run `pre-commit install` and `pre-commit run --all-files` before opening a PR.
4. Copy a relevant template from `templates/` to your target repository's `.github/workflows/` directory.
5. Use `pushpy.ps1` for validation pushes and `pushpr.ps1` to publish release-ready changes.

## Deployment

### High Level Process Description

1. Push the changes until you are satisfied with your changes. Use `pushpy.ps1`. Monitor GitHub Actions. The workflow
   must complete successfully.
2. Generate `ReleaseNotes.md`, commit the release updates, and run `pushpy.ps1` again if validation requires another pass.
3. Deploy the changes by executing `pushpr.ps1`. Monitor GitHub Actions for successful deployment.

### Detail Process

1. Run the `pushpy.ps1` script or manually commit the current changes. Run it until (repeatedly) all changes are satisfied.

2. Generate the release notes. This can be repeated until all changes are captured in `ReleaseNotes.md`. Consolidate multiple runs into a single release entry before publishing.

   1. Use an AI prompt in your preferred tool (Cursor, Junie, or Codex). Use `ai_prompts/Release-Update-devops_automation.md` for this repository. `ai_prompts/Release-Update-General.md` remains available as a generic fallback.

   alternatively

   1. Use the following template and manually update the ReleaseNotes.md file.

      ```
      ### Release ?.?.?
      - Date: YYYY-MM-DD HH:MM (local)

      ### Summary of Changes
      - Workflows: ...
      - Templates: ...
      - Build: Bumped version to ?.?.? in `pyproject.toml`.

      ### Change Statistics (vs master)
      - Branch: `your-branch-name`
      - Files changed:
        - path/to/file1
        - path/to/file2
      - Number of files changed: N
      - Insertions: X
      - Deletions: Y

      ______________________________________________________________________
      ```

3. Run the `pushpr.ps1` script once you are ready to create the PR to publish the release. You can also manually create the tag, touch a file, commit and push the changes.

4. Merge the PR in GitHub.

## Repository Structure

- `.github/workflows/`
  - Contains the actual workflow files.
  - Workflow names starting with digits are designated for this repository and should not be reused.
- `templates/` - Contains template files for users to copy into their projects.
- `ai_prompts/` - Contains reusable AI prompts for release-note, issue drafting, and project-planning automation tasks.
  - `Release-Update-devops_automation.md` - Repository-specific release-note and SemVer instructions.
  - `Release-Update-General.md` - Generic release-note and SemVer instructions.
  - `Issue-Main-Feature.md` - Prompt template for a Linear main-feature issue.
  - `Issue-Feature.md` - Prompt template for a Linear sub-issue linked to a main feature.
  - `Project-Create-a-new-Project.md` - Prompt template for creating a Linear project definition and milestones.

## Usage

- Each template workflow in `templates/` kicks off a reusable workflow in this repository's
  `.github/workflows/` directory.

- Each reusable workflow is designed to string together the desired combination of
  tasks to achieve the required workflow.

- Supported Python versions are `3.10` through `3.13` as defined in `pyproject.toml`.

- Unless you are familiar with the workflow strategies, do not change the templates
  or any of the workflow scripts.

- Several repositories' CI/CD processes depend on these scripts and may break.

- Discuss any changes with your colleagues to get consensus on any changes or additions.

## Naming Convention

- `<language>-<type>-<task>-<visibility>-<description>-<variation>`
  - where
    - language = `all (All Languages)` | `go (GoLang)` | `py (Python)` | `react (React)`
    - type = `pc` (process) | `temp` (template) | `wf` (workflow)
    - task = `build` | `ci` (continuous integration) | `dep` (deploy) | `fork` | `notify` | `pr` (pull request) | `precom` (pre-commit) | `publish` | `release`
    - visibility = `pvt` (private) | `pub` (public)
    - description = Short description where words are separated by "\_".
    - variation = `def (default)` | Variation description where words are separated by "\_".

## Keeping Workflows Up to date

We regularly update our workflows to improve functionality and security. To ensure you're using the latest version:

1. Periodically check this repository for new releases.
2. Review the changelog for any breaking changes or new features.
3. Update the workflow version in your project's workflow file.

## Setup Instructions

1. Create a `.github/workflows` directory in your project if it doesn't already exist.
2. Select the relevant template from `templates/` directory.
3. Copy the template to the `.github/workflows` directory of your repository.
4. Do not copy any of the workflow files from this repository's `.github/workflows` to the target repository.
5. Refer to similar projects that already use these workflows for configuration examples.

## PR Tag Cleanup Behavior

1. `.github/workflows/all-pc-pr-all-cleanup_tag-def.yaml` deletes the temporary `pr` tag through the GitHub API.
2. HTTP `204` is treated as success.
3. HTTP `404` and `422` are treated as non-fatal because they typically indicate the `pr` tag is already absent.
4. Any other status code fails the workflow to surface unexpected cleanup errors.

## Private Dependency Setup

1. Set a token for private RealTimeEvents repositories in your local environment (PowerShell: `$env:GH_REPO_ACCESS_RTE_LOCAL_USER="<your-token>"`).
2. Run `SetupPrivateRepoAccess.ps1` to refresh Poetry source configuration and dependencies.
3. Use the `$RepoDetailsList` in `SetupPrivateRepoAccess.ps1` to enable or disable repositories with the `active` flag.
4. Keep `rtecommon` active unless your branch explicitly removes that dependency from `pyproject.toml`.

## Available Templates

01. all-temp-fork-pub-scheduled_sync_with_upstream-daily.yaml

    | Type        | Description                                                     |
    | ----------- | --------------------------------------------------------------- |
    | Language    | All                                                             |
    | Type        | Template                                                        |
    | Task        | Fork                                                            |
    | Visibility  | Public                                                          |
    | Description | Scheduled task to sync the origin with the public fork (daily). |
    | Variation   | Daily                                                           |

02. all-temp-fork-pub-scheduled_sync_with_upstream-monthly.yaml

    | Type        | Description                                                       |
    | ----------- | ----------------------------------------------------------------- |
    | Language    | All                                                               |
    | Type        | Template                                                          |
    | Task        | Fork                                                              |
    | Visibility  | Public                                                            |
    | Description | Scheduled task to sync the origin with the public fork (monthly). |
    | Variation   | Monthly                                                           |

03. all-temp-fork-pub-scheduled_sync_with_upstream-weekly.yaml

    | Type        | Description                                                      |
    | ----------- | ---------------------------------------------------------------- |
    | Language    | All                                                              |
    | Type        | Template                                                         |
    | Task        | Fork                                                             |
    | Visibility  | Public                                                           |
    | Description | Scheduled task to sync the origin with the public fork (weekly). |
    | Variation   | Weekly                                                           |

04. all-temp-fork-pvt-scheduled_sync_with_upstream-daily.yaml

    | Type        | Description                                                      |
    | ----------- | ---------------------------------------------------------------- |
    | Language    | All                                                              |
    | Type        | Template                                                         |
    | Task        | Fork                                                             |
    | Visibility  | Private                                                          |
    | Description | Scheduled task to sync the origin with the private fork (daily). |
    | Variation   | Daily                                                            |

05. all-temp-fork-pvt-scheduled_sync_with_upstream-monthly.yaml

    | Type        | Description                                                        |
    | ----------- | ------------------------------------------------------------------ |
    | Language    | All                                                                |
    | Type        | Template                                                           |
    | Task        | Fork                                                               |
    | Visibility  | Private                                                            |
    | Description | Scheduled task to sync the origin with the private fork (monthly). |
    | Variation   | Monthly                                                            |

06. all-temp-fork-pvt-scheduled_sync_with_upstream-weekly.yaml

    | Type        | Description                                                       |
    | ----------- | ----------------------------------------------------------------- |
    | Language    | All                                                               |
    | Type        | Template                                                          |
    | Task        | Fork                                                              |
    | Visibility  | Private                                                           |
    | Description | Scheduled task to sync the origin with the private fork (weekly). |
    | Variation   | Weekly                                                            |

07. iac-temp-fork-pvt-merge_no_docker-def.yaml

    | Type        | Description                                         |
    | ----------- | --------------------------------------------------- |
    | Language    | IaC                                                 |
    | Type        | Template                                            |
    | Task        | Fork                                                |
    | Visibility  | Private                                             |
    | Description | Merge private repository to local fork (no Docker). |
    | Variation   | Default                                             |

08. iac-temp-pr-pvt-straight_through-def.yaml

    | Type        | Description                                   |
    | ----------- | --------------------------------------------- |
    | Language    | IaC                                           |
    | Type        | Template                                      |
    | Task        | Pull Request                                  |
    | Visibility  | Private                                       |
    | Description | Straight through approach (no CI job needed). |
    | Variation   | Default                                       |

09. iac-temp-publish-pvt-release_notify_after_merge-def.yaml

    | Type        | Description                                                                              |
    | ----------- | ---------------------------------------------------------------------------------------- |
    | Language    | IaC                                                                                      |
    | Type        | Template                                                                                 |
    | Task        | Publish                                                                                  |
    | Visibility  | Private                                                                                  |
    | Description | After a Pull Request is merged into master, creates a GitHub release and sends a notice. |
    | Variation   | Default                                                                                  |

10. py-temp-fork-pub-merge_no_docker-def.yaml

    | Type        | Description                                        |
    | ----------- | -------------------------------------------------- |
    | Language    | Python                                             |
    | Type        | Template                                           |
    | Task        | Fork                                               |
    | Visibility  | Public                                             |
    | Description | Merge public repository to local fork (no Docker). |
    | Variation   | Default                                            |

11. py-temp-fork-pub-merge_with_docker-def.yaml

    | Type        | Description                                          |
    | ----------- | ---------------------------------------------------- |
    | Language    | Python                                               |
    | Type        | Template                                             |
    | Task        | Fork                                                 |
    | Visibility  | Public                                               |
    | Description | Merge public repository to local fork (with Docker). |
    | Variation   | Default                                              |

12. py-temp-fork-pvt-merge_no_docker-def.yaml

    | Type        | Description                                         |
    | ----------- | --------------------------------------------------- |
    | Language    | Python                                              |
    | Type        | Template                                            |
    | Task        | Fork                                                |
    | Visibility  | Private                                             |
    | Description | Merge private repository to local fork (no Docker). |
    | Variation   | Default                                             |

13. py-temp-pr-pub-no_docker-def.yaml

    | Type        | Description                                                  |
    | ----------- | ------------------------------------------------------------ |
    | Language    | Python                                                       |
    | Type        | Template                                                     |
    | Task        | Pull Request                                                 |
    | Visibility  | Public                                                       |
    | Description | Public repository with no Docker container to be configured. |
    | Variation   | Default                                                      |

14. py-temp-pr-pub-with_docker-def.yaml

    | Type        | Description                                       |
    | ----------- | ------------------------------------------------- |
    | Language    | Python                                            |
    | Type        | Template                                          |
    | Task        | Pull Request                                      |
    | Visibility  | Public                                            |
    | Description | A Docker container has to be configured (public). |
    | Variation   | Default                                           |

15. py-temp-pr-pvt-no_docker-def.yaml

    | Type        | Description                                                   |
    | ----------- | ------------------------------------------------------------- |
    | Language    | Python                                                        |
    | Type        | Template                                                      |
    | Task        | Pull Request                                                  |
    | Visibility  | Private                                                       |
    | Description | Private repository with no Docker container to be configured. |
    | Variation   | Default                                                       |

16. py-temp-pr-pvt-straight_through-def.yaml

    | Type        | Description                                   |
    | ----------- | --------------------------------------------- |
    | Language    | Python                                        |
    | Type        | Template                                      |
    | Task        | Pull Request                                  |
    | Visibility  | Private                                       |
    | Description | Straight through approach (no CI job needed). |
    | Variation   | Default                                       |

17. py-temp-pr-pvt-with_docker-def.yaml

    | Type        | Description                                        |
    | ----------- | -------------------------------------------------- |
    | Language    | Python                                             |
    | Type        | Template                                           |
    | Task        | Pull Request                                       |
    | Visibility  | Private                                            |
    | Description | A Docker container has to be configured (private). |
    | Variation   | Default                                            |

18. py-temp-pr-pvt-with_native_docker-def.yaml

    | Type        | Description                                                   |
    | ----------- | ------------------------------------------------------------- |
    | Language    | Python                                                        |
    | Type        | Template                                                      |
    | Task        | Pull Request                                                  |
    | Visibility  | Private                                                       |
    | Description | Python template for private PR workflows using native Docker. |
    | Variation   | Default                                                       |

19. py-temp-publish-pub-build_release_notify_after_merge-def.yaml

    | Type        | Description                                                                              |
    | ----------- | ---------------------------------------------------------------------------------------- |
    | Language    | Python                                                                                   |
    | Type        | Template                                                                                 |
    | Task        | Publish                                                                                  |
    | Visibility  | Public                                                                                   |
    | Description | After a Pull Request is merged into master, creates a GitHub release and sends a notice. |
    | Variation   | Default                                                                                  |

20. py-temp-publish-pvt-build_release_notify_after_merge-def.yaml

    | Type        | Description                                                                              |
    | ----------- | ---------------------------------------------------------------------------------------- |
    | Language    | Python                                                                                   |
    | Type        | Template                                                                                 |
    | Task        | Publish                                                                                  |
    | Visibility  | Private                                                                                  |
    | Description | After a Pull Request is merged into master, creates a GitHub release and sends a notice. |
    | Variation   | Default                                                                                  |

21. py-temp-publish-pvt-release_notify_after_merge-def.yaml

    | Type        | Description                                                                              |
    | ----------- | ---------------------------------------------------------------------------------------- |
    | Language    | Python                                                                                   |
    | Type        | Template                                                                                 |
    | Task        | Publish                                                                                  |
    | Visibility  | Private                                                                                  |
    | Description | After a Pull Request is merged into master, creates a GitHub release and sends a notice. |
    | Variation   | Default                                                                                  |

22. react-temp-fork-pvt-merge_with_docker-def.yaml

    | Type        | Description                                           |
    | ----------- | ----------------------------------------------------- |
    | Language    | React                                                 |
    | Type        | Template                                              |
    | Task        | Fork                                                  |
    | Visibility  | Private                                               |
    | Description | Merge private repository to local fork (with Docker). |
    | Variation   | Default                                               |

23. react-temp-pr-pvt-with_docker-def.yaml

    | Type        | Description                                        |
    | ----------- | -------------------------------------------------- |
    | Language    | React                                              |
    | Type        | Template                                           |
    | Task        | Pull Request                                       |
    | Visibility  | Private                                            |
    | Description | A Docker container has to be configured (private). |
    | Variation   | Default                                            |

24. react-temp-publish-pvt-release_notify_after_merge-def.yaml

    | Type        | Description                                                                              |
    | ----------- | ---------------------------------------------------------------------------------------- |
    | Language    | React                                                                                    |
    | Type        | Template                                                                                 |
    | Task        | Publish                                                                                  |
    | Visibility  | Private                                                                                  |
    | Description | After a Pull Request is merged into master, creates a GitHub release and sends a notice. |
    | Variation   | Default                                                                                  |

[cicd_codestyle_img]: https://img.shields.io/badge/code%20style-black-000000.svg "Black"
[cicd_codestyle_lnk]: https://github.com/psf/black "Black"
[general_license_img]: https://img.shields.io/pypi/l/devops-automation "License"
[general_license_lnk]: https://github.com/BrightEdgeeServices/devops-automation/blob/master/LICENSE "License"
[general_maintenance_y_img]: https://img.shields.io/badge/Maintenance%20Intended-%E2%9C%94-green.svg?style=flat-square "Maintenance - intended"
[general_maintenance_y_lnk]: http://unmaintained.tech/ "Maintenance - intended"
[general_semver_link]: https://semver.org/ "Semantic Versioning - 2.0.0"
[general_semver_pic]: https://img.shields.io/badge/Semantic%20Versioning-2.0.0-brightgreen.svg?style=flat-square "Semantic Versioning - 2.0.0"
[gh_issues_img]: https://img.shields.io/github/issues-raw/BrightEdgeeServices/devops-automation "GitHub - Issue Counter"
[gh_issues_lnk]: https://github.com/BrightEdgeeServices/devops-automation/issues "GitHub - Issue Counter"
[gh_last_commit_img]: https://img.shields.io/github/last-commit/BrightEdgeeServices/devops-automation/master "GitHub - Last Commit"
[gh_last_commit_lnk]: https://github.com/BrightEdgeeServices/devops-automation/commit/master "GitHub - Last Commit"
[pypi_downloads_img]: https://img.shields.io/pypi/dm/devops-automation "Monthly downloads"
[pypi_downloads_lnk]: https://pypi.org/project/devops-automation/ "Monthly downloads"
[pypi_format_img]: https://img.shields.io/pypi/wheel/devops-automation "PyPI - Format"
[pypi_format_lnk]: https://pypi.org/project/devops-automation/ "PyPI - Format"
[pypi_py_versions_img]: https://img.shields.io/pypi/pyversions/devops-automation "PyPI - Supported Python Versions"
[pypi_py_versions_lnk]: https://pypi.org/project/devops-automation/ "PyPI - Supported Python Versions"
