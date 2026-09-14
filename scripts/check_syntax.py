#!/usr/bin/env python3
"""Compile every code cell, try every top-level import, and look for names a
cell uses but nothing defines, without running anything. Catches typos,
missing packages, and a missing import before a model call ever happens.

    python scripts/check_syntax.py            # every module
    python scripts/check_syntax.py 05         # one module
"""
from __future__ import annotations

import ast
import importlib.util
import json
import sys

from _common import ROOT, notebooks, own_env

MAGIC = ("%", "!")
# Names the kernel provides that no cell imports.
KERNEL_NAMES = {"display", "get_ipython", "_", "__", "___", "In", "Out", "exit", "quit"}


def _strip_magics(src: str) -> str:
    return "\n".join("" if line.lstrip().startswith(MAGIC) else line for line in src.splitlines())


def undefined_names(cells: list[str]) -> list[tuple[int, str]]:
    """(cell index, message) for every name used before anything defines it.

    The cells are checked as one script in notebook order, which is how a
    student runs them top to bottom. A NameError in cell 13 of a forty-minute
    notebook is the failure this exists to catch first.
    """
    from pyflakes import api as pyflakes_api, messages as pm

    starts, lines = [], []
    for src in cells:
        starts.append(len(lines) + 1)
        lines += _strip_magics(src).splitlines() or [""]
    found: list[tuple[int, str]] = []

    class _R:
        def unexpectedError(self, *a): pass
        def syntaxError(self, *a): pass
        def flake(self, m):
            if isinstance(m, pm.UndefinedName) and m.message_args[0] not in KERNEL_NAMES:
                k = max(i for i, st in enumerate(starts) if st <= m.lineno)
                found.append((k, f"'{m.message_args[0]}' is used but never defined or imported"))

    pyflakes_api.check("\n".join(lines) + "\n", "notebook", _R())
    return found


def main(argv: list[str]) -> int:
    prefix = argv[0] if argv else None
    problems, n = [], 0
    for nb_path in notebooks(prefix):
        n += 1
        rel = nb_path.relative_to(ROOT)
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
        skip_imports = own_env(ROOT / rel.parts[0])
        code = [(k, "".join(c.get("source", []))) for k, c in enumerate(nb.get("cells", [])) if c.get("cell_type") == "code"]
        try:
            for j, msg in undefined_names([src for _, src in code]):
                problems.append(f"{rel}[cell {code[j][0]}]: {msg}")
        except SyntaxError:
            pass    # reported per cell below
        for k, cell in enumerate(nb.get("cells", [])):
            if cell.get("cell_type") != "code":
                continue
            src = _strip_magics("".join(cell.get("source", [])))
            try:
                tree = ast.parse(src)
            except SyntaxError as e:
                problems.append(f"{rel}[cell {k}]: syntax error line {e.lineno}: {e.msg}")
                continue
            if skip_imports:
                continue
            for node in tree.body:
                names = []
                if isinstance(node, ast.Import):
                    names = [a.name.split(".")[0] for a in node.names]
                elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                    names = [node.module.split(".")[0]]
                for name in names:
                    if name == "helpers":
                        continue
                    if importlib.util.find_spec(name) is None:
                        problems.append(f"{rel}[cell {k}]: cannot import '{name}' in the root environment")
    for p in problems:
        print(f"✗ {p}")
    if problems:
        print(f"\n{len(problems)} problem(s) across {n} notebook(s)")
        return 1
    print(f"✓ {n} notebook(s): every code cell compiles, every import resolves, every name is defined")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
