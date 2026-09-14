#!/usr/bin/env python3
"""Validate the workspace (or the seed) against the artifact contract.

    python scripts/check_workspace.py --day 2        # everything produced on days 1-2
    python scripts/check_workspace.py --seed         # the committed seed, all days
    python scripts/check_workspace.py --seed --day 1
    python scripts/check_workspace.py --seed --through 07   # producers up to module 07
    python scripts/check_workspace.py --seed --landed       # producers whose folder is in the checkout
    python scripts/check_workspace.py --status       # print where each artifact comes from
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys

from _common import ROOT
sys.path.insert(0, str(ROOT))

from helpers import workspace as ws  # noqa: E402


def _landed_modules() -> set[str]:
    """Module ids whose folder git tracks; every folder present, outside git.

    An author's checkout holds folders that have not landed yet, so presence
    on disk is not enough there; in CI and in a fresh clone the two agree.
    """
    try:
        out = subprocess.run(["git", "ls-files", "--", "[0-9][0-9]_*"], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout
        tracked = {line.split("/", 1)[0][:2] for line in out.splitlines() if "/" in line}
        if tracked:
            return tracked
    except (OSError, subprocess.CalledProcessError):
        pass
    return {p.name[:2] for p in ROOT.glob("[0-9][0-9]_*") if p.is_dir()}


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--day", type=int, default=5)
    ap.add_argument("--seed", action="store_true", help="validate data/seed/ instead of the workspace")
    ap.add_argument("--through", metavar="NN",
                    help="only artifacts written by modules up to this one, in course order")
    ap.add_argument("--landed", action="store_true",
                    help="only artifacts written by modules whose folder git tracks (or exists, outside git)")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args(argv)
    if args.seed:
        os.environ["TE_WORKSPACE"] = str(ws.seed_root())
    if args.status:
        ws.status()
        return 0
    base = ws.root()
    order = [m for d in sorted(ws.DAYS) for m in ws.DAYS[d]]
    if args.landed:
        # Modules land one at a time, each once its notebook has run green.
        # A module that is in the checkout must have produced its artifacts;
        # one that is not yet cannot be asked for them.
        wanted = {m for m in order if m in _landed_modules()}
        scope = f"for the {len(wanted)} landed module(s)"
    elif args.through:
        if args.through not in order:
            ap.error(f"--through must be one of {order}")
        wanted = set(order[: order.index(args.through) + 1])
        scope = f"through module {args.through}"
    else:
        wanted = {m for d, mods in ws.DAYS.items() if d <= args.day for m in mods}
        scope = f"through day {args.day}"
    problems, ok = [], 0
    for name, art in ws.SCHEMA.items():
        if art.producer not in wanted:
            continue
        p = base / art.path
        if not ws._present(p, art.fmt):
            problems.append(f"{name}: missing ({art.path}; written by module {art.producer})")
            continue
        try:
            data = ws._read(p, art.fmt)
        except Exception as e:  # noqa: BLE001
            problems.append(f"{name}: unreadable ({e})")
            continue
        bad = ws.validate(name, data)
        if bad:
            problems.append(f"{name}: " + "; ".join(bad))
        else:
            ok += 1
    label = "seed" if args.seed else "workspace"
    for pr in problems:
        print(f"✗ {pr}")
    if problems:
        print(f"\n{len(problems)} problem(s) in the {label} {scope}; {ok} artifact(s) valid.")
        return 1
    print(f"✓ {label} valid {scope}: {ok} artifact(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
