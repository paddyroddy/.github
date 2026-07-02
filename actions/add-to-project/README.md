# add-to-project

This action can be used in the following manner:

```yaml
jobs:
  add-issue-to-project:
    permissions:
      issues: read
      pull-requests: read
    runs-on: ubuntu-slim
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/add-to-project@vx
        env:
          PROJECT_TOKEN: ${{ secrets.PROJECT_PAT }}
        with:
          # yamllint disable-line rule:line-length
          project-token: ${{ env.PROJECT_TOKEN }}
```

where `x` is the `major` version of the action. If a different project board is
to be targeted, then the `project-url` input can be used and the above modified
to:

```yaml
jobs:
  add-issue-to-project:
    permissions:
      issues: read
      pull-requests: read
    runs-on: ubuntu-slim
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/add-to-project@vx
        env:
          PROJECT_TOKEN: ${{ secrets.PROJECT_PAT }}
        with:
          # yamllint disable-line rule:line-length
          project-token: ${{ env.PROJECT_TOKEN }}
          project-url: project_board_url
```

where `project_board_url` is the full URL of the project board to which the
repository's issues should be added.
