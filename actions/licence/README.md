# licence

This action can be used in the following manner:

```yaml
jobs:
  licence:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/licence@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          licence-file: ./LICENCE.md
```

where `x` is the `major` version of the action.
