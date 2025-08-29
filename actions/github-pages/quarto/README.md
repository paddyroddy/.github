# quarto

This action can be used in the following manner:

```yaml
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: paddyroddy/.github/actions/github-pages/quarto@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

where `x` is the `major` version of the action. If Python dependencies are
required they can be specified via the `pyproject-toml` input:

```yaml
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: paddyroddy/.github/actions/github-pages/quarto@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          pyproject-toml: ./pyproject.toml
```

where `./pyproject.toml` is the path to the `pyproject.toml` file.
