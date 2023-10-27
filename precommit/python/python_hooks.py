#!/usr/bin/env python
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve()

sys.path.append(str(HERE.parents[1]))

from _run_hooks import run_hooks  # noqa: E402


def main() -> int:
    return run_hooks(pathlib.Path("python/python-hooks.yml"))


if __name__ == "__main__":
    sys.exit(main())
