# deployment

This action can be used in the following manner:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/python/deployment@vx.y.z
        with:
          pypi-api-token: ${{ secrets.PYPI_API_TOKEN }}
          pyproject-toml: ./pyproject.toml
          test-pypi-api-token: ${{ secrets.TEST_PYPI_API_TOKEN }}
```

where `x.y.z` is the `major.minor.patch` version of the action.
