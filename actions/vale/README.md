# vale

This action can be used in the following manner:

```yaml
jobs:
  vale:
    permissions:
      contents: read
      pull-requests: read
    runs-on: ubuntu-slim
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/vale@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

where `x` is the `major` version of the action. If flags are required for vale,
then modify the above to:

```yaml
jobs:
  vale:
    permissions:
      contents: read
      pull-requests: read
    runs-on: ubuntu-slim
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/vale@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          vale-flags: ""
```
