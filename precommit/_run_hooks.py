import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve()


def run_hooks(hooks_path: pathlib.Path) -> int:
    """
    Run pre-commit using the specified config.

    Args:
        hooks_path: The Path object of the hooks
    Returns:
        The return code of the process

    """
    cfg = HERE.parent / hooks_path
    result = subprocess.run(
        [  # noqa: S603
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
