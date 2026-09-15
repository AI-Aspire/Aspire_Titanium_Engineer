"""The one capability, as plain Python: look up an eval case or a trajectory.

Shared by the MCP server and the skill script so that every mechanism in the
notebook answers from the same data. The notebook itself defines the same
functions inline, so students can read them next to the loop that calls them.
"""
from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from helpers import workspace as ws  # noqa: E402

STOP = {"a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how", "i", "in", "is", "it", "of",
        "on", "or", "our", "should", "that", "the", "their", "to", "what", "when", "with", "my", "can", "do",
        "does", "this", "you", "your", "me", "we", "not", "but", "if", "so", "was", "will", "have", "has"}

CASES = ws.load("eval_cases", quiet=True)
TRAJECTORIES = ws.load("trajectories", quiet=True)
CASE_BY_ID = {str(c["id"]): c for c in CASES}
TRAJ_BY_ID = {str(t["id"]): t for t in TRAJECTORIES}


def terms(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9][a-z0-9-]+", text.lower()) if t not in STOP}


def trajectory_view(t: dict) -> dict:
    steps = t.get("steps", [])
    return {"trajectory": t["id"], "task_id": t.get("task_id"), "passed": bool(t.get("passed")),
            "tools": [s.get("name") for s in steps if s.get("role") == "tool"],
            "final": next((s.get("content", "") for s in reversed(steps) if s.get("role") == "assistant"), "")}


def case_view(c: dict) -> dict:
    runs = [t for t in TRAJECTORIES if str(t.get("task_id", "")).endswith(str(c["id"]))]
    return {"case": c["id"], "question": c["question"], "reference": c.get("reference", ""),
            "runs": [{"trajectory": t["id"], "passed": bool(t.get("passed"))} for t in runs]}


def get_case(case_id: str) -> dict | None:
    c = CASE_BY_ID.get(str(case_id).strip())
    return case_view(c) if c else None


def get_trajectory(trajectory_id: str) -> dict | None:
    t = TRAJ_BY_ID.get(str(trajectory_id).strip())
    return trajectory_view(t) if t else None


def search_cases(query: str, k: int = 3) -> list[dict]:
    q = terms(query)
    ranked = sorted(CASES, key=lambda c: len(q & terms(c["question"] + " " + c.get("reference", ""))), reverse=True)
    return [{"case": c["id"], "question": c["question"], "reference": textwrap.shorten(c.get("reference", ""), 200)}
            for c in ranked[:k] if q & terms(c["question"] + " " + c.get("reference", ""))]


def lookup(query: str) -> dict | list:
    """By id first, then by the words in the question."""
    q = query.strip()
    return get_case(q) or get_trajectory(q) or search_cases(q)
