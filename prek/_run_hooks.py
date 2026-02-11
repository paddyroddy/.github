import pathlib
import subprocess
import sys
import os

HERE = pathlib.Path(__file__).resolve()


def run_hooks(hooks_path: pathlib.Path) -> int:
    """
    Run prek using the specified config.

    Args:
        hooks_path: The Path object of the hooks

    Returns:
        The return code of the process
    """
    # Always use --all-files for simplicity
    cmd = [
        "prek",
        "run",
        "--config",
        str(hooks_path),
        "--all-files",
    ]
    
    return subprocess.run(cmd, check=False, cwd=os.getcwd()).returncode  # noqa: S603