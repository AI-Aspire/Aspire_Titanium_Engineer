"""Where a notebook's own files are, in Jupyter and in marimo alike.

Jupyter runs a notebook with its folder as the working directory. marimo runs
it from wherever `marimo edit` was typed, usually the repository root, and
sets `__file__` to the mirror. A notebook that opens a file beside itself
with a bare relative path therefore works in one and not the other.
"""
from __future__ import annotations

import inspect
from pathlib import Path

_HELPERS = Path(__file__).resolve().parent


def module_dir(_frame=None) -> Path:
    """The folder of the notebook that calls this.

    marimo is asked first; failing that, the caller's `__file__` (a script
    or a test); failing that, the working directory, which is what Jupyter
    sets to the notebook's folder. Only the direct caller is inspected: the
    frames behind a Jupyter cell belong to the kernel and carry its files.
    """
    try:
        import marimo as mo

        if mo.running_in_notebook():
            d = mo.notebook_dir()
            if d:
                return Path(d)
    except Exception:  # noqa: BLE001  not installed, or not running under marimo
        pass
    frame = _frame or inspect.currentframe().f_back
    f = frame.f_globals.get("__file__") if frame else None
    if f and not Path(f).resolve().is_relative_to(_HELPERS):
        return Path(f).resolve().parent
    return Path.cwd()


def local(*parts: str) -> Path:
    """A path beside the notebook: `local("data", "trace.npz")`."""
    return module_dir(inspect.currentframe().f_back).joinpath(*parts)
