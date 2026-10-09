# jekyll

This action can be used in the following manner:

```yaml
jobs:
  build-and-deploy:
    env:
      BUNDLE_GEMFILE: ${{ github.workspace }}/Gemfile
    permissions:
      contents: write
    runs-on: ubuntu-slim
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/github-pages/jekyll@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          ruby-version: "4.0"
```

where `x` is the `major` version of the action.
