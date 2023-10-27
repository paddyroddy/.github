#!/usr/bin/env python
import pathlib
import subprocess
import sys
import argparse

HERE = pathlib.Path(__file__).resolve()


def main(hooks_path: pathlib.Path) -> int:
    cfg = HERE.parent / f"{hooks_path}.yml"
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
    parser = argparse.ArgumentParser(description="pre-commit hooks")
    parser.add_argument(
        "pre_commit_hook",
        type=str,
        help="path to the desired pre-commit hook",
    )
    args = parser.parse_args()
    exit(main(pathlib.Path(args.pre_commit_hook)))
