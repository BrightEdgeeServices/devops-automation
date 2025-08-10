# DevOps Platform Repository

| **Category** | **Status' and Links**                                                                                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| General      | [![][general_maintenance_y_img]][general_maintenance_y_lnk] [![][general_semver_pic]][general_semver_link] [![][general_license_img]][general_license_lnk]                        |
| CD/CI        | [![][cicd_codestyle_img]][cicd_codestyle_lnk]                                                                                                                                     |
| PyPI         | [![][pypi_release_img]][pypi_release_lnk] [![][pypi_py_versions_img]][pypi_py_versions_lnk] [![][pypi_format_img]][pypi_format_lnk] [![][pypi_downloads_img]][pypi_downloads_lnk] |
| Github       | [![][gh_issues_img]][gh_issues_lnk] [![][gh_last_commit_img]][gh_last_commit_lnk]                                                                                                 |

## Repository Structure

- `.github/workflows/`
  - Contains the actual workflow files.
  - Workflow names starting with digits are designated for this repository and should not be reused.
- `templates/` - Contains template files for users to copy into their projects.

## Usage

Each template workflow in `templates/` kick-off a reusable workflow in this repository's
`.github/workflows/` directory.
Each reusable workflow is designed to string together the desired combination of
tasks to achieve the required workflow.

Unless you are familiar with the workflow strategies, do not change the templates
or any of the workflow scripts.
Several repositories' CI/CD processes depend on these scripts and may break.
Discuss any changes with your colleagues to get consensus on any changes or additions.

## Naming Convention

- `<language>-<type>-<task>-<description>-<variation>`
  - where
    - language = `go (GoLang)` | `py (Python)`
    - type = `pc (process)` | `pub (publish)` | `temp (template)` | `wf (workflow)`
    - task = `ci (continuous integration)` | `dep (deploy)` | `precom (pre-commit) | pypi`
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

## Available Templates

1. py-temp-dep-pvt_no_docker-def.yaml

   | Type        | Description                                                  |
   | ----------- | ------------------------------------------------------------ |
   | Language    | Python                                                       |
   | Type        | Template                                                     |
   | Task        | Deployment to production environment                         |
   | Description | Private repository with no Docker container to be configured |
   | Variation   | Default                                                      |

1. py-temp-dep-pvt_with_docker-def.yaml

   | Type        | Description                             |
   | ----------- | --------------------------------------- |
   | Language    | Python                                  |
   | Type        | Template                                |
   | Task        | Deployment to production environment    |
   | Description | A Docker container has to be configured |
   | Variation   | Default                                 |

1. py-temp-fork-pvt_merge_with_local-def.yaml

   | Type        | Description                             |
   | ----------- | --------------------------------------- |
   | Language    | Python                                  |
   | Type        | Template                                |
   | Task        | Fork                                    |
   | Description | Merge private repository to local fork. |
   | Variation   | Default                                 |

1. py-temp-fork-scheduled_sync_with_upstream-def.yaml

   | Type        | Description                                      |
   | ----------- | ------------------------------------------------ |
   | Language    | Python                                           |
   | Type        | Template                                         |
   | Task        | Fork                                             |
   | Description | Scheduled task to sync the origin with the fork. |
   | Variation   | Default                                          |

1. py-temp-pub-pvt_no_docker-def.yaml

   | Type        | Description                                             |
   | ----------- | ------------------------------------------------------- |
   | Language    | Python                                                  |
   | Type        | Template                                                |
   | Task        | Publish in GitHub                                       |
   | Description | Publish in GitHub for use by other private repositories |
   | Variation   | Default                                                 |

1. py-temp-pypi-pub_custom_ci-def.yaml

   | Type        | Description                                                          |
   | ----------- | -------------------------------------------------------------------- |
   | Language    | Python                                                               |
   | Type        | Template                                                             |
   | Task        | Publish to PyPI                                                      |
   | Description | Refers to custom ci process in local directory of target repository. |
   | Variation   | Default                                                              |

1. py-temp-pypi-pub_no_docker-def.yaml

   | Type        | Description                             |
   | ----------- | --------------------------------------- |
   | Language    | Python                                  |
   | Type        | Template                                |
   | Task        | Publish to PyPI                         |
   | Description | A Docker container has to be configured |
   | Variation   | Default                                 |

1. py-temp-pypi-pub_with_docker-def.yaml

   | Type        | Description                             |
   | ----------- | --------------------------------------- |
   | Language    | Python                                  |
   | Type        | Template                                |
   | Task        | Publish to PyPI                         |
   | Description | A Docker container has to be configured |
   | Variation   | Default                                 |

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
[pypi_release_img]: https://img.shields.io/pypi/v/devops-automation "Test status"
[pypi_release_lnk]: https://pypi.org/project/devops-automation/ "Test status"
