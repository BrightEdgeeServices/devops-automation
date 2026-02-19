# DevOps Platform Repository

| **Category** | **Status' and Links**                                                                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General      | [![][general_maintenance_y_img]][general_maintenance_y_lnk] [![][general_semver_pic]][general_semver_link] [![][general_license_img]][general_license_lnk] |
| CD/CI        | [![][cicd_codestyle_img]][cicd_codestyle_lnk]                                                                                                              |
| PyPI         | [![][pypi_py_versions_img]][pypi_py_versions_lnk] [![][pypi_format_img]][pypi_format_lnk] [![][pypi_downloads_img]][pypi_downloads_lnk]                    |
| Github       | [![][gh_issues_img]][gh_issues_lnk] [![][gh_last_commit_img]][gh_last_commit_lnk]                                                                          |

## Deployment

### High Level Process Description

1. Push the changes until you are satisfied with your changes. Use `pushpy.ps1`. Monitor GitHub Actions. The workflow
   must complete successfully.
1. Generate the ReleaseNotes and do `pushpy.ps1`.
1. Deploy the changes by executing `pushpr.ps1`. Monitor GitHub Actions for successful deployment.

### Detail Process

1. Run the `pushpy.ps1` script or manually commit the current changes. Run it until (repeatedly) all changes are satisfied.

1. Generate the release notes. This can be repeated until all changes are captured in `ReleaseNotes.md`. Consolidate multiple runs into a single release entry before publishing.

   1. Use an AI prompt in your preferred tool (Cursor, Junie, or Codex). The default prompt is stored in `ai_prompts/Release-Update-General.txt`.

   alternatively

   1. Use the following template and manually update the ReleaseNotes.md file.

      ```
       # Release ?.?.?
       ## Summary of Changes
       - bla, bla, bla
       ## Next Heading
       - bla, bla, bla
       ---
      ```

1. Run the `pushpr.ps1` script once you are ready to create the PR to publish the release. You can also manually create the tag, touch a file, commit and push the changes.

1. Merge the PR in GitHub.

## Repository Structure

- `.github/workflows/`
  - Contains the actual workflow files.
  - Workflow names starting with digits are designated for this repository and should not be reused.
- `templates/` - Contains template files for users to copy into their projects.
- `ai_prompts/` - Contains reusable AI prompts for release-note and repository automation tasks.

## Usage

- Each template workflow in `templates/` kick-off a reusable workflow in this repository's
  `.github/workflows/` directory.

- Each reusable workflow is designed to string together the desired combination of
  tasks to achieve the required workflow.

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
1. Review the changelog for any breaking changes or new features.
1. Update the workflow version in your project's workflow file.

## Setup Instructions

1. Create a `.github/workflows` directory in your project if it doesn't already exist.
1. Select the relevant template from `templates/` directory.
1. Copy the template to the `.github/workflows` directory of your repository.
1. Do not copy any of the workflow files from this repositories `.github/workflows` to the target repository.
1. Refer to similar projects that already use these workflows for configuration examples.

## Available Templates

1. all-temp-fork-pub-scheduled_sync_with_upstream-daily.yaml

   | Type        | Description                                                     |
   | ----------- | --------------------------------------------------------------- |
   | Language    | All                                                             |
   | Type        | Template                                                        |
   | Task        | Fork                                                            |
   | Visibility  | Public                                                          |
   | Description | Scheduled task to sync the origin with the public fork (daily). |
   | Variation   | Daily                                                           |

1. all-temp-fork-pub-scheduled_sync_with_upstream-monthly.yaml

   | Type        | Description                                                       |
   | ----------- | ----------------------------------------------------------------- |
   | Language    | All                                                               |
   | Type        | Template                                                          |
   | Task        | Fork                                                              |
   | Visibility  | Public                                                            |
   | Description | Scheduled task to sync the origin with the public fork (monthly). |
   | Variation   | Monthly                                                           |

1. all-temp-fork-pub-scheduled_sync_with_upstream-weekly.yaml

   | Type        | Description                                                      |
   | ----------- | ---------------------------------------------------------------- |
   | Language    | All                                                              |
   | Type        | Template                                                         |
   | Task        | Fork                                                             |
   | Visibility  | Public                                                           |
   | Description | Scheduled task to sync the origin with the public fork (weekly). |
   | Variation   | Weekly                                                           |

