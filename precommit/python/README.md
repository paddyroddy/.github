# Python pre-commit config

In a repository that requires [pre-commit](https://pre-commit.com), simply add
a file called `.pre-commit-config.yaml` with the following code.

```yaml
repos:
  - repo: https://github.com/paddyroddy/.github
    rev: vx.y.z
    hooks:
      - id: python-hooks
```

where `x.y.z` is the `major.minor.patch` version of the action. Then run
`pre-commit install`.
