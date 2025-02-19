# DevOps Platform Repository

| **Category** | **Status' and Links**                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------- |
| General      | [![][general_maintenance_y_img]][general_maintenance_y_lnk] [![][general_semver_pic]][general_semver_link] |

This repository contains reusable GitHub Actions workflows for various programming languages and frameworks. These
workflows are designed to be easily integrated into your projects to provide consistent CI/CD processes across your
organization.

## Available Workflows

- [Golang CI](./docs/golang-ci.md)
- [Python Default](./docs/python-template-default.md)

## Usage

1. Choose the workflow that matches your project's language or framework.
1. Follow the setup instructions in the workflow-specific documentation in the `docs/` directory.
1. Do not change the template workflows. If there is a specific need, discuss it with the team to create a customized
   workflow.

## Naming Convention

- <language>-<type>-<task>-<description>
  - where
    - language = `Golang` | `Python`
    - type = `process` | `template` | `wf`
    - task = `default` (for workflows) | `ci` | `deploy` | `precommit`
    - description = Short description. If it is the default it sshould be `none`

## Repository Structure

- `.github/workflows/`: Contains the actual workflow files.
- `docs/`: Contains detailed documentation for each workflow.
- `templates/`: Contains template files for users to copy into their projects.

## Keeping Workflows Up-to-Date

We regularly update our workflows to improve functionality and security. To ensure you're using the latest version:

1. Periodically check this repository for new releases.
1. Review the changelog for any breaking changes or new features.
1. Update the workflow version in your project's workflow file.

## Repository Workflow Rules

This repository follows strict workflow rules to ensure code quality and proper review processes:

1. All changes must be associated with an issue.
1. Changes can only be merged into the main branch via pull requests.
1. Pull requests require approval from at least two reviewers.
1. The main branch is protected and can only be updated through approved pull requests.
1. When referencing workflows in your projects, use a specific version tag or commit SHA to ensure stability.

[general_maintenance_y_img]: https://img.shields.io/badge/Maintenance%20Intended-%E2%9C%94-green.svg?style=flat-square "Maintenance - intended"
[general_maintenance_y_lnk]: http://unmaintained.tech/ "Maintenance - intended"
[general_semver_link]: https://semver.org/ "Sentic Versioning - 2.0.0"
[general_semver_pic]: https://img.shields.io/badge/Semantic%20Versioning-2.0.0-brightgreen.svg?style=flat-square "Sentic Versioning - 2.0.0"
