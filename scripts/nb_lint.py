#!/usr/bin/env python3
"""Lint notebook and markdown prose against docs/STYLE.md.

Rules (id: what it catches)
  P0xx  position words: a notebook must stand alone (no day, module, week,
        or "yesterday"; no path or link into a sibling module)
  T0xx  phrases that read as machine-written
  B0xx  former client, partner, and corpus names that must not appear
  L001  markdown cell over 150 words (L002 warns at 120)
  L003  checkpoint cell ("You should see ...") over 60 words
  E001  exclamation mark in prose
  H001  header ends with a colon
  H002  header is Title Case (sentence case is the rule)
  S001  more than one bold span in a cell
  S002  em dash outside a "## Task k of N — title" header
  S003  emoji outside the fixed set
  K001  task headers not numbered "Task k of N" consecutively
  K002  a required template section is missing
  K003  the Learn, Create, Grow acts are out of order or an act has no task

Matching normalises whitespace first, so a phrase split across a hard wrap
is still found (the offset -> line map is how the report stays accurate).

Suppress a rule for one cell with an HTML comment in that cell:
    <!-- lint: ignore S002 -->     or     <!-- lint: ignore -->

Usage: python scripts/nb_lint.py [--strict] [--brand-only] [paths...]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
MODULE_DIR = re.compile(r"^\d{2}_[A-Za-z]")
SKIP_PARTS = {".git", ".venv", "node_modules", "__pycache__", ".ipynb_checkpoints", "__marimo__", ".qdrant_local"}
# Files that legitimately contain the banned strings (the lint itself, its tests).
BRAND_EXEMPT = {"scripts/nb_lint.py", "tests/test_nb_lint.py", "tests/test_scripts.py", "scripts/strip_outputs.py"}
# Files that may say "Day N": the schedule and the front page.
POSITION_EXEMPT_PREFIXES = ("README.md", "docs/", "CLAUDE.md", "AGENTS.md", "00_Setup/", "project/", "data/")

_I = re.I
POSITION = [
    (r"\b(?:Week|Weeks)\s+(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten)\b", "names a course week", "P001"),
    (r"\bDay\s+(?:\d+|one|two|three|four|five)\b", "names a course day", "P002"),
    (r"\b(?:Demo|Module|Session|Notebook)\s+\d{1,2}\b", "names a sibling module by number", "P003"),
    (r"\bTC\s?\d+\b", "names a technical challenge by number", "P004"),
    (r"\b(?:yesterday|tomorrow|this morning|this afternoon|earlier today|later today|last week|next week)\b", "temporal clause", "P005"),
    (r"\bthis\s+course\b|\bsince\s+day\s+one\b|\ball\s+along\b|\bweeks\s+ago\b|\bwhen\s+you\s+scoped\b", "temporal clause", "P006"),
    (r"\balready\s+(?:built|wrote)\b", "assumes an earlier notebook", "P007"),
    (r"(?<![\w/])\d{2}_[A-Z][A-Za-z_&]+/", "path into a sibling module", "P008"),
    (r"\]\(\.?\.?/?[A-Za-z0-9_./-]+\.(?:ipynb|py)\)", "links to a notebook file", "P009"),
    (r"\]\(\.\./README\.md(?:#[^)]*)?\)", "links out to a README", "P010"),
]
TELLS = [
    (r"\bcomprehensive\b", "T001"), (r"\bleverag(?:e|es|ed|ing)\b", "T002"), (r"\brobust(?:ly|ness)?\b", "T003"),
    (r"\bbest practices?\b", "T004"), (r"\bin this notebook\b", "T005"), (r"\bnow that (?:we|you)\b", "T006"),
    (r"\bkey takeaways?\b", "T007"), (r"\blet'?s (?:break|dive|explore|get started|begin)\b", "T008"),
    (r"\bdelve\b", "T009"), (r"\bseamless(?:ly)?\b", "T010"), (r"\bcutting[- ]edge\b|\bstate[- ]of[- ]the[- ]art\b", "T011"),
    (r"\bpowerful\b", "T012"), (r"\bunlock(?:s|ed|ing)?\b", "T013"), (r"\bharness the power\b", "T014"),
    (r"\bit'?s (?:important|worth) (?:to note|noting)\b|\bit is (?:important|worth) (?:to note|noting)\b", "T015"),
    (r"\bin today'?s\b", "T016"), (r"\blandscape\b", "T017"), (r"\bjourney\b", "T018"),
    (r"\bempower(?:s|ed|ing)?\b|\bsupercharge\b|\belevate\b", "T019"), (r"\bcrucial\b|\bvital\b", "T020"),
    (r"\butiliz(?:e|es|ed|ing)\b", "T021"), (r"\b(?:Furthermore|Moreover|Additionally),", "T022"),
    (r"\bin conclusion\b|\boverall,", "T023"), (r"\bhappy coding\b|\bwelcome to\b|\bcongratulations\b|\bgreat job\b", "T024"),
    (r"\bfinal takeaways\b|\bsummary of what we (?:learned|built|did)\b", "T025"),
    (r"\bdeep dive\b|\bunder the hood\b|\bthink of it as\b", "T026"),
    (r"\bby the end of this\b", "T027"), (r"\bgame[- ]chang(?:er|ing)\b|\brevolutioni[sz]e\b|\btransformative\b", "T028"),
]
BRAND = [
    (r"\bAccenture\b", "B001"), (r"\bMWFG\b|\bMidWest Financial\b", "B002"), (r"\bACME\b|\bAcme\b|\bacme_", "B003"),
    (r"AI[ -]?Makers?pace|aimakerspace|AI-Maker-Space", "B004"), (r"\bMorgan Stanley\b", "B005"),
    (r"\bEU AI Act\b|eu_ai_act", "B006"), (r"LLM-Dev-101/assets|LLMOps-Dev-101/assets", "B007"),
    (r"forms\.gle/|skills\.workera\.ai|aie-challenge|Interactive-Dev-Environment-for", "B008"),
    (r"linkedin\.com/in/", "B009"),
    (r"\byour client'?s?\b|\bclient readout\b|\bas an? (?:\w+ )?consultant\b|\bconsulting engagement\b", "B010"),
    (r"\[/admin\]|begin_admin_session", "B011"), (r"/home/[a-z]+/|/Users/[a-z]+/", "B012"),
]
ALLOWED_EMOJI = {"✅", "❓", "⚠", "ℹ", "❌"}
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⬀-⯿]")
PROPER = {
    "AI", "Aspire", "LangChain", "LangGraph", "LangSmith", "RAGAS", "Ragas", "DSPy", "GraphRAG", "MCP", "OpenAI",
    "Anthropic", "Claude", "GPT", "Qdrant", "Chroma", "ChromaDB", "Python", "NIST", "OWASP", "DeepEval", "Tavily",
    "Streamlit", "Jupyter", "GitHub", "Git", "LLM", "LLMs", "RAG", "JSON", "JSONL", "CSV", "API", "APIs", "SDG",
    "BM25", "RRF", "HyDE", "PII", "TTS", "STT", "Kokoro", "Whisper", "Parakeet", "Deskmate", "Titanium", "Engineer",
    "Cohere", "Inter", "I", "Ollama", "LM", "Studio", "vLLM", "Docker", "Windows", "Mac", "macOS", "Linux", "Node",
    "Unsloth", "Hugging", "Face", "UTCP", "A2A", "SQL", "SQLite", "HTTP", "URL", "ID", "IDs", "UI", "UX", "PoC",
    "MVP", "PMF", "OK", "Task", "Setup", "Build", "Ship", "Share", "Activity", "Advanced", "Conclusion",
    "Deep", "Research", "Agents", "Agent", "Memory", "Guardrails", "Voice", "Evals", "Prompt", "Patterns",
    "Retrieval", "Multi", "Architecture", "Responsible", "Top", "Release", "Decision", "Risk", "Register",
    "Vibe", "Judge", "Judges", "Checks", "Ladder", "Six", "Ways", "Off", "Shelf", "Optimization", "Trajectory",
    "Kinds", "Three", "Report", "Generator", "Unroll", "Attack", "Your", "Improving", "Dev", "Environment", "Agentic",
    "DCI", "vs", "V1", "V2", "React", "ReAct", "CoT", "Redis", "SDK", "CLI", "PDF", "PDFs", "Markdown", "README",
    "Loom", "Zoom", "Slack", "Teams", "Excel", "PowerPoint", "Google", "Azure", "AWS", "GCP", "Kubernetes",
    "Prompts", "Transcripts", "Corpus", "Manifest", "Workspace", "Learn", "Create", "Grow",
}
REQUIRED_SECTIONS = [
    ("## Learn | Create | Grow", "K002"),
    ("### Learn", "K002"),
    ("### Create", "K002"),
    ("### Grow", "K002"),
    ("**Estimated time:**", "K002"),
    ("## Setup", "K002"),
    ("# Learn\n", "K002"),
    ("# Create\n", "K002"),
    ("## Your turn", "K002"),
    ("# Grow\n", "K002"),
    ("## From prototype to production", "K002"),
    ("## Responsible controls", "K002"),
    ("## Grow further", "K002"),
]
TASK_HEADER = re.compile(r"^##\s+Task\s+(\d+)\s+of\s+(\d+)\s+—\s+\S", re.M)
LOOSE_TASK = re.compile(r"^##\s+Task\b", re.M)
IGNORE = re.compile(r"<!--\s*lint:\s*ignore(?:\s+([A-Z]\d{3}(?:\s+[A-Z]\d{3})*))?\s*-->")


class Finding:
    def __init__(self, where: str, rule: str, snippet: str, why: str, level: str = "fail"):
        self.where, self.rule, self.snippet, self.why, self.level = where, rule, snippet, why, level

    def __str__(self) -> str:
        tag = "warn" if self.level == "warn" else "fail"
        return f"{self.where}:{self.rule}:{tag}: {self.snippet!r} — {self.why}"


def _flatten(text: str) -> tuple[str, list[int]]:
    flat, line_of, line, prev_space = [], [], 1, False
    for ch in text:
        if ch == "\n":
            line += 1
        if ch.isspace():
            if prev_space:
                continue
            flat.append(" "); line_of.append(line); prev_space = True
        else:
            flat.append(ch); line_of.append(line); prev_space = False
    return "".join(flat), line_of


def _strip_code(md: str) -> str:
    """Remove fenced blocks and inline code so prose rules do not fire on code."""
    md = re.sub(r"```.*?```", " ", md, flags=re.S)
    md = re.sub(r"`[^`\n]*`", " ", md)
    md = re.sub(r"<!--.*?-->", " ", md, flags=re.S)
    return md


def _phrases(text: str, where: str, *, position: bool, tells: bool, brand: bool, ignored: set[str]) -> list[Finding]:
    out: list[Finding] = []
    flat, line_of = _flatten(text)
    groups = []
    if position:
        groups += [(re.compile(p, _I), why, rid, "fail") for p, why, rid in POSITION]
    if tells:
        groups += [(re.compile(p, _I), "reads as machine-written", rid, "fail") for p, rid in TELLS]
    if brand:
        groups += [(re.compile(p), "former client, partner, or corpus name", rid, "fail") for p, rid in BRAND]
    for pat, why, rid, level in groups:
        if rid in ignored or "*" in ignored:
            continue
        for m in pat.finditer(flat):
            out.append(Finding(f"{where}:{line_of[m.start()]}", rid, m.group(0).strip(), why, level))
    return out


def _header_words(h: str) -> list[str]:
    body = h.lstrip("#").strip()
    body = EMOJI.sub("", body).replace("️", "")
    body = re.sub(r"^\s*(?:Task\s+\d+\s+of\s+\d+\s+—\s*)", "", body)
    return body.split()


def _prose_rules(md: str, where: str, ignored: set[str], *, is_cell: bool) -> list[Finding]:
    out: list[Finding] = []
    prose = _strip_code(md)
    lines = md.splitlines()

    if "E001" not in ignored and "*" not in ignored:
        for i, line in enumerate(_strip_code(md).splitlines(), 1):
            if "!" in line and not line.strip().startswith("!["):
                for m in re.finditer(r"(?<!\!)\!(?!\[)", line):
                    out.append(Finding(f"{where}:{i}", "E001", line.strip()[:60], "exclamation mark"))
                    break
    for i, line in enumerate(lines, 1):
        if not re.match(r"^#{1,6}\s", line):
            continue
        if "H001" not in ignored and line.rstrip().endswith(":"):
            out.append(Finding(f"{where}:{i}", "H001", line.strip()[:60], "header ends with a colon"))
        if "H002" not in ignored:
            words = _header_words(line)
            title_case = [w for w in words[1:]
                          if w[:1].isupper() and not w.isupper() and not any(c.isdigit() for c in w)
                          and w.strip("(),.:;'\"") not in PROPER and "-" not in w and "_" not in w]
            if len(title_case) >= 2:
                out.append(Finding(f"{where}:{i}", "H002", line.strip()[:60],
                                   f"Title Case header ({', '.join(title_case[:3])}); use sentence case"))
    if is_cell:
        words = len(prose.split())
        first = md.strip().splitlines()[0] if md.strip() else ""
        is_checkpoint = first.lstrip("*_ ").lower().startswith("you should see")
        is_meta = first.startswith("**Estimated time")
        if is_checkpoint and words > 60 and "L003" not in ignored:
            out.append(Finding(where, "L003", first[:50], f"checkpoint cell is {words} words (max 60)"))
        elif words > 150 and "L001" not in ignored:
            out.append(Finding(where, "L001", first[:50], f"markdown cell is {words} words (max 150; aim for 120)"))
        elif words > 120 and "L002" not in ignored:
            out.append(Finding(where, "L002", first[:50], f"markdown cell is {words} words (aim for 120)", "warn"))
        bolds = re.findall(r"\*\*[^*\n]+\*\*", prose)
        if len(bolds) > 1 and not is_meta and "S001" not in ignored:
            out.append(Finding(where, "S001", bolds[1][:40], f"{len(bolds)} bold spans in one cell (max 1)"))
        if "S002" not in ignored:
            for i, line in enumerate(prose.splitlines(), 1):
                if "—" in line and not re.match(r"^##\s+Task\s+\d+\s+of\s+\d+\s+—", line):
                    out.append(Finding(f"{where}:{i}", "S002", line.strip()[:60], "em dash outside a task header"))
        if "S003" not in ignored:
            for i, line in enumerate(md.splitlines(), 1):
                for m in EMOJI.finditer(line):
                    ch = m.group(0)
                    if ch not in ALLOWED_EMOJI:
                        out.append(Finding(f"{where}:{i}", "S003", ch, "emoji outside the fixed set"))
    return out


def _ignored(md: str) -> set[str]:
    m = IGNORE.search(md)
    if not m:
        return set()
    return set(m.group(1).split()) if m.group(1) else {"*"}


def lint_notebook(path: Path, *, brand_only: bool = False) -> list[Finding]:
    rel = str(path.relative_to(ROOT)) if path.is_absolute() and path.is_relative_to(ROOT) else str(path)
    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [Finding(rel, "X000", "", f"cannot parse notebook: {e}")]
    out: list[Finding] = []
    all_md: list[str] = []
    for k, cell in enumerate(nb.get("cells", [])):
        src = "".join(cell.get("source", []))
        where = f"{rel}[cell {k}]"
        ignored = _ignored(src)
        if cell.get("cell_type") == "markdown":
            all_md.append(src)
            out += _phrases(_strip_code(src), where, position=not brand_only, tells=not brand_only, brand=True, ignored=ignored)
            if not brand_only:
                out += _prose_rules(src, where, ignored, is_cell=True)
        else:
            out += _phrases(src, where, position=False, tells=False, brand=True, ignored=ignored)
            if not brand_only and "P008" not in ignored:
                for m in re.finditer(r"(?<![\w/])\d{2}_[A-Z][A-Za-z_&]+/", src):
                    out.append(Finding(where, "P008", m.group(0), "path into a sibling module"))
    if brand_only:
        return out
    joined = "\n".join(all_md)
    if "K002" not in _ignored(joined):
        for needle, rid in REQUIRED_SECTIONS:
            if needle not in joined:
                out.append(Finding(rel, rid, needle, "required template section is missing"))
    acts = [(k, "".join(c.get("source", [])).strip()) for k, c in enumerate(nb.get("cells", []))
            if c.get("cell_type") == "markdown"]
    pos = {name: next((k for k, t in acts if t == f"# {name}"), None) for name in ("Learn", "Create", "Grow")}
    if None not in pos.values() and "K003" not in _ignored(joined):
        if not (pos["Learn"] < pos["Create"] < pos["Grow"]):
            out.append(Finding(rel, "K003", "# Learn / # Create / # Grow", "acts must appear in the order Learn, Create, Grow"))
        first_task = {name: any(LOOSE_TASK.match(t) for k, t in acts if k > pos[name] and k < (pos["Create"] if name == "Learn" else pos["Grow"]))
                      for name in ("Learn", "Create")}
        for name, ok in first_task.items():
            if not ok:
                out.append(Finding(rel, "K003", f"# {name}", f"the {name} act has no task"))
        turn = next((k for k, t in acts if t.startswith("## Your turn")), None)
        if turn is not None and not (pos["Create"] < turn < pos["Grow"]):
            out.append(Finding(rel, "K003", "## Your turn", "the group activity belongs at the end of the Create act"))
    tasks = TASK_HEADER.findall(joined)
    loose = len(LOOSE_TASK.findall(joined))
    if loose and len(tasks) != loose:
        out.append(Finding(rel, "K001", "## Task", f"{loose - len(tasks)} task header(s) not in the form '## Task k of N — title'"))
    if tasks:
        ks = [int(k) for k, _ in tasks]
        ns = {int(n) for _, n in tasks}
        if ks != list(range(1, len(ks) + 1)) or ns != {len(ks)}:
            out.append(Finding(rel, "K001", f"Task {ks}", f"task numbering must be 1..N of N (found N={sorted(ns)})"))
    return out


def lint_markdown(path: Path, *, brand_only: bool = False) -> list[Finding]:
    rel = str(path.relative_to(ROOT)) if path.is_absolute() and path.is_relative_to(ROOT) else str(path)
    text = path.read_text(encoding="utf-8", errors="replace")
    ignored = _ignored(text)
    exempt_position = rel.startswith(POSITION_EXEMPT_PREFIXES)
    in_module = any(MODULE_DIR.match(part) for part in Path(rel).parts[:-1])
    out = _phrases(_strip_code(text), rel, position=not brand_only and not exempt_position,
                   tells=not brand_only and in_module, brand=rel not in BRAND_EXEMPT, ignored=ignored)
    if not brand_only and in_module:
        out += _prose_rules(text, rel, ignored, is_cell=False)
    return out


def lint_other(path: Path) -> list[Finding]:
    """Brand strings in code, config, and CI."""
    rel = str(path.relative_to(ROOT)) if path.is_absolute() and path.is_relative_to(ROOT) else str(path)
    if rel in BRAND_EXEMPT:
        return []
    text = path.read_text(encoding="utf-8", errors="replace")
    return _phrases(text, rel, position=False, tells=False, brand=True, ignored=set())


def targets(paths: list[str]) -> list[Path]:
    if paths:
        out = []
        for p in paths:
            q = Path(p)
            out += sorted(q.rglob("*")) if q.is_dir() else [q]
        return [p for p in out if p.is_file()]
    out = []
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or any(part in SKIP_PARTS for part in p.parts):
            continue
        if p.suffix in {".ipynb", ".md", ".py", ".toml", ".yml", ".yaml", ".json", ".jsonl", ".csv", ".txt"}:
            out.append(p)
    return out


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--strict", action="store_true", help="warnings fail too")
    ap.add_argument("--brand-only", action="store_true", help="only the B0xx rules, repo-wide")
    args = ap.parse_args(argv)

    findings: list[Finding] = []
    n = 0
    for p in targets(args.paths):
        n += 1
        if p.suffix == ".ipynb":
            findings += lint_notebook(p, brand_only=args.brand_only)
        elif p.suffix == ".md":
            findings += lint_markdown(p, brand_only=args.brand_only)
        else:
            findings += lint_other(p)
    fails = [f for f in findings if f.level == "fail" or args.strict]
    warns = [f for f in findings if f.level == "warn" and not args.strict]
    for f in sorted(findings, key=str):
        print(f)
    if fails:
        print(f"\n✗ {len(fails)} finding(s) across {n} file(s); {len(warns)} warning(s). See docs/STYLE.md.")
        return 1
    print(f"✓ {n} file(s) pass the style lint; {len(warns)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
