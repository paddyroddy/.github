# LaTeX pre-commit config

In a repository that requires [pre-commit](https://pre-commit.com), simply add
a file called `.pre-commit-config.yaml` with the following code.

```yaml
repos:
  - repo: https://github.com/paddyroddy/.github
    rev: v0.1.0
    hooks:
      - id: latex-hooks
```

Then run `pre-commit install; pre-commit autoupdate`.
