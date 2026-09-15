"""The workspace: what the cohort produces, read back by later notebooks.

Every notebook reads and writes artifacts through this module and never opens
`workspace/` or `data/seed/` paths directly. `load()` returns the cohort's own
artifact when it exists and is valid, and otherwise falls back to the seed
example with a one-line notice. `save()` validates before it writes.

    from helpers import workspace as ws
    charter = ws.load("charter")            # str
    rows = ws.load("transcripts")           # list[dict]
    ws.save("judge_scores", rows)           # validates required keys, writes, logs

Formats: md -> str, json -> object, jsonl -> list[dict], csv -> list[dict],
dir -> list[Path].
"""
from __future__ import annotations

import csv
import io
import json
import os
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from helpers.config import ROOT, SEED, PROJECT

# ── Schema ──────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Artifact:
    name: str
    path: str            # relative to the workspace root
    fmt: str             # md | json | jsonl | csv | dir
    producer: str        # module directory prefix, e.g. "04"
    keys: tuple = ()     # required keys per row (jsonl/csv) or top-level keys (json)
    about: str = ""
    optional: str = ""   # why the seed may lack it (nothing downstream reads it)


_A = Artifact
SCHEMA: dict[str, Artifact] = {a.name: a for a in [
    _A("manifest", "manifest.json", "json", "01", ("cohort", "created", "writes"),
       "What has been written, by which notebook, when"),
    _A("charter", "pitch/charter.md", "md", "01", (), "The group's problem, users, and product vision"),
    _A("prompts", "prompts/prompts.jsonl", "jsonl", "02", ("pattern", "input", "output", "model"),
       "One row per prompt pattern tried, with the model's output"),
    _A("transcripts", "transcripts/transcripts.jsonl", "jsonl", "03", ("id", "turns", "tool_calls"),
       "Multi-turn conversations with the first agent, including tool calls"),
    _A("rubric", "evals/rubric.json", "json", "04", ("criteria",), "The group's scoring rubric"),
    _A("vibe_checks", "evals/vibe_checks.jsonl", "jsonl", "04", ("id", "input", "expected"),
       "Hand-written inputs with what a good answer must contain"),
    _A("judge_scores", "evals/judge_scores.jsonl", "jsonl", "04", ("id", "judge", "score", "rationale"),
       "LLM-as-judge scores over the transcripts, with an optional human_score"),
    _A("corpus", "corpus", "dir", "05", (), "Markdown pages rendered from the earlier artifacts"),
    _A("baseline_runs", "retrieval/baseline_runs.jsonl", "jsonl", "05", ("question", "answer", "contexts"),
       "Questions answered by the first RAG pipeline"),
    _A("eval_cases", "retrieval/eval_cases.jsonl", "jsonl", "06", ("id", "question", "reference"),
       "Retrieval eval cases with a reference answer"),
    _A("ladder", "retrieval/ladder.csv", "csv", "06", ("retriever", "hit_rate", "mrr"),
       "One row per retriever on the ladder, with its scores"),
    _A("wiki", "corpus/wiki/index.md", "md", "07", (), "A model-readable index of the corpus"),
    _A("agentic_runs", "retrieval/agentic_runs.jsonl", "jsonl", "07", ("question", "mode", "answer"),
       "The same questions answered by direct and agentic retrieval"),
    _A("testset", "retrieval/testset.jsonl", "jsonl", "08", ("question", "reference"),
       "A synthetic test set generated from the corpus"),
    _A("ragas_scores", "retrieval/ragas_scores.csv", "csv", "08", ("variant", "faithfulness"),
       "RAGAS scores before and after one change"),
    _A("tasks", "agent/tasks.jsonl", "jsonl", "09", ("id", "goal", "success"),
       "Agent tasks composed from the eval cases, with a success condition"),
    _A("trajectories", "agent/trajectories.jsonl", "jsonl", "09", ("id", "task_id", "steps", "passed"),
       "Full agent runs against the tasks"),
    _A("capability_report", "agent/capability_report.md", "md", "09", (), "Where the agent passes and fails"),
    _A("memory", "memory/MEMORY.md", "md", "10", (), "Long-term memory distilled from the trajectories"),
    _A("episodes", "memory/episodes.jsonl", "jsonl", "10", ("id", "summary"), "Episodic memory entries"),
    _A("tools_catalog", "agent/tools_catalog.json", "json", "11", ("tools",),
       "The same capability described as tool, skill, MCP server, and sub-agent"),
    _A("multi_agent_report", "research/multi_agent_report.md", "md", "12", (), "A cited multi-agent report"),
    _A("guardrail_cases", "guardrails/cases.jsonl", "jsonl", "13", ("id", "input", "attack", "expected"),
       "Attack and benign inputs drawn from the transcripts"),
    _A("ladder_results", "guardrails/ladder_results.jsonl", "jsonl", "13", ("case_id", "rung", "blocked"),
       "Which rung of the guardrail ladder caught which case"),
    _A("voice_sessions", "research/voice_sessions.jsonl", "jsonl", "14", ("id", "question", "answer"),
       "Spoken questions and the answers given",
       optional="needs the speech services running, and no later module reads it"),
    _A("dspy_program", "research/dspy_program.json", "json", "15", ("optimizer",),
       "The optimised judge program and its agreement score"),
    _A("graph", "retrieval/graph.json", "json", "16", ("nodes", "edges"), "A knowledge graph over the corpus"),
    _A("graph_eval", "retrieval/graph_eval.json", "json", "16", ("graph", "vector"),
       "GraphRAG scored against the vector baseline"),
    _A("research_report", "research/report.md", "md", "17", (), "A deep-research report on the top failure mode"),
    _A("ots_results", "guardrails/ots_results.jsonl", "jsonl", "18", ("case_id", "guardrail", "tripped"),
       "Off-the-shelf guardrail results on the same cases"),
    _A("risk_register", "demo/risk_register.md", "md", "19", (), "A NIST AI RMF risk register"),
    _A("owasp_findings", "guardrails/owasp_findings.jsonl", "jsonl", "20", ("id", "category", "succeeded"),
       "OWASP LLM Top 10 attacks against the agent"),
    _A("deepeval_results", "demo/deepeval_results.jsonl", "jsonl", "21", ("test", "version", "passed"),
       "DeepEval results for two versions of the agent"),
    _A("release_decision", "demo/release_decision.md", "md", "21", (), "Ship or hold, with evidence"),
    _A("scorecard", "demo/scorecard.jsonl", "jsonl", "project", ("group", "criterion", "score"),
       "Demo day scores from the cohort's own harness",
       optional="written only if the cohort holds a demo day"),
]}

