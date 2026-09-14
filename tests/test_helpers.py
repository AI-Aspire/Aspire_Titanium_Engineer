"""Shared helpers, no network."""
import re

from helpers import brand, config, judge, rag


def test_palette_is_hex():
    for k, v in brand.PALETTE.items():
        assert re.fullmatch(r"#[0-9A-Fa-f]{6}", v), k


def test_css_mentions_tokens():
    css = brand.css()
    assert brand.PALETTE["paper"] in css and brand.PALETTE["slate_900"] in css


def test_parse_judge_json_takes_last_scored_block():
    text = 'thinking {"score": 3} ... final {"score": 8, "rationale": "clear"}'
    assert judge.parse_judge_json(text)["score"] == 8


def test_parse_judge_json_handles_braces_in_strings():
    text = '{"score": 5, "rationale": "uses {curly} braces"}'
    assert judge.parse_judge_json(text)["rationale"] == "uses {curly} braces"


def test_parse_judge_json_unparseable():
    assert judge.parse_judge_json("no json here")["score"] is None


def test_parse_json_first_block():
    assert judge.parse_json('x {"a": 1} y {"b": 2}') == {"a": 1}


def test_chunk_text_overlaps():
    chunks = rag.chunk_text("abcdefghij", size=4, overlap=1)
    assert chunks == ["abcd", "defg", "ghij", "j"]


def test_budget_respects_seed_mode(monkeypatch):
    monkeypatch.setattr(config, "SEED_MODE", True)
    assert config.budget(20) == 5
    assert config.budget(20, seed=2) == 2
    monkeypatch.setattr(config, "SEED_MODE", False)
    assert config.budget(20) == 20


def test_require_names_missing(monkeypatch):
    monkeypatch.delenv("DEFINITELY_NOT_SET_XYZ", raising=False)
    try:
        config.require("DEFINITELY_NOT_SET_XYZ")
    except RuntimeError as e:
        assert "DEFINITELY_NOT_SET_XYZ" in str(e)
    else:
        raise AssertionError("expected RuntimeError")


def test_cohort_loaded():
    assert "cohort" in config.COHORT and "groups" in config.COHORT["cohort"]


def test_blank_env_value_does_not_clobber_an_exported_one(tmp_path, monkeypatch):
    """A blank line in .env means "use the default", not "erase what the caller set".

    `make seed` and `check_execute.py` export TE_WORKSPACE. A blank
    `TE_WORKSPACE=` in .env used to override it, so the notebooks wrote to the
    wrong workspace while the run still looked green.
    """
    import os

    from dotenv import load_dotenv

    env = tmp_path / ".env"
    env.write_text("TE_WORKSPACE=\nLLM_MODEL=from-dotenv\n")
    monkeypatch.setenv("TE_WORKSPACE", "data/seed")
    monkeypatch.setenv("LLM_MODEL", "from-shell")

    exported = {k: v for k, v in os.environ.items() if v.strip()}
    load_dotenv(env, override=True)
    for k, v in exported.items():           # the rule helpers.config applies
        if not os.environ.get(k, "").strip():
            os.environ[k] = v

    assert os.environ["TE_WORKSPACE"] == "data/seed"   # blank in .env, so kept
    assert os.environ["LLM_MODEL"] == "from-dotenv"    # set in .env, so it wins


def test_package_metadata_stays_light():
    """The installed package must not carry the course's pins.

    Two modules keep their own environment precisely because they pin a
    different LangChain line. They depend on this package to get the shared
    helpers, so anything heavy here makes their environment unresolvable.
    Heavy imports belong in the `course` group and stay lazy inside functions.
    """
    import tomllib
    from pathlib import Path

    root = Path(__file__).resolve().parent.parent
    with (root / "pyproject.toml").open("rb") as fh:
        cfg = tomllib.load(fh)

    declared = " ".join(cfg["project"]["dependencies"]).lower()
    for heavy in ("langchain", "qdrant", "chromadb", "deepeval", "sentence-transformers",
                  "torch", "streamlit", "jupyter"):
        assert heavy not in declared, f"{heavy} belongs in the course group, not package metadata"

    groups = cfg["dependency-groups"]
    assert "langchain" in " ".join(groups["course"]).lower()
    assert set(cfg["tool"]["uv"]["default-groups"]) >= {"course", "dev"}


def test_own_env_modules_depend_on_the_root_package():
    """Each own-environment module gets `helpers` the same way: as a path
    dependency on the root package, never a sys.path line."""
    import tomllib
    from pathlib import Path

    root = Path(__file__).resolve().parent.parent
    for name in ("08_SDG_RAGAS", "14_Voice_Agents"):
        with (root / name / "pyproject.toml").open("rb") as fh:
            cfg = tomllib.load(fh)
        deps = " ".join(cfg["project"]["dependencies"]).lower()
        assert "aspire-titanium-engineer" in deps, f"{name} cannot import helpers"
        assert "aspire-titanium-engineer" in cfg["tool"]["uv"]["sources"], f"{name} needs a path source"


def test_progress_helpers_survive_without_a_jupyter_frontend():
    """marimo and plain scripts have no IPython display handle.

    `display(..., display_id=True)` returns None there, and calling .update()
    on it used to raise from a daemon thread and kill the notebook.
    """
    from helpers import ui

    with ui.spinner("working"):
        pass
    assert list(ui.track([1, 2, 3], "counting")) == [1, 2, 3]


def test_match_persona_tolerates_a_model_that_decorates_the_name():
    """RAGAS looks personas up by the exact name the model echoes back.

    Reasoning models add the role in brackets, change the case, or drop a
    word. Each of those cost a forty-minute run before the matcher existed.
    """
    from helpers.sdg import match_persona

    names = ["Jordan Hayes", "helpdesk lead"]
    assert match_persona("Jordan Hayes", names) == "Jordan Hayes"
    assert match_persona("Jordan Hayes (Software Engineer)", names) == "Jordan Hayes"
    assert match_persona("HELPDESK  LEAD", names) == "helpdesk lead"
    assert match_persona("Helpdesk Lead: runs the queue", names) == "helpdesk lead"
    assert match_persona("Jordan Hays", names) == "Jordan Hayes"
    assert match_persona("Finance Director", names) is None
