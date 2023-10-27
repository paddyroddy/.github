# pdoc

This action can be used in the following manner:

```yaml
jobs:
  documentation:
    runs-on: ubuntu-latest
    steps:
      - uses: paddyroddy/.github/actions/python/pdoc@vx.y.z
        with:
          docs-dependency-section: .[docs]
          gh-pages-publish-directory: ./html/python_project
          github-token: ${{ secrets.GITHUB_TOKEN }}
          project-directory: ./src/python_project
          pyproject-toml: ./pyproject.toml
          python-version: "3.x"
          template-directory: ./documentation
```

where `x.y.z` is the `major.minor.patch` version of the action.
