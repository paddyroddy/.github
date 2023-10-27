# linting

This action can be used in the following manner:

```yaml
jobs:
  linting:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/linting@vx.y.z
        with:
          pre-commit-config: ./.pre-commit-config.yaml
```

where `x.y.z` is the `major.minor.patch` version of the action.
