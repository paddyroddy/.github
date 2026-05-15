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
        with:
          licence-file: ./LICENCE.txt
          # yamllint disable-line rule:line-length
          licence-token: ${{ secrets.LICENCE_PAT }} # zizmor: ignore[secrets-outside-env]
```

where `x` is the `major` version of the action.
