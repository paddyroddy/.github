# deployment

This action can be used in the following manner:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
    steps:
      - uses: paddyroddy/.github/actions/python/deployment@vx
        with:
          pyproject-toml: ./pyproject.toml
          python-version: "3.x"
```

where `x` is the `major` version of the action.
