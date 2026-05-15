# compile

This action can be used in the following manner:

```yaml
jobs:
  compile-latex:
    permissions:
      contents: read
    runs-on: ubuntu-latest
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/latex/compile@vx
```

where `x` is the `major` version of the action.
