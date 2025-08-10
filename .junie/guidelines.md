# Guidelines

You are an expert in Python and scalable web application development. You write secure, maintainable, and
performant code following Python best practices.

## About this Repository

- This repository is a collection of reusable GitHub Actions workflow scripts.
- They are used by and across a multiple Organizations.
- The `templates` directory contains the "start" of the GitHub Action for a repository. This script is copied to the .github directory of each target repository.
- The `templates` scripts calls the reusable scripts in the `.github/workflows` directory of this repository.
- The reusable scripts in the `.github/workflows` are purpose designed to accomplish various tasks.
- The README.md contains the descriptions of these reusable scripts and must be maintained at all times.

## Python Best Practices

- Follow PEP 8 with 120 character line limit
- Use double quotes for Python strings
- Sort imports with `isort`
- Use f-strings for string formatting
- Methods, functions and classes must always be sorted alphabetically on and in the relevant level.

**Explanation:**

- Double quotes are preferred by [Black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
- [isort](https://github.com/PyCQA/isort) automatically sorts imports for you

## Testing

- Always write unit tests and check that they pass for new features.
- Test both positive and negative scenarios

**Explanation:**

- Use `pytest`
