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
    # Discovered, not listed: modules land one at a time as each is verified,
    # and the rule applies to whichever of them carry their own environment.
    for pyproject in sorted(root.glob("[0-9][0-9]_*/pyproject.toml")):
        name = pyproject.parent.name
        with pyproject.open("rb") as fh:
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


def test_litellm_model_prefixes_a_repo_id_for_a_self_hosted_server(monkeypatch):
    """A Hugging Face repo id has a slash in it and is not a litellm provider."""
    from helpers import config, llm

    monkeypatch.setattr(config, "LLM_BASE", "http://server:8888/v1")
    assert llm.litellm_model("unsloth/Qwen3.6-35B") == "openai/unsloth/Qwen3.6-35B"
    assert llm.litellm_model("gpt-5.6-luna") == "openai/gpt-5.6-luna"
    assert llm.litellm_model("openai/gpt-5.6-luna") == "openai/gpt-5.6-luna"
    monkeypatch.setattr(config, "LLM_BASE", "")
    assert llm.litellm_model("gpt-5.6-luna") == "gpt-5.6-luna"


def test_chat_model_drops_message_names_for_a_self_hosted_server(monkeypatch):
    """A self-hosted server refused a whole request over "name" on an assistant message."""
    from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
    from helpers import config, llm

    monkeypatch.setattr(config, "KEY", "sk-test")
    monkeypatch.setattr(config, "LLM_BASE", "http://server:8888/v1")
    msgs = [HumanMessage("hi", name="user1"), AIMessage("ok", name="scoper"),
            ToolMessage("42", tool_call_id="c1", name="lookup")]
    payload = llm.chat_model(model="m")._get_request_payload(msgs)
    assert [m["role"] for m in payload["messages"]] == ["user", "assistant", "tool"]
    assert not any("name" in m for m in payload["messages"] if m["role"] != "tool")
    monkeypatch.setattr(config, "LLM_BASE", None)
    payload = llm.chat_model(model="m")._get_request_payload(msgs)
    assert "name" in payload["messages"][1]


def test_local_paths_follow_the_caller_not_the_working_directory(tmp_path, monkeypatch):
    """A notebook opening `data/x` worked in Jupyter and not in marimo, whose
    working directory is wherever it was launched."""
    from pathlib import Path
    from helpers.paths import local, module_dir

    assert module_dir() == Path(__file__).resolve().parent          # a script: beside itself
    assert local("fixtures", "x") == Path(__file__).resolve().parent / "fixtures" / "x"
    monkeypatch.chdir(tmp_path)
    ns = {}
    exec("from helpers.paths import module_dir\nd = module_dir()", ns)   # a kernel: no __file__
    assert ns["d"] == tmp_path.resolve()


# ── helpers.evals ────────────────────────────────────────────────────────────

def test_bootstrap_interval_contains_the_mean():
    from helpers.evals import bootstrap_ci

    mean, low, high = bootstrap_ci([0.2, 0.4, 0.6, 0.8, 1.0], seed=1)
    assert abs(mean - 0.6) < 1e-9
    assert low <= mean <= high
    assert low < high


def test_bootstrap_is_deterministic_for_a_seed_and_moves_with_it():
    from helpers.evals import bootstrap_ci

    values = [0.11, 0.42, 0.57, 0.63, 0.78, 0.81, 0.9, 0.97]
    assert bootstrap_ci(values, seed=3) == bootstrap_ci(values, seed=3)
    assert bootstrap_ci(values, seed=3) != bootstrap_ci(values, seed=4)


def test_bootstrap_refuses_an_empty_list():
    import pytest
    from helpers.evals import bootstrap_ci

    with pytest.raises(ValueError):
        bootstrap_ci([])


def test_difference_interval_narrows_with_more_cases():
    import numpy as np
    from helpers.evals import difference_ci

    rng = np.random.default_rng(7)
    widths = []
    for n in (8, 64, 512):
        before = (rng.random(n) < 0.80).astype(float)
        after = (rng.random(n) < 0.88).astype(float)
        _, low, high = difference_ci(before, after, seed=0)
        widths.append(high - low)
    assert widths[0] > widths[1] > widths[2]


def test_difference_is_after_minus_before_and_paired_when_lengths_match():
    from helpers.evals import difference_ci

    before = [0.5, 0.5, 0.5, 0.5]
    after = [0.7, 0.7, 0.7, 0.7]
    delta, low, high = difference_ci(before, after)
    assert abs(delta - 0.2) < 1e-9
    assert abs(low - 0.2) < 1e-9 and abs(high - 0.2) < 1e-9   # paired: no spread at all


def test_difference_falls_back_to_independent_resampling_for_unequal_lengths():
    from helpers.evals import difference_ci

    delta, low, high = difference_ci([0.0, 1.0, 1.0], [1.0, 1.0, 0.0, 1.0, 1.0], seed=2)
    assert abs(delta - (0.8 - 2 / 3)) < 1e-9
    assert low <= delta <= high


def test_fingerprint_ignores_case_order_and_notices_a_changed_case():
    from helpers.evals import fingerprint

    cases = [{"id": "v01", "question": "a"}, {"id": "v02", "question": "b"}]
    fp = fingerprint(cases)
    assert len(fp) == 12 and fp == fingerprint(list(reversed(cases)))
    assert fp == fingerprint([{"id": "v01", "question": "changed"}, {"id": "v02"}])
    assert fp != fingerprint(cases + [{"id": "v03"}])
    assert fp != fingerprint(cases, keys=("id", "question"))


def test_compare_refuses_when_the_case_set_changed():
    from helpers.evals import compare

    before = {"fingerprint": "aaaaaaaaaaaa", "scores": {"faithfulness": 0.9}}
    after = {"fingerprint": "bbbbbbbbbbbb", "scores": {"faithfulness": 0.95}}
    out = compare(before, after)
    assert out["comparable"] is False and out["delta"] == {}
    assert "aaaaaaaaaaaa" in out["reason"] and "bbbbbbbbbbbb" in out["reason"]


def test_compare_reports_a_delta_per_shared_metric():
    from helpers.evals import compare

    before = {"fingerprint": "f", "scores": {"a": 0.5, "b": 0.8}}
    after = {"fingerprint": "f", "scores": {"a": 0.7, "b": 0.6, "c": 1.0}}
    out = compare(before, after)
    assert out["comparable"] is True
    assert set(out["delta"]) == {"a", "b"}
    assert abs(out["delta"]["a"] - 0.2) < 1e-9 and abs(out["delta"]["b"] + 0.2) < 1e-9


def test_gate_names_every_metric_under_its_minimum():
    from helpers.evals import gate

    out = gate({"a": 0.9, "b": 0.5, "c": 0.7}, {"a": 0.8, "b": 0.6, "c": 0.7})
    assert out == {"passed": False, "failed": ["b"]}
    assert gate({"a": 0.9}, {"a": 0.8}) == {"passed": True, "failed": []}


def test_gate_fails_a_metric_that_is_missing():
    from helpers.evals import gate

    assert gate({"a": 0.9}, {"a": 0.8, "b": 0.5}) == {"passed": False, "failed": ["b"]}
    assert gate({"a": None}, {"a": 0.0})["failed"] == ["a"]
