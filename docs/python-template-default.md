# Golang CI

This document provides instructions for setting up and using the Golang workflow in your projects.

## Features

- Linting
- Running tests
- Building the application
- Creating a tarball with the binary and configuration
- Creating a GitHub release with the tarball as an asset

## Setup Instructions

1. Create a `.github/workflows` directory in your project if it doesn't already exist.

1. Create a new file named `golang-ci.yml` in the `.github/workflows` directory & copy the contents of the template file provided. `golang-ci.yml`

<!-- 3. Update the `go-version` to match your project's Go version. -->

3. Ensure your project has a `VERSION` file in the root directory containing the current version number (e.g., `1.0.0`).

1. Make sure you have a `config.yml` file in your project root with a `production:` section for the production configuration.

## Troubleshooting

- Ensure your `main.go` file is in the root of your repository.
- Check that your `config.yml` file is properly formatted and includes a `production:` section.
- Verify that your `VERSION` file exists and contains a valid version number.

If you encounter any issues, please check the workflow run logs in GitHub Actions for more detailed error messages.
