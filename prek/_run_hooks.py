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
    
    with open("/tmp/prek_shell_debug.txt", "w") as f:
        f.write(f"Shell command: {cmd}\n")
        f.write(f"cwd: {os.getcwd()}\n")
    
    result = subprocess.run(cmd, check=False, cwd=os.getcwd(), shell=True)  # noqa: S602
    
    with open("/tmp/prek_shell_debug.txt", "a") as f:
        f.write(f"returncode: {result.returncode}\n")
    
    return result.returncode