1. all-temp-fork-pvt-scheduled_sync_with_upstream-daily.yaml

   | Type        | Description                                                      |
   | ----------- | ---------------------------------------------------------------- |
   | Language    | All                                                              |
   | Type        | Template                                                         |
   | Task        | Fork                                                             |
   | Visibility  | Private                                                          |
   | Description | Scheduled task to sync the origin with the private fork (daily). |
   | Variation   | Daily                                                            |

1. all-temp-fork-pvt-scheduled_sync_with_upstream-monthly.yaml

   | Type        | Description                                                        |
   | ----------- | ------------------------------------------------------------------ |
   | Language    | All                                                                |
   | Type        | Template                                                           |
   | Task        | Fork                                                               |
   | Visibility  | Private                                                            |
   | Description | Scheduled task to sync the origin with the private fork (monthly). |
   | Variation   | Monthly                                                            |

1. all-temp-fork-pvt-scheduled_sync_with_upstream-weekly.yaml

   | Type        | Description                                                       |
   | ----------- | ----------------------------------------------------------------- |
   | Language    | All                                                               |
   | Type        | Template                                                          |
   | Task        | Fork                                                              |
   | Visibility  | Private                                                           |
   | Description | Scheduled task to sync the origin with the private fork (weekly). |
   | Variation   | Weekly                                                            |

1. iac-temp-fork-pvt-merge_no_docker-def.yaml

   | Type        | Description                                         |
   | ----------- | --------------------------------------------------- |
   | Language    | IaC                                                 |
   | Type        | Template                                            |
   | Task        | Fork                                                |
   | Visibility  | Private                                             |
   | Description | Merge private repository to local fork (no Docker). |
   | Variation   | Default                                             |

1. iac-temp-pr-pvt-straight_through-def.yaml

   | Type        | Description                                   |
   | ----------- | --------------------------------------------- |
   | Language    | IaC                                           |
   | Type        | Template                                      |
   | Task        | Pull Request                                  |
   | Visibility  | Private                                       |
   | Description | Straight through approach (no CI job needed). |
   | Variation   | Default                                       |

1. iac-temp-publish-pvt-release_notify_after_merge-def.yaml

   | Type        | Description                                                                              |
   | ----------- | ---------------------------------------------------------------------------------------- |
   | Language    | IaC                                                                                      |
   | Type        | Template                                                                                 |
   | Task        | Publish                                                                                  |
   | Visibility  | Private                                                                                  |
   | Description | After a Pull Request is merged into master, creates a GitHub release and sends a notice. |
   | Variation   | Default                                                                                  |

1. py-temp-fork-pub-merge_no_docker-def.yaml

   | Type        | Description                                        |
   | ----------- | -------------------------------------------------- |
   | Language    | Python                                             |
   | Type        | Template                                           |
   | Task        | Fork                                               |
   | Visibility  | Public                                             |
   | Description | Merge public repository to local fork (no Docker). |
   | Variation   | Default                                            |

1. py-temp-fork-pub-merge_with_docker-def.yaml

   | Type        | Description                                          |
   | ----------- | ---------------------------------------------------- |
   | Language    | Python                                               |
   | Type        | Template                                             |
   | Task        | Fork                                                 |
   | Visibility  | Public                                               |
   | Description | Merge public repository to local fork (with Docker). |
   | Variation   | Default                                              |

1. py-temp-fork-pvt-merge_no_docker-def.yaml

   | Type        | Description                                         |
   | ----------- | --------------------------------------------------- |
   | Language    | Python                                              |
   | Type        | Template                                            |
   | Task        | Fork                                                |
   | Visibility  | Private                                             |
   | Description | Merge private repository to local fork (no Docker). |
   | Variation   | Default                                             |

1. py-temp-pr-pub-no_docker-def.yaml

   | Type        | Description                                                  |
   | ----------- | ------------------------------------------------------------ |
   | Language    | Python                                                       |
   | Type        | Template                                                     |
   | Task        | Pull Request                                                 |
   | Visibility  | Public                                                       |
   | Description | Public repository with no Docker container to be configured. |
   | Variation   | Default                                                      |

