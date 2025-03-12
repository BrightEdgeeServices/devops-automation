# DevOps Platform Repository

| **Category** | **Status' and Links**                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------- |
| General      | [![][general_maintenance_y_img]][general_maintenance_y_lnk] [![][general_semver_pic]][general_semver_link] |

This repository contains reusable GitHub Actions workflows for various programming languages and frameworks. These
workflows are designed to be easily integrated into your projects to provide consistent CI/CD processes across your
organization.

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
    - type = `pc (process)` | `temp (template)` | `wf (workflow)`
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
1. Do not copy any of the workflow files from this repositories `.github/workflows`.

## Available Templates

1. py-temp-dep-pvt_no_docker-def.yaml

   | Type        | Description                              |
   | ----------- | ---------------------------------------- |
   | Language    | Python                                   |
   | Type        | Template                                 |
   | Task        | Deployment to production environment     |
   | Description | No Docker container has to be configured |
   | Variation   | Default                                  |

1. py-temp-dep-pvt_with_docker-def.yaml

   | Type        | Description                             |
   | ----------- | --------------------------------------- |
   | Language    | Python                                  |
   | Type        | Template                                |
   | Task        | Deployment to production environment    |
   | Description | A Docker container has to be configured |
   | Variation   | Default                                 |

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

[general_maintenance_y_img]: https://img.shields.io/badge/Maintenance%20Intended-%E2%9C%94-green.svg?style=flat-square "Maintenance - intended"
[general_maintenance_y_lnk]: http://unmaintained.tech/ "Maintenance - intended"
[general_semver_link]: https://semver.org/ "Sentic Versioning - 2.0.0"
[general_semver_pic]: https://img.shields.io/badge/Semantic%20Versioning-2.0.0-brightgreen.svg?style=flat-square "Sentic Versioning - 2.0.0"
