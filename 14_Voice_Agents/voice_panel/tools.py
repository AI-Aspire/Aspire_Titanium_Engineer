"""The researchers' tools: search and fetch over your workspace corpus, plus web
search when a Tavily key is set.

    search(q)        -> ranked corpus pages (title, path, snippet, score)
    fetch(path)      -> one page's text
    web_search(q)    -> Tavily results, or [] when TAVILY_API_KEY is not set

The corpus is whatever `helpers.workspace` resolves: the cohort's own pages when
they exist, the seed example otherwise. Nothing here writes to disk.
"""
from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path

import httpx

_REPO = Path(__file__).resolve().parents[2]
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from helpers import workspace as ws  # noqa: E402
from helpers.config import TAVILY_KEY  # noqa: E402

STOP = {"a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how", "i", "in", "is", "it",
        "of", "on", "or", "our", "should", "that", "the", "their", "to", "what", "when", "with", "my",
        "can", "do", "does", "why", "not", "this", "they", "you", "your", "we", "will", "was", "if"}


def terms(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9][a-z0-9-]+", text.lower()) if t not in STOP and len(t) > 2}


class Corpus:
    """Every markdown page in the workspace corpus, loaded once."""

    def __init__(self):
        base = ws.load_path("corpus")
        self.pages: list[dict] = []
        for p in sorted(base.rglob("*.md")):
            text = p.read_text(encoding="utf-8", errors="ignore")
            first = next((ln.lstrip("# ").strip() for ln in text.splitlines() if ln.strip()), p.stem)
            self.pages.append({"path": str(p.relative_to(base)), "title": first[:120],
                               "text": text, "terms": terms(text)})

    def search(self, q: str, max_results: int = 5) -> list[dict]:
        qt = terms(q)
        scored = []
        for page in self.pages:
            hit = qt & page["terms"]
            if hit:
                bonus = 2 * len(qt & terms(page["title"]))
                scored.append((len(hit) + bonus, page))
        scored.sort(key=lambda x: -x[0])
        return [{"title": pg["title"], "path": pg["path"], "score": s,
                 "snippet": textwrap.shorten(re.sub(r"\s+", " ", pg["text"]), 300)}
                for s, pg in scored[:max_results]]

    def fetch(self, path: str, max_chars: int = 4000) -> dict:
        for page in self.pages:
            if page["path"] == path:
                return {"path": path, "text": page["text"][:max_chars]}
        return {"path": path, "text": "[no such page]"}


_CORPUS: Corpus | None = None


def corpus() -> Corpus:
    global _CORPUS
    if _CORPUS is None:
        _CORPUS = Corpus()
    return _CORPUS


def search(q: str, max_results: int = 5) -> list[dict]:
    return corpus().search(q, max_results)


def fetch(path: str, max_chars: int = 4000) -> dict:
    return corpus().fetch(path, max_chars)


def web_search(q: str, max_results: int = 5) -> list[dict]:
    """Tavily search through its REST API. Returns [] when no key is set."""
    if not TAVILY_KEY:
        return []
    try:
        r = httpx.post("https://api.tavily.com/search", timeout=30,
                       json={"api_key": TAVILY_KEY, "query": q, "max_results": max_results,
                             "include_answer": False})
        r.raise_for_status()
        return [{"title": it.get("title", ""), "url": it.get("url", ""), "content": it.get("content", "")[:600]}
                for it in r.json().get("results", [])]
    except Exception as e:  # noqa: BLE001 - a failed web search is a valid (empty) result
        return [{"title": "web search failed", "url": "", "content": str(e)[:200]}]
