# compile

This action can be used in the following manner:

```yaml
jobs:
  compile-latex:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/latex/compile@vx.y.z
```

where `x.y.z` is the `major.minor.patch` version of the action.