# Which day each producing module runs on. This is the one place outside
# docs/schedule/ that knows about days; notebooks never do.
# Day 4 is the instructors' pick from 14 to 21; day 5 is optional, so its
# only artifact is the demo scorecard, and only if a demo day is held.
DAYS: dict[int, tuple[str, ...]] = {
    1: ("01", "02", "03", "04", "05"),
    2: ("06", "07", "08", "09"),
    3: ("10", "11", "12", "13"),
    4: ("14", "15", "16", "17", "18", "19", "20", "21"),
    5: ("project",),
}


def day_of(module: str) -> int:
    for day, mods in DAYS.items():
        if module in mods:
            return day
    raise KeyError(module)


# ── Roots ───────────────────────────────────────────────────────────────────


def root() -> Path:
    """The live workspace. Override with TE_WORKSPACE (absolute or repo-relative)."""
    env = os.environ.get("TE_WORKSPACE", "").strip()
    if env:
        p = Path(env)
        return p if p.is_absolute() else ROOT / p
    return ROOT / "workspace"


def seed_root() -> Path:
    return SEED


def path(name: str, *, seed: bool = False) -> Path:
    """Absolute path of an artifact in the workspace (or the seed)."""
    art = SCHEMA[name]
    return (seed_root() if seed else root()) / art.path


# ── Reading ─────────────────────────────────────────────────────────────────


def _read(p: Path, fmt: str):
    if fmt == "md":
        return p.read_text(encoding="utf-8")
    if fmt == "json":
        return json.loads(p.read_text(encoding="utf-8"))
    if fmt == "jsonl":
        return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]
    if fmt == "csv":
        return list(csv.DictReader(io.StringIO(p.read_text(encoding="utf-8"))))
    if fmt == "dir":
        return sorted(q for q in p.rglob("*") if q.is_file())
    raise ValueError(fmt)


def _present(p: Path, fmt: str) -> bool:
    if fmt == "dir":
        return p.is_dir() and any(q.is_file() for q in p.rglob("*"))
    return p.is_file() and p.stat().st_size > 0


