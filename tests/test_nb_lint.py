"""Each lint rule fires on a fixture and stays quiet on clean text."""
import json

import nb_lint as L

CLEAN = """# Vibe checks and judges

## Learn | Create | Grow

### Learn
What a judge measures.

### Create
A judge that scores your own transcripts.

### Grow
What production adds.

**Estimated time:** 30 minutes
**Reads:** transcripts
**Writes:** judge_scores

## Setup

# Learn

## Task 1 of 2 — Score one transcript by hand

Read the transcript and give it a number. Say why in one sentence.

You should see a score between 0 and 10. Stop here if the cell prints nothing.

# Create

## Task 2 of 2 — Let the model score it

Same rubric, one model call.

## Your turn

# Grow

## From prototype to production

## Responsible controls

## Grow further
"""


def _nb(*cells):
    return {"cells": [{"cell_type": "markdown", "source": [c]} for c in cells]}


def _cells(text):
    """Split a fixture into cells on blank lines, the way a real notebook is laid out."""
    return [c for c in text.split("\n\n") if c.strip()]


def _lint(tmp_path, *cells):
    p = tmp_path / "x.ipynb"
    expanded = []
    for c in cells:
        expanded += _cells(c) if c is CLEAN else [c]
    p.write_text(json.dumps(_nb(*expanded)))
    return {f.rule for f in L.lint_notebook(p)}


def test_clean_template_passes(tmp_path):
    rules = _lint(tmp_path, CLEAN)
    assert not {r for r in rules if r.startswith(("P", "T", "B", "E", "H", "S", "K"))}, rules


def test_position_words(tmp_path):
    rules = _lint(tmp_path, CLEAN, "As you saw on Day 2, the retrieval you built yesterday is slow.")
    assert {"P002", "P005"} <= rules


def test_sibling_module_reference(tmp_path):
    assert "P003" in _lint(tmp_path, CLEAN, "Reuse the judge from Demo 03.")
    assert "P008" in _lint(tmp_path, CLEAN, "Open 04_Vibe_Checks/README.md")


def test_tells(tmp_path):
    rules = _lint(tmp_path, CLEAN, "In this notebook we leverage a robust, comprehensive approach.")
    assert {"T001", "T002", "T003", "T005"} <= rules


def test_brand_strings_in_code_and_prose(tmp_path):
    p = tmp_path / "x.ipynb"
    p.write_text(json.dumps({"cells": [
        {"cell_type": "markdown", "source": [CLEAN]},
        {"cell_type": "code", "source": ["kb = load('acme_kb.md')  # from the EU AI Act demo\n"]},
    ]}))
    rules = {f.rule for f in L.lint_notebook(p)}
    assert {"B003", "B006"} <= rules


def test_length_rules(tmp_path):
    long = "word " * 151
    assert "L001" in _lint(tmp_path, CLEAN, long)
    warn = {f.rule: f.level for f in L.lint_notebook(_write(tmp_path, CLEAN, "word " * 125))}
    assert warn.get("L002") == "warn"
    assert "L003" in _lint(tmp_path, CLEAN, "You should see " + "word " * 70)


def _write(tmp_path, *cells):
    p = tmp_path / "y.ipynb"
    p.write_text(json.dumps(_nb(*cells)))
    return p


def test_exclamation_and_headers(tmp_path):
    rules = _lint(tmp_path, CLEAN, "Great, it works!\n\n## Step One: Understanding The Loop:")
    assert {"E001", "H001", "H002"} <= rules


def test_bold_emdash_emoji(tmp_path):
    rules = _lint(tmp_path, CLEAN, "**one** and **two** — plus a rocket 🚀 and a 🎉")
    assert {"S001", "S002", "S003"} <= rules
    assert "S003" not in _lint(tmp_path, CLEAN, "✅ done, ❓ why, ⚠️ careful")


def test_task_numbering(tmp_path):
    bad = CLEAN.replace("## Task 2 of 2 — Let the model score it", "## Task 3 of 2 — Let the model score it")
    assert "K001" in _lint(tmp_path, *_cells(bad))
    loose = CLEAN.replace("## Task 2 of 2 — Let the model score it", "## Task, let the model score it")
    assert "K001" in _lint(tmp_path, *_cells(loose))


def test_missing_template_section(tmp_path):
    assert "K002" in _lint(tmp_path, *_cells(CLEAN.replace("## Grow further", "")))


def test_act_order(tmp_path):
    swapped = CLEAN.replace("# Create\n", "# TEMP\n").replace("# Learn\n", "# Create\n").replace("# TEMP\n", "# Learn\n")
    assert "K003" in _lint(tmp_path, *_cells(swapped))
    empty_learn = CLEAN.replace("# Learn\n\n## Task 1 of 2", "## Task 1 of 2").replace("# Create\n\n## Task 2", "# Learn\n\n# Create\n\n## Task 2")
    assert "K003" in _lint(tmp_path, *_cells(empty_learn))


def test_ignore_comment(tmp_path):
    rules = _lint(tmp_path, CLEAN, "<!-- lint: ignore S002 -->\nAn em dash — allowed here.")
    assert "S002" not in rules


def test_markdown_file_in_module_dir(tmp_path):
    d = tmp_path / "05_RAG"
    d.mkdir()
    p = d / "README.md"
    p.write_text("# RAG\n\nThis is a comprehensive guide to Day 2!\n")
    rules = {f.rule for f in L.lint_markdown(p)}
    assert {"T001", "P002", "E001"} <= rules


def test_explicit_path_skips_vendor_directories(tmp_path):
    """Linting a named directory must not walk into a module's own .venv.

    Two modules keep a virtual environment inside themselves; without this the
    lint reported thousands of findings from third-party code.
    """
    mod = tmp_path / "08_Example"
    (mod / ".venv" / "lib").mkdir(parents=True)
    (mod / ".venv" / "lib" / "vendored.py").write_text("# leverage a comprehensive approach\n")
    (mod / "README.md").write_text("# Example\n\nPlain and direct.\n")
    found = {p.name for p in L.targets([str(mod)])}
    assert "vendored.py" not in found
    assert "README.md" in found


def test_consulting_frame_rule_skips_generated_records():
    """A helpdesk model saying "the menu path for your client" is data, not voice.

    The seed is a record of what a model said and must not be hand-edited, so
    the framing rule cannot apply there. The hard brand rules still do.
    """
    kw = dict(position=False, tells=False, brand=True, ignored=set())
    text = "open a ticket for the exact menu path for your client\n[/admin][begin_admin_session]"
    seed = {f.rule for f in L._phrases(text, "data/seed/transcripts/transcripts.jsonl", **kw)}
    prose = {f.rule for f in L._phrases(text, "03_Agents_101/README.md", **kw)}
    assert "B010" not in seed and "B011" in seed
    assert "B010" in prose and "B011" in prose
