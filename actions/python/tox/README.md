# tox

This action can be used in the following manner:

```yaml
jobs:
  test:
    name: ${{ matrix.os }} py${{ matrix.python-version }}
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os:
          - macos-latest
          - ubuntu-latest
          - windows-latest
        python-version:
          - "3.x"
    steps:
      - uses: paddyroddy/.github/actions/python/tox@vx
        with:
          cache-path: |-
            .tox
          operating-system: ${{ matrix.os }}
          pyproject-toml: ./pyproject.toml
          python-version: ${{ matrix.python-version }}
```

where `x` is the `major` version of the action. If coverage with
Coveralls is not desired, then modify the above to:

```yaml
jobs:
  test:
    name: ${{ matrix.os }} py${{ matrix.python-version }}
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os:
          - macos-latest
          - ubuntu-latest
          - windows-latest
        python-version:
          - "3.x"
    steps:
      - uses: paddyroddy/.github/actions/python/tox@vx
        with:
          cache-path: |-
            .tox
          coverage-with-coveralls: no
          operating-system: ${{ matrix.os }}
          pyproject-toml: ./pyproject.toml
          python-version: ${{ matrix.python-version }}
```