def source(name: str) -> str | None:
    """'workspace', 'seed', or None."""
    art = SCHEMA[name]

    def present(base: Path) -> bool:
        p = base / art.path
        if name == "corpus":
            # A separately saved wiki is navigation, not a replacement corpus.
            # Interactive experiments may save it while reading seed pages.
            return any(q.is_file() and q.relative_to(p).parts[0] != "wiki"
                       and q.name != "vibe_checks.md" for q in p.rglob("*.md"))
        return _present(p, art.fmt)

    if present(root()) and not _invalid(root() / art.path, art):
        return "workspace"
    if present(seed_root()):
        return "seed"
    return None


def load(name: str, *, quiet: bool = False):
    """The cohort's artifact if present and valid, else the seed example."""
    art = SCHEMA[name]
    src = source(name)
    if src is None:
        raise FileNotFoundError(
            f"No '{name}' in the workspace or the seed. It is written by module "
            f"{art.producer} ({art.path})."
        )
    base = root() if src == "workspace" else seed_root()
    if src == "seed" and not quiet:
        print(f"ℹ '{name}' comes from the seed example (data/seed/{art.path}); "
              f"your workspace does not have it yet.")
    return _read(base / art.path, art.fmt)


def load_path(name: str) -> Path:
    """The path that load() would read from. Useful for directory artifacts."""
    src = source(name)
    if src is None:
        raise FileNotFoundError(name)
    return (root() if src == "workspace" else seed_root()) / SCHEMA[name].path


# ── Validation ──────────────────────────────────────────────────────────────


def validate(name: str, data) -> list[str]:
    """Problems with `data` for artifact `name`. Empty list means valid."""
    art = SCHEMA[name]
    problems: list[str] = []
    if art.fmt == "md":
        if not isinstance(data, str) or len(data.strip()) < 20:
            problems.append("markdown must be a string of at least 20 characters")
    elif art.fmt == "json":
        if not isinstance(data, dict):
            problems.append("json artifact must be an object")
        else:
            for k in art.keys:
                if k not in data:
                    problems.append(f"missing top-level key '{k}'")
    elif art.fmt in ("jsonl", "csv"):
        if not isinstance(data, list) or not data:
            problems.append("must be a non-empty list of rows")
        else:
            for i, row in enumerate(data):
                if not isinstance(row, dict):
                    problems.append(f"row {i} is not an object")
                    continue
                missing = [k for k in art.keys if k not in row]
                if missing:
                    problems.append(f"row {i} missing {missing}")
                if len(problems) > 10:
                    problems.append("...")
                    break
    elif art.fmt == "dir":
        if not isinstance(data, (list, tuple)) or not data:
            problems.append("directory artifact must be a non-empty list of files")
    return problems


def _invalid(p: Path, art: Artifact) -> bool:
    try:
        data = _read(p, art.fmt)
    except Exception:
        return True
    return bool(validate(art.name, data))


# ── Writing ─────────────────────────────────────────────────────────────────


def save(name: str, data, *, module: str | None = None) -> Path:
    """Validate, write, and record in the manifest. Returns the path written."""
    art = SCHEMA[name]
    problems = validate(name, data)
    if problems:
        raise ValueError(f"'{name}' failed validation: " + "; ".join(problems))
    p = root() / art.path
    p.parent.mkdir(parents=True, exist_ok=True)
    if art.fmt == "md":
        p.write_text(data, encoding="utf-8")
        count = len(data.splitlines())
    elif art.fmt == "json":
        p.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        count = len(data)
    elif art.fmt == "jsonl":
        p.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in data), encoding="utf-8")
        count = len(data)
    elif art.fmt == "csv":
        fields = list(dict.fromkeys(k for r in data for k in r))
        with p.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields)
            w.writeheader()
            w.writerows(data)
        count = len(data)
    else:
        raise ValueError(f"use save_dir() for '{name}'")
    _record(name, module or art.producer, count)
    print(f"✅ wrote {name} → {p.relative_to(ROOT) if p.is_relative_to(ROOT) else p} ({count} {'lines' if art.fmt == 'md' else 'rows'})")
    return p


def save_dir(name: str, files: dict[str, str], *, module: str | None = None) -> Path:
    """Write a directory artifact from {relative_name: text}."""
    art = SCHEMA[name]
    if art.fmt != "dir":
        raise ValueError(f"'{name}' is not a directory artifact")
    if not files:
        raise ValueError("no files to write")
    base = root() / art.path
    base.mkdir(parents=True, exist_ok=True)
    for rel, text in files.items():
        q = base / rel
        q.parent.mkdir(parents=True, exist_ok=True)
        q.write_text(text, encoding="utf-8")
    _record(name, module or art.producer, len(files))
    print(f"✅ wrote {name}/ ({len(files)} files)")
    return base


