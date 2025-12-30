# Project Title

Fork Repository Scheduled Sync Workflows - Multi-Frequency Support

# Summary Description

Create weekly and monthly workflow templates for forked repository sync to reduce resource waste. Update 8 URS repositories to use appropriate scheduling frequency.

# Description and Objective

This project addresses resource optimization and scheduling flexibility for forked repositories in the Universal Rating System (URS) organization. Currently, all forked repositories use a single daily scheduled sync workflow, which wastes computational resources and processing time for repositories that update infrequently. Additionally, when scheduled workflows fail, they become disabled, requiring manual intervention.

The objective is to create a more efficient and flexible scheduling system by providing three distinct reusable workflow templates (daily, weekly, and monthly) that allow repository maintainers to select the appropriate update frequency based on their repository's actual update cadence. This will reduce unnecessary workflow executions, prevent scheduling disables, and ensure forked repositories remain synchronized with their upstream sources at appropriate intervals.

# Key Features / Deliverables

Rename the existing py-temp-fork-scheduled_sync_with_upstream-def.yaml template to clearly indicate its daily scheduling nature (e.g., py-temp-fork-scheduled_sync_with_upstream-daily-def.yaml)

Create a new weekly scheduled sync workflow template (py-temp-fork-scheduled_sync_with_upstream-weekly-def.yaml) with cron schedule configured for weekly execution

Create a new monthly scheduled sync workflow template (py-temp-fork-scheduled_sync_with_upstream-monthly-def.yaml) with cron schedule configured for monthly execution

Update VEnvIt repository to use the appropriate scheduled sync workflow template

Update rte_iac repository to use the appropriate scheduled sync workflow template

Update displayfx repository to use the appropriate scheduled sync workflow template

Update beetools repository to use the appropriate scheduled sync workflow template

Update FixDate repository to use the appropriate scheduled sync workflow template

Update SqlDbWrpr repository to use the appropriate scheduled sync workflow template

Update DateId repository to use the appropriate scheduled sync workflow template

Update CsvWrpr repository to use the appropriate scheduled sync workflow template

Ensure all three workflow templates maintain compatibility with the underlying reusable workflow (py-wf-fork-scheduled_sync_with_upstream-def.yaml)

Document the selection criteria for choosing between daily, weekly, and monthly scheduling frequencies

# Success Criteria

All three workflow templates (daily, weekly, monthly) are successfully created and available in the devops-automation repository templates directory

The existing daily workflow template is renamed to reflect its scheduling frequency

All eight specified URS organization repositories are updated to use the appropriate scheduled sync workflow template based on their update frequency requirements

No scheduled workflows become disabled due to execution failures during the 60-day monitoring period

All forked repositories remain synchronized with their upstream repositories at their designated intervals

Resource utilization metrics show a reduction in unnecessary workflow executions compared to the previous single daily schedule approach

Workflow execution logs confirm successful synchronization operations for all updated repositories

# Deployment & Rollout Plan

Phase 1 - Template Creation: Create the weekly and monthly workflow templates in the devops-automation repository templates directory, ensuring they follow the same structure as the existing daily template with appropriate cron schedule modifications

Phase 2 - Template Renaming: Rename the existing py-temp-fork-scheduled_sync_with_upstream-def.yaml to py-temp-fork-scheduled_sync_with_upstream-daily-def.yaml to clearly indicate its daily scheduling nature

Phase 3 - Repository Assessment: Evaluate each of the eight target repositories to determine the most appropriate scheduling frequency (daily, weekly, or monthly) based on their upstream update patterns and maintenance requirements

Phase 4 - Repository Updates: Update each of the eight repositories sequentially, replacing the current workflow reference with the appropriate new template reference (daily, weekly, or monthly)

Phase 5 - Validation: Verify that all updated repositories have the correct workflow configuration and that the workflow files are properly committed to their respective repositories

Phase 6 - Monitoring Period: Monitor all updated repositories for 60 days to ensure scheduled workflows execute successfully without becoming disabled, and verify that repository synchronization occurs as expected

Phase 7 - Documentation: Update any relevant documentation to reflect the new multi-frequency workflow options and provide guidance on selecting the appropriate schedule
