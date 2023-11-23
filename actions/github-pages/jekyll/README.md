# jekyll

This action can be used in the following manner:

```yaml
jobs:
  build-and-deploy:
    env:
      BUNDLE_GEMFILE: ${{ github.workspace }}/Gemfile
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/github-pages/jekyll@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          ruby-version: "3.2"
```

where `x` is the `major` version of the action.