def _record(name: str, module: str, count: int) -> None:
    p = root() / SCHEMA["manifest"].path
    p.parent.mkdir(parents=True, exist_ok=True)
    manifest = json.loads(p.read_text(encoding="utf-8")) if p.exists() else _fresh_manifest()
    manifest.setdefault("writes", []).append({
        "artifact": name, "module": module, "count": count,
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    })
    p.write_text(json.dumps(manifest, indent=2), encoding="utf-8")


def _fresh_manifest() -> dict:
    from helpers.config import COHORT
    return {"cohort": COHORT.get("cohort", {}).get("id", "dev"),
            "created": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "writes": []}


# ── Setup ───────────────────────────────────────────────────────────────────

_CHARTER_TEMPLATE_MARKER = "<!-- template -->"


def init(*, force: bool = False) -> Path:
    """Create the workspace, copy the group's charter in, and start the manifest."""
    r = root()
    r.mkdir(parents=True, exist_ok=True)
    manifest_path = r / SCHEMA["manifest"].path
    if not manifest_path.exists() or force:
        manifest_path.write_text(json.dumps(_fresh_manifest(), indent=2), encoding="utf-8")
    charter_src = PROJECT / "CHARTER.md"
    if charter_src.exists():
        text = charter_src.read_text(encoding="utf-8")
        if _CHARTER_TEMPLATE_MARKER not in text:
            dest = r / SCHEMA["charter"].path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(charter_src, dest)
            _record("charter", "01", len(text.splitlines()))
        else:
            print("ℹ project/CHARTER.md is still the template; the seed charter will be used until you fill it in.")
    print(f"✅ workspace ready at {r}")
    return r


def status() -> None:
    """Print every artifact and where it currently comes from."""
    width = max(len(n) for n in SCHEMA)
    for name, art in SCHEMA.items():
        src = source(name) or "—"
        print(f"{name:<{width}}  {src:<9}  {art.path}")


# ── Corpus ──────────────────────────────────────────────────────────────────


def build_corpus(*, module: str = "05") -> list[Path]:
    """Render the earlier artifacts into markdown pages under corpus/.

    One page for the charter, one per prompt pattern, one per transcript, one
    for the vibe checks. Later notebooks retrieve over these pages.
    """
    pages: dict[str, str] = {}
    pages["charter.md"] = load("charter", quiet=True)

    prompts = load("prompts", quiet=True)
    by_pattern: dict[str, list[dict]] = {}
    for r in prompts:
        by_pattern.setdefault(r["pattern"], []).append(r)
    for pattern, rows in by_pattern.items():
        body = [f"# Prompt pattern: {pattern}", ""]
        for i, r in enumerate(rows, 1):
            body += [f"## Example {i}", "", "**Input**", "", r["input"], "", "**Output**", "",
                     r["output"], "", f"_Model: {r.get('model', '')}_", ""]
        pages[f"prompts/{_slug(pattern)}.md"] = "\n".join(body)

    for t in load("transcripts", quiet=True):
        body = [f"# Transcript {t['id']}", ""]
        for turn in t["turns"]:
            body += [f"**{turn.get('role', 'user')}:** {turn.get('content', '')}", ""]
        if t.get("tool_calls"):
            body += ["## Tool calls", ""]
            for c in t["tool_calls"]:
                body += [f"- `{c.get('name', '?')}` {json.dumps(c.get('args', {}))} → {c.get('result', '')}"]
        pages[f"transcripts/{_slug(str(t['id']))}.md"] = "\n".join(body)

    try:
        vibes = load("vibe_checks", quiet=True)
        body = ["# Vibe checks", ""]
        for v in vibes:
            body += [f"## {v['id']}", "", f"**Input:** {v['input']}", "", f"**A good answer includes:** {v['expected']}", ""]
        pages["vibe_checks.md"] = "\n".join(body)
    except FileNotFoundError:
        pass

    base = save_dir("corpus", pages, module=module)
    return sorted(q for q in base.rglob("*.md"))


def _slug(text: str) -> str:
    keep = "".join(ch.lower() if ch.isalnum() else "-" for ch in text)
    while "--" in keep:
        keep = keep.replace("--", "-")
    return keep.strip("-")[:60] or "page"
