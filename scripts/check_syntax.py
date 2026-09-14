#!/usr/bin/env python3
"""Compile every code cell and try every top-level import, without running
anything. Catches typos and missing packages before a model call ever happens.

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


def _strip_magics(src: str) -> str:
    return "\n".join("" if line.lstrip().startswith(MAGIC) else line for line in src.splitlines())


def main(argv: list[str]) -> int:
    prefix = argv[0] if argv else None
    problems, n = [], 0
    for nb_path in notebooks(prefix):
        n += 1
        rel = nb_path.relative_to(ROOT)
        nb = json.loads(nb_path.read_text(encoding="utf-8"))
        skip_imports = own_env(ROOT / rel.parts[0])
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
    print(f"✓ {n} notebook(s): every code cell compiles and every import resolves")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
