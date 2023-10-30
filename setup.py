import setuptools


setuptools.setup(
    entry_points={
        "console_scripts": [
            "latex-hooks = precommit.latex.latex_hooks:main",
            "python-hooks = precommit.python.python_hooks:main",
        ]
    },
    name="pre_commit_placeholder_package",
    packages=setuptools.find_packages("precommit"),
    version="0.0.0",
)
