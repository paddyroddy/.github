# jekyll

This action can be used in the following manner:

```yaml
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/ruby/jekyll@vx.y.z
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          ruby-version: "3.2"
```

where `x.y.z` is the `major.minor.patch` version of the action.
