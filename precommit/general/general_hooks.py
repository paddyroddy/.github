#!/usr/bin/env python
"""General pre-commit hooks."""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve()

sys.path.append(str(HERE.parents[1]))

from _run_hooks import run_hooks  # noqa: E402


def main() -> int:
    """
    Run the general pre-commit hooks.

    Returns
        The return code of the process
    """
    return run_hooks(pathlib.Path("general/general-hooks.yml"))


if __name__ == "__main__":
    sys.exit(main())
