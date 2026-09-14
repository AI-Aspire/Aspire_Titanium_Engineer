#!/usr/bin/env python3
"""Every third-party import in a notebook must be declared in a pyproject.

Catches the failure where a notebook works on the author's machine because some
other package happened to pull the import in, and then fails for a student on a
clean install. Maps the imported module to the distribution that provides it,
then checks that distribution is declared: in the root `pyproject.toml`, in one
of its dependency groups, or in the module's own `pyproject.toml`.

    python scripts/check_deps.py            # every module
    python scripts/check_deps.py --list     # print what each module imports
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
import tomllib
from collections import defaultdict
from importlib.metadata import packages_distributions

from _common import ROOT, config, modules, notebooks

STDLIB = set(sys.stdlib_module_names)
LOCAL = {"helpers", "src", "lib", "skills", "advanced", "eval_lookup", "mcp_server", "agent"}


def declared() -> tuple[dict[str, str], dict[str, set[str]]]:
    """Distribution name -> where it is declared, and module -> its own deps."""
    def names(spec: str) -> str:
        return re.split(r"[<>=!\[;~ ]", spec.strip(), 1)[0].lower().replace("_", "-")

    with (ROOT / "pyproject.toml").open("rb") as fh:
        root_cfg = tomllib.load(fh)
    where: dict[str, str] = {}
    for spec in root_cfg.get("project", {}).get("dependencies", []):
        where[names(spec)] = "root"
    for group, specs in root_cfg.get("dependency-groups", {}).items():
        for spec in specs:
            where.setdefault(names(spec), f"group:{group}")

    own: dict[str, set[str]] = {}
    for m in modules():
        p = m / "pyproject.toml"
        if not p.exists():
            continue
        with p.open("rb") as fh:
            cfg = tomllib.load(fh)
        own[m.name] = {names(s) for s in cfg.get("project", {}).get("dependencies", [])}
    return where, own


def imports_of(path) -> set[str]:
    """Top-level module names imported by a notebook's code cells."""
    nb = json.loads(path.read_text(encoding="utf-8"))
    found: set[str] = set()
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        src = "\n".join("" if l.lstrip().startswith(("%", "!")) else l
                        for l in "".join(cell.get("source", [])).splitlines())
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                found |= {a.name.split(".")[0] for a in node.names}
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                found.add(node.module.split(".")[0])
    return {m for m in found if m not in STDLIB and m not in LOCAL}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    args = ap.parse_args(argv)

    provides = packages_distributions()      # import name -> [distribution, ...]
    where, own = declared()
    own_env = set(config().get("own_env", []))

    problems: list[str] = []
    per_module: dict[str, set[str]] = defaultdict(set)
    for nb in notebooks():
        module = nb.relative_to(ROOT).parts[0]
        per_module[module] |= imports_of(nb)

    for module, mods in sorted(per_module.items()):
        for imp in sorted(mods):
            dists = provides.get(imp)
            if not dists:
                # Not installed in this environment. Declared is what matters: an
                # optional group or a module's own env may simply not be synced
                # right now. Fall back to matching the import name itself.
                guess = imp.lower().replace("_", "-")
                if module in own_env or guess in where or guess in own.get(module, set()):
                    continue
                problems.append(f"{module}: imports '{imp}', which is neither installed nor declared")
                continue
            # A namespace such as `langgraph` is provided by several distributions
            # (langgraph, langgraph-checkpoint, ...) and their order differs by
            # platform, so declaring any one of them satisfies the import.
            names = [d.lower().replace("_", "-") for d in dists]
            dist = names[0]
            if module in own_env:
                if not any(n in own.get(module, set()) or n in where for n in names):
                    problems.append(f"{module}: imports '{imp}' ({dist}), not in {module}/pyproject.toml")
            elif not any(n in where for n in names):
                problems.append(f"{module}: imports '{imp}' ({dist}), not declared in pyproject.toml")

    if args.list:
        for module, mods in sorted(per_module.items()):
            print(f"\n{module}")
            for imp in sorted(mods):
                d = (provides.get(imp) or ["?"])[0]
                print(f"  {imp:<24} {d:<24} {where.get(d.lower().replace('_','-'), '—')}")

    for p in problems:
        print(f"✗ {p}")
    if problems:
        print(f"\n{len(problems)} undeclared dependency problem(s)")
        return 1
    print(f"✓ every import across {len(per_module)} modules is declared")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
