# add-to-project

This action can be used in the following manner:

```yaml
jobs:
  add-issue-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/add-to-project@vx
        with:
          app-id: ${{ vars.PROJECT_BOARD_APP_ID }}
          app-pem: ${{ secrets.PROJECT_BOARD_PRIVATE_KEY }}
```

where `x` is the `major` version of the action. If a different project board is
to be targeted, then the `project-url` input can be used and the above modified
to:

```yaml
jobs:
  add-issue-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/add-to-project@vx
        with:
          app-id: ${{ vars.PROJECT_BOARD_APP_ID }}
          app-pem: ${{ secrets.PROJECT_BOARD_PRIVATE_KEY }}
          project-url: project_board_url
```

where `project_board_url` is the full URL of the project board to which the
repository's issues should be added.
