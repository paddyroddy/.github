#!/usr/bin/env python
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve()


def main() -> int:
    cfg = HERE.parent / "python-hooks.yaml"
    result = subprocess.run(
        [
            "pre-commit",
            "run",
            "--config",
            f"{cfg}",
            "--files",
        ]
        + sys.argv[1:],
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    exit(main())
