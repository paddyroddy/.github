# vale

This action can be used in the following manner:

```yaml
jobs:
  vale:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/latex/vale@vx.y.z
        with:
          github-token: ${{ secrets.GITHUB_SECRET }}
```

where `x.y.z` is the `major.minor.patch` version of the action. If flags are
required for vale, then modify the above to:

```yaml
jobs:
  vale:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/latex/vale@vx.y.z
        with:
          github-token: ${{ secrets.GITHUB_SECRET }}
          vale-flags: ""
```
