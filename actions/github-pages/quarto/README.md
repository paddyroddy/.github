# quarto

This action can be used in the following manner:

```yaml
jobs:
  build-and-deploy:
    runs-on: ubuntu-slim
    permissions:
      contents: write
    steps:
      - uses: paddyroddy/.github/actions/github-pages/quarto@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

where `x` is the `major` version of the action. If Python dependencies are
required they can be specified via the `requirements-txt` input:

```yaml
jobs:
  build-and-deploy:
    runs-on: ubuntu-slim
    permissions:
      contents: write
    steps:
      - uses: paddyroddy/.github/actions/github-pages/quarto@vx
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          requirements-txt: ./requirements.txt
```

where `./requirements.txt` is the path to the `requirements.txt` file.
