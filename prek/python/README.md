# Python prek config

In a repository that requires [prek](https://github.com/j178/prek), simply add a
file called `.pre-commit-config.yaml` with the following code.

```yaml
repos:
  - repo: https://github.com/paddyroddy/.github
    rev: v0.1.0
    hooks:
      - id: python-hooks
```

Then run `prek install; prek autoupdate`.
