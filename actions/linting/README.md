# linting

This action can be used in the following manner:

```yaml
jobs:
  linting:
    runs-on: ubuntu-slim
    steps:
      - uses: paddyroddy/.github/actions/linting@vx
        with:
          pre-commit-config: ./.pre-commit-config.yaml
```

where `x` is the `major` version of the action.
