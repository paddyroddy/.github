# vale

This action can be used in the following manner:

```yaml
jobs:
  vale:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/latex/vale@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

where `x` is the `major` version of the action. If flags are required for vale,
then modify the above to:

```yaml
jobs:
  vale:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/latex/vale@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          vale-flags: ""
```
