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

    if sys.argv[1:]:
        cmd.extend(["--files", *sys.argv[1:]])
    else:
        cmd.append("--all-files")

    return subprocess.run(  # noqa: S603
        cmd,
        check=False,
        cwd=pathlib.Path.cwd(),
    ).returncode
