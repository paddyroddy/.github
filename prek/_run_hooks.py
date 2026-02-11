import pathlib
import subprocess
import sys
import os
import shlex

HERE = pathlib.Path(__file__).resolve()


def run_hooks(hooks_path: pathlib.Path) -> int:
    """
    Run prek using the specified config.

    Args:
        hooks_path: The Path object of the hooks

    Returns:
        The return code of the process
    """
    cmd_parts = [
        "prek",
        "run",
        "--config",
        str(hooks_path),
    ]
    
    if sys.argv[1:]:
        cmd_parts.extend(["--files", *sys.argv[1:]])
    else:
        cmd_parts.append("--all-files")
    
    # Join into a shell command
    cmd = " ".join(shlex.quote(part) for part in cmd_parts)
    
    return subprocess.run(cmd, check=False, cwd=os.getcwd(), shell=True).returncode  # noqa: S602