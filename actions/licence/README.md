# licence

This action can be used in the following manner:

```yaml
jobs:
  licence:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/licence@vx
        with:
          licence-token: ${{ secrets.LICENCE_PAT }}
          licence-file: ./LICENCE.txt
```

where `x` is the `major` version of the action.
