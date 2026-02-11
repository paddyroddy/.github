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
    cmd = [
        "prek",
        "run",
        "--config",
        str(hooks_path),
    ]

    # only pass the files if they were given
    if len(sys.argv) > 1:
        cmd += ["--files", *sys.argv[1:]]

    return subprocess.run(cmd, check=False).returncode  # noqa: S603
