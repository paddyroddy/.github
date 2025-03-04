# links

This action can be used in the following manner:

```yaml
jobs:
  links:
    runs-on: ubuntu-latest
    timeout-minutes: 2
    steps:
      - uses: paddyroddy/.github/actions/links@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

where `x` is the `major` version of the action. If custom link checking is
required, one can add custom inputs through `lychee-args`, i.e.:

```yaml
jobs:
  linting:
    runs-on: ubuntu-latest
    timeout-minutes: 2
    steps:
      - uses: paddyroddy/.github/actions/links@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          lychee-args: --no-progress --verbose .
```
