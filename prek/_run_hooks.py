import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve()


def run_hooks(hooks_path: pathlib.Path) -> int:
    """
    Run prek using the specified config.

    Args:
        hooks_path: The Path object of the hooks

    Returns:
        The return code of the process
    """
    # Debug: write to a file
    with open("/tmp/prek_debug.txt", "w") as f:
        f.write(f"sys.argv = {sys.argv}\n")
        f.write(f"hooks_path = {hooks_path}\n")
    
    cmd = [
        "prek",
        "run",
        "--config",
        str(hooks_path),
    ]
    
    if sys.argv[1:]:
        cmd.extend(["--files", *sys.argv[1:]])
    else:
        cmd.append("--all-files")
    
    with open("/tmp/prek_debug.txt", "a") as f:
        f.write(f"cmd = {cmd}\n")
    
    return subprocess.run(cmd, check=False).returncode  # noqa: S603