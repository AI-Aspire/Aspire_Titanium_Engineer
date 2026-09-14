"""Shared bits for the scripts: repo root, module discovery, UTF-8 output."""
from __future__ import annotations

import re
import sys
import tomllib
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
MODULE_RE = re.compile(r"^(\d{2})_[A-Za-z]")


def config() -> dict:
    with (ROOT / "pyproject.toml").open("rb") as fh:
        return tomllib.load(fh).get("tool", {}).get("titanium", {})


def modules() -> list[Path]:
    """Numbered module directories, in order."""
    return sorted(p for p in ROOT.iterdir() if p.is_dir() and MODULE_RE.match(p.name))


def notebooks(prefix: str | None = None) -> list[Path]:
    """Every source notebook, optionally filtered by module prefix ("05" or "05_RAG")."""
    out = []
    for m in modules():
        if prefix and not m.name.startswith(prefix):
            continue
        out += sorted(p for p in m.rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts)
    return out


def own_env(module: Path) -> bool:
    return module.name in set(config().get("own_env", [])) and (module / "pyproject.toml").exists()
