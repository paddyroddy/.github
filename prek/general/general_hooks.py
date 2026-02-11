"""General prek hooks."""

import pathlib
import sys

HERE = pathlib.Path(__file__).resolve()

sys.path.append(str(HERE.parents[1]))

from _run_hooks import run_hooks  # noqa: E402


def main() -> int:
    """
    Run the general prek hooks.

    Returns
        The return code of the process
    """
    return run_hooks(HERE.parent / "general-hooks.yaml")


if __name__ == "__main__":
    sys.exit(main())
