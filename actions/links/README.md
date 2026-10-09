# links

This action can be used in the following manner:

```yaml
jobs:
  links:
    permissions:
      contents: read
    runs-on: ubuntu-slim
    timeout-minutes: 2
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/links@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

where `x` is the `major` version of the action. If custom link checking is
required, one can add custom inputs through `lychee-args`, i.e.:

```yaml
jobs:
  links:
    permissions:
      contents: read
    runs-on: ubuntu-slim
    timeout-minutes: 2
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/links@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          lychee-args: --no-progress --verbose .
```

If a specific branch is required, one can use the `branch` input:

```yaml
jobs:
  links:
    permissions:
      contents: read
    runs-on: ubuntu-slim
    timeout-minutes: 2
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/links@vx
        with:
          branch: gh-pages
          github-token: ${{ secrets.GITHUB_TOKEN }}
```
