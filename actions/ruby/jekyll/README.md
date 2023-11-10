# jekyll

This action can be used in the following manner:

```yaml
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/ruby/jekyll@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          ruby-version: "3.2"
```

where `x` is the `major` version of the action. If the documentation is not at
the root directory, then modify the above to, e.g.:

```yaml
jobs:
  build-and-deploy:
    env:
      BUNDLE_GEMFILE: ${{ github.workspace }}/docs
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/ruby/jekyll@vx
        with:
          docs-directory: docs
          github-token: ${{ secrets.GITHUB_TOKEN }}
          ruby-version: "3.2"
```
