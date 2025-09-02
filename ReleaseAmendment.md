# Release 2.5.3

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
