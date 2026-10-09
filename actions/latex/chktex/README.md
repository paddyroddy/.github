# chktex

This action can be used in the following manner:

```yaml
jobs:
  chktex:
    permissions:
      contents: read
    runs-on: ubuntu-latest
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/latex/chktex@vx
```

where `x` is the `major` version of the action.
