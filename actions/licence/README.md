# licence

This action can be used in the following manner:

```yaml
jobs:
  update-licence-year:
    permissions:
      contents: read
    runs-on: ubuntu-slim
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/licence@vx
        env:
          LICENCE_TOKEN: ${{ secrets.LICENCE_PAT }}
        with:
          licence-file: ./LICENCE.txt
          # yamllint disable-line rule:line-length
          licence-token: ${{ env.LICENCE_TOKEN }}
```

where `x` is the `major` version of the action.
