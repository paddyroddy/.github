# quarto

This action can be used in the following manner:

```yaml
jobs:
  build-and-deploy:
    permissions:
      contents: write
    runs-on: ubuntu-slim
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/github-pages/quarto@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

where `x` is the `major` version of the action. If Python dependencies are
required they can be specified via the `requirements-txt` input:

```yaml
jobs:
  build-and-deploy:
    permissions:
      contents: write
    runs-on: ubuntu-slim
    steps:
      # yamllint disable-line rule:line-length
      - uses: paddyroddy/.github/actions/github-pages/quarto@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          requirements-txt: ${{ github.workspace }}/requirements.txt
```

where `./requirements.txt` is the path to the `requirements.txt` file.
