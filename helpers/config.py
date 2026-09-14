"""Configuration every notebook shares.

Loads the repository-root `.env` no matter which module folder you run from,
then exposes endpoints, model names, tuning, paths, and the cohort overlay.
Nothing here is hard-coded per notebook: if you want a different timeout, a
different reasoning budget, or a different model, change `.env`.

    from helpers.config import LLM_MODEL, require
    require("OPENAI_API_KEY")          # fail early, with a clear message
"""
from __future__ import annotations

import os
import tomllib
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent

# The repo `.env` wins over a stale shell value, with one exception that matters:
# a blank line in `.env` means "unset, use the default", so it must never erase a
# value the caller exported on purpose. `make seed` and `check_execute.py` both
# pass TE_WORKSPACE that way, and without this they silently wrote to the wrong
# workspace and the run looked green while producing nothing.
_exported = {k: v for k, v in os.environ.items() if v.strip()}
load_dotenv(ROOT / ".env", override=True)
load_dotenv(override=False)                 # a local .env may fill gaps
for _k, _v in _exported.items():
    if not os.environ.get(_k, "").strip():
        os.environ[_k] = _v

DATA = ROOT / "data"
SEED = DATA / "seed"
IMAGES = ROOT / "images"
PROJECT = ROOT / "project"


# ── readers ──────────────────────────────────────────────────────────────────

def _str(name: str, default: str | None = None) -> str | None:
    """An environment value, or the default. Blank and unset mean the same."""
    v = os.environ.get(name)
    v = v.strip() if v else ""
    return v or default


def _num(name: str, default: float | None) -> float | None:
    v = _str(name)
    if v is None:
        return default
    try:
        return float(v)
    except ValueError:
        raise RuntimeError(f"{name} in .env must be a number, not {v!r}") from None


def _int(name: str, default: int | None) -> int | None:
    v = _num(name, default)
    return None if v is None else int(v)


def _bool(name: str, default: bool = False) -> bool:
    v = _str(name)
    return default if v is None else v.lower() in {"1", "true", "yes", "on"}


# ── endpoints and models ─────────────────────────────────────────────────────

# Any non-empty key works against an open self-hosted server.
KEY = _str("OPENAI_API_KEY") or _str("ANTHROPIC_API_KEY") or "EMPTY"

LLM_MODEL = _str("LLM_MODEL", "gpt-4.1-mini")
LLM_BASE = _str("OPENAI_BASE_URL")          # None means the provider default

EMBED_MODEL = _str("EMBED_MODEL", "text-embedding-3-small")
EMBED_BASE = _str("EMBED_BASE_URL", LLM_BASE)

JUDGE_MODEL = _str("JUDGE_MODEL", LLM_MODEL)

RAGAS_MODEL = _str("RAGAS_MODEL", LLM_MODEL)
RAGAS_BASE = _str("RAGAS_BASE_URL", LLM_BASE)
SDG_MODEL = _str("SDG_MODEL", RAGAS_MODEL)

TAVILY_KEY = _str("TAVILY_API_KEY")
COHERE_KEY = _str("COHERE_API_KEY")

# ── tuning ───────────────────────────────────────────────────────────────────
# These are the numbers that used to be scattered through the notebooks.

LLM_TIMEOUT = _num("LLM_TIMEOUT", 600.0)            # seconds; generous by default
LLM_MAX_RETRIES = _int("LLM_MAX_RETRIES", 3)
LLM_TEMPERATURE = _num("LLM_TEMPERATURE", None)     # None means do not send one
JUDGE_TEMPERATURE = _num("JUDGE_TEMPERATURE", 0.0)  # judges want determinism
# Empty means no cap, which is what a reasoning model needs: a cap truncates it
# mid-thought. Set it only if your provider bills by the token and you must.
LLM_MAX_TOKENS = _int("LLM_MAX_TOKENS", None)
# low | medium | high, or empty to send nothing. Ignored by models without it.
LLM_REASONING_EFFORT = _str("LLM_REASONING_EFFORT")

EMBED_TIMEOUT = _num("EMBED_TIMEOUT", LLM_TIMEOUT)
EMBED_BATCH = _int("EMBED_BATCH", 64)

STT_BASE = _str("STT_BASE")
STT_MODEL = _str("STT_MODEL")
TTS_BASE = _str("TTS_BASE")
TTS_MODEL = _str("TTS_MODEL")
TTS_KEY = _str("TTS_KEY")

# ── workspace ────────────────────────────────────────────────────────────────

SEED_MODE = _bool("TE_SEED_MODE")


def _load_cohort() -> dict:
    path = ROOT / "cohort.toml"
    if not path.exists():
        return {"cohort": {"id": "dev", "name": "Cohort", "client": "", "city": "",
                           "groups": 8, "repo": ""}, "banner": {"show_client": False}}
    with path.open("rb") as fh:
        return tomllib.load(fh)


COHORT = _load_cohort()


def require(*names: str) -> None:
    """Assert the named environment variables are set, with a copy-pasteable hint."""
    missing = [n for n in names if not _str(n)]
    if missing:
        raise RuntimeError(
            f"Missing in your .env: {', '.join(missing)}. "
            f"Copy .env.template to .env at the repository root and fill it in."
        )


def budget(normal: int, seed: int | None = None) -> int:
    """Pick a loop budget: the normal value, or a smaller one in seed mode."""
    if SEED_MODE:
        return seed if seed is not None else max(1, normal // 4)
    return normal


def summary() -> str:
    """One line naming the endpoint and the tuning in force. Notebooks print this."""
    where = LLM_BASE or "provider default"
    effort = LLM_REASONING_EFFORT or "unset"
    cap = LLM_MAX_TOKENS or "no cap"
    return (f"{LLM_MODEL} at {where} · timeout {LLM_TIMEOUT:.0f}s · "
            f"retries {LLM_MAX_RETRIES} · reasoning {effort} · tokens {cap}")
