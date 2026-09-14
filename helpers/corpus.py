"""Reading the workspace corpus, and the keyword search several notebooks need
before they have a vector store.

    from helpers import corpus
    pages = corpus.pages()                    # [{path, title, text}, ...]
    hits  = corpus.search("vpn staging", pages, k=3)

`terms` is the tokeniser those searches share. It is deliberately plain: a
notebook that wants better retrieval builds it, and that is the lesson.
"""
from __future__ import annotations

import re

from helpers import workspace as ws

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "did", "do", "does", "for", "from",
    "had", "has", "have", "how", "i", "if", "in", "is", "it", "its", "my", "no", "not", "of",
    "on", "or", "our", "should", "so", "that", "the", "their", "them", "then", "there", "these",
    "they", "this", "to", "was", "were", "what", "when", "where", "which", "who", "why", "will",
    "with", "you", "your",
}
_TOKEN = re.compile(r"[a-z0-9][a-z0-9._-]*")


def terms(text: str) -> set[str]:
    """Lowercase content words, stopwords dropped."""
    return {t for t in _TOKEN.findall((text or "").lower()) if t not in STOPWORDS}


def title_of(text: str, fallback: str = "") -> str:
    """The first heading or first non-empty line."""
    for line in (text or "").splitlines():
        if line.strip():
            return line.lstrip("#").strip()[:120] or fallback
    return fallback


def pages(*, quiet: bool = True) -> list[dict]:
    """Every markdown page in the corpus as `{path, title, text}`, sorted by path.

    Reads the cohort's corpus when it exists and the seed example otherwise,
    exactly like every other artifact.
    """
    base = ws.load_path("corpus")
    out = []
    for p in sorted(base.rglob("*.md")):
        text = p.read_text(encoding="utf-8", errors="ignore")
        rel = str(p.relative_to(base))
        out.append({"path": rel, "title": title_of(text, p.stem), "text": text})
    if not quiet:
        print(f"{len(out)} corpus pages from the {ws.source('corpus')}")
    return out


def as_dict(page_list: list[dict] | None = None) -> dict[str, str]:
    """`{path: text}`, for a notebook that wants to look a page up by name."""
    return {p["path"]: p["text"] for p in (page_list if page_list is not None else pages())}


def sections(text: str, name: str = "") -> list[dict]:
    """Split one markdown page on `##` headings into `{title, text, source}`."""
    out, title, lines = [], title_of(text, name), []
    for line in (text or "").splitlines():
        if line.startswith("## "):
            if lines:
                out.append({"source": name, "title": title, "text": "\n".join(lines).strip()})
            title, lines = line[3:].strip(), []
        else:
            lines.append(line)
    if lines:
        out.append({"source": name, "title": title, "text": "\n".join(lines).strip()})
    return [s for s in out if s["text"]]


def search(query: str, page_list: list[dict] | None = None, *, k: int = 3) -> list[dict]:
    """Rank pages by how many query words they contain. Returns the top `k`
    pages with a `score`, highest first. Ties break on path, so it is stable."""
    corpus_pages = page_list if page_list is not None else pages()
    q = terms(query)
    if not q:
        return []
    scored = []
    for p in corpus_pages:
        overlap = q & terms(p["title"] + " " + p["text"])
        if overlap:
            scored.append({**p, "score": len(overlap), "matched": sorted(overlap)})
    scored.sort(key=lambda p: (-p["score"], p["path"]))
    return scored[:k]


def snippet(text: str, width: int = 700) -> str:
    """One-line-ish preview of a page, for a tool result."""
    import textwrap
    return textwrap.shorten(re.sub(r"\s+", " ", text or "").strip(), width=width, placeholder=" ...")
