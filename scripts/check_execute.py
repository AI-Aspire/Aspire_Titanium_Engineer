#!/usr/bin/env python3
"""Run notebooks for real. Minutes, not seconds, and it costs model calls, so
it is never part of `make check`.

    python scripts/check_execute.py            # every module, in order, in Jupyter
    python scripts/check_execute.py 05         # one module
    python scripts/check_execute.py --offline  # only modules that need no key
    python scripts/check_execute.py --save     # write outputs back (then: make scrub)
    python scripts/check_execute.py --marimo   # run the .py mirrors instead

A student opens either the notebook or its marimo mirror, so both have to run.
The two differ in working directory and in execution order, which is exactly
where a notebook breaks, so `--marimo` is not redundant with the default pass.

Modules listed in [tool.titanium].own_env run inside their own uv project.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from _common import ROOT, config, notebooks, own_env


_ANSI = re.compile(r"\x1b\[[0-9;]*m")
_NOISE = ("IPKernelApp", "warnings.warn", "DeprecationWarning", "UserWarning",
          "Kernel is running over TCP", "to enable transport encryption")


def _child_error(blob: str) -> str:
    """The real failure from a child run, not the last line of noise.

    The child prints its own `✗ <path>: <error>` line. Falling back to the last
    line of combined output picked up a kernel TCP warning instead, which cost
    an afternoon of debugging the wrong thing.
    """
    lines = [l.rstrip() for l in (blob or "").splitlines() if l.strip()]
    for line in reversed(lines):
        if line.startswith("✗ ") and ": " in line:
            return line.split(": ", 1)[1][:400]
    for line in reversed(lines):
        if not any(n in line for n in _NOISE):
            return line[:400]
    return "failed with no message"


def run_marimo(nb: Path, *, timeout: int) -> tuple[bool, str]:
    """Execute the marimo mirror by exporting it, which runs every cell.

    Runs from the repository root, the way a student who typed
    `marimo edit <path>` there would, so a notebook that assumes its own
    directory is the working directory fails here and only here.
    """
    py = nb.with_suffix(".py")
    if not py.exists():
        return False, "no marimo mirror; run: make marimo"
    with tempfile.TemporaryDirectory() as td:
        out = Path(td) / "out.html"
        r = subprocess.run(
            [sys.executable, "-m", "marimo", "export", "html", str(py), "-o", str(out), "--no-sandbox", "-f"],
            cwd=ROOT, text=True, capture_output=True, timeout=timeout,
        )
    blob = (r.stdout or "") + (r.stderr or "")
    if "some cells failed to execute" in blob or "MarimoExceptionRaised" in blob:
        line = next((l for l in blob.splitlines() if "Error" in l or "Raised" in l), "a cell failed")
        return False, line.strip()[:200]
    if r.returncode != 0:
        return False, blob.strip().splitlines()[-1][:200] if blob.strip() else f"exit {r.returncode}"
    return True, ""


def _say(msg: str) -> None:
    """Progress on stderr, flushed, so a log being tailed shows where a run is."""
    print(f"  [{time.strftime('%H:%M:%S')}] {msg}", file=sys.stderr, flush=True)


def _stderr_of(cell) -> str:
    return "".join(o.get("text", "") for o in cell.get("outputs", [])
                   if o.get("output_type") == "stream" and o.get("name") == "stderr")


def run_one(nb: Path, *, save: bool, timeout: int) -> tuple[bool, str]:
    import nbformat
    from nbclient import NotebookClient

    doc = nbformat.read(nb, as_version=4)
    total = sum(1 for c in doc.cells if c.cell_type == "code")
    started: dict[int, float] = {}
    label = nb.relative_to(ROOT) if nb.is_relative_to(ROOT) else nb

    # A long run must say which cell it is on and what the kernel wrote to
    # stderr, as it happens. Without this, a notebook that retried a call
    # for an hour looked the same from outside as one making progress.
    def on_start(cell, cell_index):
        if cell.cell_type == "code":
            started[cell_index] = time.time()
            first = next((l for l in cell.source.splitlines() if l.strip() and not l.startswith("#")), "")
            _say(f"{label} cell {cell_index} start: {first[:70]}")

    def on_done(cell, cell_index, execute_reply):
        if cell.cell_type == "code":
            _say(f"{label} cell {cell_index} done in {time.time() - started.get(cell_index, time.time()):0.0f}s")
            for line in _stderr_of(cell).splitlines():
                if line.strip() and not any(n in line for n in _NOISE):
                    _say(f"    stderr: {line[:160]}")

    def on_error(cell, cell_index, execute_reply):
        for o in cell.get("outputs", []):
            if o.get("output_type") == "error":
                _say(f"{label} cell {cell_index} ERROR {o.get('ename')}: {str(o.get('evalue', ''))[:1200]}")
                # The frames nearest the failure, so a validation error names
                # the field and a library error names the call.
                frames = [_ANSI.sub("", l) for l in o.get("traceback", [])]
                for line in "\n".join(frames).splitlines()[-14:]:
                    if line.strip():
                        _say(f"    | {line[:200]}")

    client = NotebookClient(doc, timeout=timeout, kernel_name="python3",
                            resources={"metadata": {"path": str(nb.parent)}}, allow_errors=False,
                            on_cell_start=on_start, on_cell_executed=on_done, on_cell_error=on_error)
    _say(f"{label}: {total} code cells")
    try:
        client.execute()
    except Exception as e:  # noqa: BLE001
        return False, str(e).splitlines()[-1][:200] if str(e) else type(e).__name__
    if save:
        nbformat.write(doc, nb)
    return True, ""


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("prefix", nargs="?")
    ap.add_argument("--offline", action="store_true")
    ap.add_argument("--save", action="store_true")
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--marimo", action="store_true", help="run the .py mirrors instead of the notebooks")
    ap.add_argument("--single", help="internal: run one notebook path in this interpreter")
    args = ap.parse_args(argv)

    if args.single:
        ok, err = run_one(Path(args.single), save=args.save, timeout=args.timeout)
        print(("✓ " if ok else "✗ ") + args.single + ("" if ok else f": {err}"))
        return 0 if ok else 1

    offline = set(config().get("offline", []))
    failures, n = [], 0
    for nb in notebooks(args.prefix):
        module = nb.relative_to(ROOT).parts[0]
        if args.offline and module not in offline:
            continue
        n += 1
        t0 = time.time()
        mdir = ROOT / module
        if args.marimo:
            ok, err = run_marimo(nb, timeout=args.timeout)
        elif own_env(mdir):
            cmd = ["uv", "run", "--project", str(mdir), "python", str(ROOT / "scripts/check_execute.py"),
                   "--single", str(nb), "--timeout", str(args.timeout)] + (["--save"] if args.save else [])
            # Stream the child's output as it comes, and keep a copy for the
            # verdict; capturing it all would hide an hour of progress lines.
            proc = subprocess.Popen(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            lines = []
            for line in proc.stdout:
                lines.append(line)
                if line.startswith("  ["):
                    print(line, end="", file=sys.stderr, flush=True)
            ok = proc.wait() == 0
            err = _child_error("".join(lines))
        else:
            ok, err = run_one(nb, save=args.save, timeout=args.timeout)
        secs = time.time() - t0
        fmt = "marimo" if args.marimo else "jupyter"
        print(f"{'✓' if ok else '✗'} [{fmt}] {nb.relative_to(ROOT)} ({secs:0.0f}s){'' if ok else ': ' + err}")
        if not ok:
            failures.append(nb)
    if failures:
        print(f"\n✗ {len(failures)} of {n} notebook(s) failed")
        return 1
    print(f"✓ {n} notebook(s) executed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