1. py-temp-pr-pub-with_docker-def.yaml

   | Type        | Description                                       |
   | ----------- | ------------------------------------------------- |
   | Language    | Python                                            |
   | Type        | Template                                          |
   | Task        | Pull Request                                      |
   | Visibility  | Public                                            |
   | Description | A Docker container has to be configured (public). |
   | Variation   | Default                                           |

1. py-temp-pr-pvt-no_docker-def.yaml

   | Type        | Description                                                   |
   | ----------- | ------------------------------------------------------------- |
   | Language    | Python                                                        |
   | Type        | Template                                                      |
   | Task        | Pull Request                                                  |
   | Visibility  | Private                                                       |
   | Description | Private repository with no Docker container to be configured. |
   | Variation   | Default                                                       |

1. py-temp-pr-pvt-straight_through-def.yaml

   | Type        | Description                                   |
   | ----------- | --------------------------------------------- |
   | Language    | Python                                        |
   | Type        | Template                                      |
   | Task        | Pull Request                                  |
   | Visibility  | Private                                       |
   | Description | Straight through approach (no CI job needed). |
   | Variation   | Default                                       |

1. py-temp-pr-pvt-with_docker-def.yaml

   | Type        | Description                                        |
   | ----------- | -------------------------------------------------- |
   | Language    | Python                                             |
   | Type        | Template                                           |
   | Task        | Pull Request                                       |
   | Visibility  | Private                                            |
   | Description | A Docker container has to be configured (private). |
   | Variation   | Default                                            |

1. py-temp-pr-pvt-with_native_docker-def.yaml

   | Type        | Description                                                   |
   | ----------- | ------------------------------------------------------------- |
   | Language    | Python                                                        |
   | Type        | Template                                                      |
   | Task        | Pull Request                                                  |
   | Visibility  | Private                                                       |
   | Description | Python template for private PR workflows using native Docker. |
   | Variation   | Default                                                       |

1. py-temp-publish-pub-build_release_notify_after_merge-def.yaml

   | Type        | Description                                                                              |
   | ----------- | ---------------------------------------------------------------------------------------- |
   | Language    | Python                                                                                   |
   | Type        | Template                                                                                 |
   | Task        | Publish                                                                                  |
   | Visibility  | Public                                                                                   |
   | Description | After a Pull Request is merged into master, creates a GitHub release and sends a notice. |
   | Variation   | Default                                                                                  |

1. py-temp-publish-pvt-build_release_notify_after_merge-def.yaml

   | Type        | Description                                                                              |
   | ----------- | ---------------------------------------------------------------------------------------- |
   | Language    | Python                                                                                   |
   | Type        | Template                                                                                 |
   | Task        | Publish                                                                                  |
   | Visibility  | Private                                                                                  |
   | Description | After a Pull Request is merged into master, creates a GitHub release and sends a notice. |
   | Variation   | Default                                                                                  |

1. py-temp-publish-pvt-release_notify_after_merge-def.yaml

   | Type        | Description                                                                              |
   | ----------- | ---------------------------------------------------------------------------------------- |
   | Language    | Python                                                                                   |
   | Type        | Template                                                                                 |
   | Task        | Publish                                                                                  |
   | Visibility  | Private                                                                                  |
   | Description | After a Pull Request is merged into master, creates a GitHub release and sends a notice. |
   | Variation   | Default                                                                                  |

1. react-temp-fork-pvt-merge_with_docker-def.yaml

   | Type        | Description                                           |
   | ----------- | ----------------------------------------------------- |
   | Language    | React                                                 |
   | Type        | Template                                              |
   | Task        | Fork                                                  |
   | Visibility  | Private                                               |
   | Description | Merge private repository to local fork (with Docker). |
   | Variation   | Default                                               |

1. react-temp-pr-pvt-with_docker-def.yaml

   | Type        | Description                                        |
   | ----------- | -------------------------------------------------- |
   | Language    | React                                              |
   | Type        | Template                                           |
   | Task        | Pull Request                                       |
   | Visibility  | Private                                            |
   | Description | A Docker container has to be configured (private). |
   | Variation   | Default                                            |

1. react-temp-publish-pvt-release_notify_after_merge-def.yaml

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
[general_semver_link]: https://semver.org/ "Sentic Versioning - 2.0.0"
[general_semver_pic]: https://img.shields.io/badge/Semantic%20Versioning-2.0.0-brightgreen.svg?style=flat-square "Sentic Versioning - 2.0.0"
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
