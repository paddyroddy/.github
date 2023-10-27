# licence

This action can be used in the following manner:

```yaml
jobs:
  licence:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/licence@vx.y.z
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          licence-file: ./LICENCE.md
```

where `x.y.z` is the `major.minor.patch` version of the action.
