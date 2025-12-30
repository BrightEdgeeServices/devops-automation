# Issue Title

Create Multi-Frequency Scheduled Sync Workflow Templates

# Git Branch Name

feature-devops-automation-fork-sync-templates

# Description of the work subset

Currently, the devops-automation repository contains a single scheduled sync workflow template (py-temp-fork-scheduled_sync_with_upstream-def.yaml) that runs daily. This template lacks clear naming to indicate its daily scheduling frequency, and there are no alternative templates available for repositories that require weekly or monthly synchronization schedules.

This work subset focuses exclusively on the devops-automation repository and addresses the template creation and naming requirements. The existing daily template needs to be renamed to clearly indicate its scheduling frequency, and two new templates must be created to provide weekly and monthly scheduling options. All templates must maintain compatibility with the underlying reusable workflow (py-wf-fork-scheduled_sync_with_upstream-def.yaml) and follow the established template structure.

# Proposed Solution for the work subset

Rename the existing py-temp-fork-scheduled_sync_with_upstream-def.yaml template file to py-temp-fork-scheduled_sync_with_upstream-daily-def.yaml to clearly indicate its daily scheduling nature.

Update the template name within the renamed file to reflect the daily scheduling frequency (e.g., "Python Template Scheduled Merge Fork with Upstream - Daily").

Create a new weekly scheduled sync workflow template file named py-temp-fork-scheduled_sync_with_upstream-weekly-def.yaml based on the existing template structure.

Configure the weekly template with a cron schedule for weekly execution (e.g., '0 0 * * 0' for Sunday at midnight UTC) and update the template name to indicate weekly scheduling.

Create a new monthly scheduled sync workflow template file named py-temp-fork-scheduled_sync_with_upstream-monthly-def.yaml based on the existing template structure.

Configure the monthly template with a cron schedule for monthly execution (e.g., '0 0 1 * \*' for the first day of each month at midnight UTC) and update the template name to indicate monthly scheduling.

Ensure all three workflow templates maintain the same structure, permissions, secrets configuration, and compatibility with the underlying reusable workflow (py-wf-fork-scheduled_sync_with_upstream-def.yaml@master).

Verify that all templates include the workflow_dispatch trigger to allow manual execution when needed.

# Success Criteria

The existing daily workflow template is successfully renamed from py-temp-fork-scheduled_sync_with_upstream-def.yaml to py-temp-fork-scheduled_sync_with_upstream-daily-def.yaml.

The renamed daily template contains updated name and cron schedule configuration that clearly indicates daily scheduling.

The weekly workflow template (py-temp-fork-scheduled_sync_with_upstream-weekly-def.yaml) is successfully created in the templates directory.

The weekly template contains appropriate cron schedule configuration for weekly execution and updated name indicating weekly scheduling.

The monthly workflow template (py-temp-fork-scheduled_sync_with_upstream-monthly-def.yaml) is successfully created in the templates directory.

The monthly template contains appropriate cron schedule configuration for monthly execution and updated name indicating monthly scheduling.

All three workflow templates maintain compatibility with the underlying reusable workflow (py-wf-fork-scheduled_sync_with_upstream-def.yaml).

All three workflow templates follow the same structure, permissions, and secrets configuration as the original template.

All three workflow templates include the workflow_dispatch trigger for manual execution.

New tests are implemented for new functionality.

Old tests are adapted for code changes.

All tests are successful.

# Completion Checks

Commented GitHub Workflows scripts for testing purposes are restored.

Functions/methods/variables in modules are in alphabetical order (if possible).

CI successful.

CodeCov above 99% or justifiably less.

Commented code not useful any more are removed.

Remove warnings, errors and spelling reported by IDE.

Update / remove ToDo's.

Merged into main-feature.

Deleted related development branches.
