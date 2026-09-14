"""Synthetic data generation: a small fix around RAGAS's test set generator.

RAGAS asks the model which persona each question is for, then looks the
reply up by exact name. A model that answers "Jordan Hayes (Software
Engineer)" for a persona called "Jordan Hayes" turns a forty-minute run into
a KeyError at the end. `tolerant_personas()` makes that lookup forgiving.

Nothing here imports ragas at module load, so the root environment (which
does not have ragas) can import and test the matcher.
"""
from __future__ import annotations

import difflib
import re


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().casefold()


def match_persona(key: str, names: list[str], *, cutoff: float = 0.6) -> str | None:
    """The persona name that `key` most plausibly refers to, or None.

    Tried in order: exact; case and spacing; one name contained in the other
    (the model decorated the name with a role, or dropped part of it); the
    closest name by character overlap at or above `cutoff` (a typo).
    """
    if key in names:
        return key
    k = _norm(key)
    by_norm = {_norm(n): n for n in names}
    if k in by_norm:
        return by_norm[k]
    contained = [n for n in names if _norm(n) in k or k in _norm(n)]
    if contained:
        return max(contained, key=len)
    best = difflib.get_close_matches(k, list(by_norm), n=1, cutoff=cutoff)
    return by_norm[best[0]] if best else None


def _tolerant_getitem(self, key: str):
    names = [p.name for p in self.personas]
    hit = match_persona(key, names)
    if hit is None:
        raise KeyError(f"No persona found with name '{key}' (the personas are {names})")
    return next(p for p in self.personas if p.name == hit)


def tolerant_personas() -> None:
    """Make RAGAS resolve an inexact persona name to the closest persona.

    Idempotent. Call once before generating a test set. Imports ragas here,
    not at module load, so this module stays importable without it.
    """
    from ragas.testset.persona import PersonaList

    if PersonaList.__getitem__ is not _tolerant_getitem:
        PersonaList.__getitem__ = _tolerant_getitem
