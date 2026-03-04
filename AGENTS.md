# Repository Guidelines for Codex

You are an expert in Python and scalable web application development. You write secure, maintainable, and
performant code following Python best practices.

## Project Structure & Module Organization

- Core application code lives in `devops-automation/`.
- The envorinment are driven by environment variables. The $env:PROJECT_DIR holds the base directory for all repos.
- Tests are in `tests/` (`unit/`, `functional`, `helpers/`, `test_data/`).
- Legacy/archived code is in `legacy/` and `tests/legacy/` (excluded from normal test runs).
- SQL/bootstrap assets are in `scripts/` and `data/`.

## Build, Test, and Development Commands

- `.env` file is created by the `SetupDotEnv.ps1` in the repo root directory. Do not edit the `.env` file direct. Amend the `SetupDotEnv.ps1` script and then run it to update the `.env` file.
- External Docker is only used for functional (end-to-end) testing. Units test will create its own Docker container and
  database instance for testing.
- External Docker container is created by running the `SetUpDocker.ps1` script, which calls several other scripts. This script can be amended as needed.
- SQL/bootstrap assets are in `scripts/` and `data/`.

## Testing

**General Guidelines**

- The file name for the test is a combination of the module directory and subdirectories in snake_case.
- The class test name is the name of the class- or function name in the module in CamelCase.
- The test method name is the name of the test function followed by a description in snake_case.
- Tests must be named in the format `test_*.py`.
- Prefer deterministic unit tests
- Use fixtures from `tests/conftest.py` and `tests/test_data/`.
- Do not assign any default values to any variable. If the actual value is not available, the code must crash.

**Unit Testing Guidelines**

- Always write unit tests for all new code and check that they pass for new features.
- Do not mock database connections ir sessions.
- Do not mock Google dependencies e.g. GoogleDriveManager. Use the
- Do not mock any functions within the module under test or in the same repo.
- Each unit test must test a single functionality.
- Unit tests must only test the code in the relevant module.
- Unit tests must reside in the `tests/unit` directory.

**Functionality Testing Guidelines**

- Only write functional tests on request.
- Functional tests must test the integration of multiple modules.
- Functional tests must reside in the `tests/functional` directory.

## Security and Credentials

- Each repo have a `.env` file that contains the relevant environment variables, secrets and credentials for that repo.
- GitHub can be accessed by using the $env:GH_REPO_ACCESS_RTE_LOCAL_USER token
- The default port for MySQL are in the environment variable $env:MYSQL_TCP_PORT
- The default database name for MySQL are in the environment variable $env:MYSQL_DATABASE
- The default password for MySQL are in the environment variable $env:MYSQL_PASSWORD
- The default host for MySQL are in the environment variable $env:MYSQL_HOST
- The default user name for MySQL are in the environment variable $env:MYSQL_USER
- The default root password for MySQL are in the environment variable $env:MYSQL_ROOT_PASSWORD
