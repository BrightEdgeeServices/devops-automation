# Issue Title

Add Multi-Frequency Scheduled Sync Workflows for Forked Repositories

# Git Branch Name

main_feature-devops-automation-multi-frequency-fork-sync

# Version Prediction

Minor version update: 7.1.7 → 7.2.0

# Description of Feature or Improvement

Currently, all forked repositories in the Universal Rating System (URS) organization use a single daily scheduled sync workflow template (py-temp-fork-scheduled_sync_with_upstream-def.yaml). This approach wastes computational resources and processing time for repositories that update infrequently, as they are unnecessarily checked daily. Additionally, when scheduled workflows fail, they become disabled, requiring manual intervention to re-enable them.

This feature introduces flexibility by providing three distinct reusable workflow templates with different scheduling frequencies (daily, weekly, and monthly), allowing repository maintainers to select the appropriate update cadence based on their repository's actual upstream update patterns. This optimization will reduce unnecessary workflow executions, prevent scheduling disables, and ensure forked repositories remain synchronized with their upstream sources at appropriate intervals.

The scope includes creating two new workflow templates (weekly and monthly), renaming the existing template to clearly indicate its daily scheduling nature, and updating eight specified URS organization repositories to use the appropriate scheduling frequency.

# Proposed Solution

Rename the existing py-temp-fork-scheduled_sync_with_upstream-def.yaml template to py-temp-fork-scheduled_sync_with_upstream-daily-def.yaml to clearly indicate its daily scheduling nature.

Create a new weekly scheduled sync workflow template (py-temp-fork-scheduled_sync_with_upstream-weekly-def.yaml) with cron schedule configured for weekly execution (e.g., '0 0 * * 0' for Sunday at midnight UTC).

Create a new monthly scheduled sync workflow template (py-temp-fork-scheduled_sync_with_upstream-monthly-def.yaml) with cron schedule configured for monthly execution (e.g., '0 0 1 * \*' for the first day of each month at midnight UTC).

Ensure all three workflow templates maintain compatibility with the underlying reusable workflow (py-wf-fork-scheduled_sync_with_upstream-def.yaml) and follow the same structure as the existing template.

Evaluate each of the eight target repositories (VEnvIt, rte_iac, displayfx, beetools, FixDate, SqlDbWrpr, DateId, CsvWrpr) to determine the most appropriate scheduling frequency based on their upstream update patterns and maintenance requirements.

Update each repository sequentially to use the appropriate new template reference, replacing the current workflow configuration.

Document the selection criteria for choosing between daily, weekly, and monthly scheduling frequencies to guide future repository configurations.

# Success Criteria

All three workflow templates (daily, weekly, monthly) are successfully created and available in the devops-automation repository templates directory.

The existing daily workflow template is renamed to reflect its scheduling frequency.

All eight specified URS organization repositories are updated to use the appropriate scheduled sync workflow template based on their update frequency requirements.

No scheduled workflows become disabled due to execution failures during the 60-day monitoring period.

All forked repositories remain synchronized with their upstream repositories at their designated intervals.

Resource utilization metrics show a reduction in unnecessary workflow executions compared to the previous single daily schedule approach.

Workflow execution logs confirm successful synchronization operations for all updated repositories.

New tests are implemented for new functionality.

Old tests are adapted for code changes.

All tests are successful.

ReleaseNotes are updated.

# Deployment Checks

Commented GitHub Workflows scripts for testing purposes are restored.

Functions/methods/variables in modules are in alphabetical order (if possible).

Commented code not useful any more are removed.

Remove warnings, errors and spelling reported by IDE.

Update / remove ToDo's.

CI successful.

CodeCov above 99% or justifiably less.

Merged into master.

ReleaseNotes are published.

Deleted related development branches.

Complete the project in Linear if done.
