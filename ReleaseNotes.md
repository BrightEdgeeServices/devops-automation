# Release 1.4.2

- py-pc-ci-pvt_with_docker-def.yaml
  - Update "Configure Poetry" step.
  - Fixed "Configure Poetry" step.
  - Add creation of `logs` directory
- py-pc-ci-pvt_no_docker-def.
  - Add creation of `logs` directory
- py-pc-dep-with_docker-def.yaml
  - Add RELEASE_EMAIL_PASSWORD and RELEASE_EMAIL_USER environment variables.
- py-wf-dep-pvt_with_docker-def.yaml
  - Add RELEASE_EMAIL_PASSWORD and RELEASE_EMAIL_USER environment variables.
  - Add INSTALLER_USER_ID, INSTALLER_USER_PWD, MYSQL_DATABASE, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_ROOT_PASSWORD, MYSQL_TCP_PORT, MYSQL_USER, PROJECT_NAME
- py-temp-dep-pvt_no_docker-def.yaml
  - Rename job python-template-deploy-private-no-docker to py-temp-dep-pvt_no_docker-def
- py-temp-dep-pvt_with_docker-def.yaml
  - Rename job python-template-deploy-private-with-docker to py-temp-dep-pvt_with_docker-def
  - Add RELEASE_EMAIL_PASSWORD and RELEASE_EMAIL_USER environment variables.
- py-temp-fork-pvt_merge_no_docker-def.yaml
  - Rename job python-template-merge-with-local-fork to py-temp-fork-pvt_merge_no_docker-def
- py-temp-fork-pvt_merge_no_docker-def.yaml
  - Rename job python-template-fork-merge-with-docker to py-temp-fork-pvt_merge_no_docker-def
- py-temp-fork-scheduled_sync_with_upstream-def.yaml
  - Rename scheduled-fork-update-pull-template to py-temp-fork-scheduled_sync_with_upstream-def
- py-temp-pypi-pub_no_docker-def.yaml
  - Rename job python-template-pypi-public-no-docker to py-temp-pypi-pub_no_docker-def
- py-temp-pypi-pub_with_docker-def.yaml
  - Rename job python-template-pypi-public-with-docker to py-temp-pypi-pub_with_docker-def

______________________________________________________________________

# Release 1.4.1

- Add PYPI_API_TOKEN_PROD in py-wf-pypi-pub_with_docker-def.yaml

______________________________________________________________________

# Release 1.4.0

- Removed the .github/ISSUE_TEMPLATE directory.
  This will force the repository to use the
  BrightEdgeeServices/.github/ISSUE_TEMPLATE directory, centralizing the maintenance of templates.
- Add workflow to automate the update of forked repositories:
  - py-pc-fork-merge-def.yaml
  - py-pc-fork-sync_with_upstream-def.yaml
  - py-wf-fork-merge_no_docker-def.yaml
  - py-wf-fork-merge_with_docker-def.yaml
  - py-wf-fork-scheduled_sync_with_upstream-def.yaml
  - py-temp-fork-pvt_merge_no_docker-def.yaml
  - py-temp-fork-pvt_merge_with_docker-def.yaml
  - py-temp-fork-scheduled_sync_with_upstream-def.yaml

______________________________________________________________________

# Release 1.3.0

- Update py-pc-ci-pub_no_docker-def.yaml with Poetry configuration for private repositories
- Update SetupGitHubAccess to auto create new branches.

______________________________________________________________________

# Release 1.2.2

- Update py-wf-pypi-pub_no_docker-def.yaml with PYPI_API_TOKEN_PROD secret variable
- Update py-pc-pypi-default.yaml with BEE and RTE master token variables
- Add py-pc-pypi-default.yaml Poetry config secrets
- Add py-pc-ci-pub_no_docker-def.yaml Poetry config secrets

______________________________________________________________________

# Release 1.2.1

- Fix and remove Docker sections from py-pc-ci-pvt_no_docker-def
- Configure secrets variables so that it is inherited/transferred between the reusable workflows.

______________________________________________________________________

# Release 1.2.0

- Update the secrets' references.
- Add the ISSUE_TEMPLATEs

______________________________________________________________________

# Release 1.1.0

- Update badges.
- Change the name of 00-deployment-pipeline.yaml to Production Pipeline
- Remove version reference from target custom workflows
- Add a pub_custom_ci workflow
  - py-temp-pypi-pub_custom_ci-def.yaml
  - py-wf-pypi-pub_custom_ci-def.yaml.yaml

______________________________________________________________________

# Release 1.0.0

- Rename all workflow scripts to shorten the names.
- Update workflow scripts
- Format workflow scripts
- Install automation scripts

______________________________________________________________________

# Release 0.2.0

- Implement reusable GitHub workflows.
- templates:
  - python-template-deploy.yaml
  - python-template-pypi.yaml

______________________________________________________________________

# Release 0.1.0

- No Release Notes will be kept according to a group decision.

______________________________________________________________________
