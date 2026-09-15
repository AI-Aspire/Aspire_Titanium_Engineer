"""The artifact contract: schema, seed fallback, validation on save."""
import json

import pytest

from helpers import workspace as ws


def test_every_artifact_has_a_producer_on_some_day():
    days = {m for mods in ws.DAYS.values() for m in mods}
    for name, art in ws.SCHEMA.items():
        assert art.producer in days, f"{name} produced by unknown module {art.producer}"


def test_paths_are_artifact_named_not_day_named():
    for art in ws.SCHEMA.values():
        assert not art.path.lower().startswith("day"), art.path


def test_validate_jsonl_requires_keys():
    assert ws.validate("prompts", [{"pattern": "x", "input": "i", "output": "o", "model": "m"}]) == []
    bad = ws.validate("prompts", [{"pattern": "x"}])
    assert bad and "missing" in bad[0]
    assert ws.validate("prompts", []) == ["must be a non-empty list of rows"]


def test_validate_json_and_md():
    assert ws.validate("rubric", {"criteria": []}) == []
    assert ws.validate("rubric", {"nope": 1})
    assert ws.validate("charter", "short")
    assert ws.validate("charter", "A charter long enough to count as real text.") == []


def test_save_then_load_prefers_workspace(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("TE_WORKSPACE", str(tmp_path))
    rows = [{"pattern": "few-shot", "input": "q", "output": "a", "model": "m"}]
    ws.save("prompts", rows)
    assert ws.source("prompts") == "workspace"
    assert ws.load("prompts") == rows
    manifest = json.loads((tmp_path / "manifest.json").read_text())
    assert manifest["writes"][-1]["artifact"] == "prompts"


def test_save_rejects_invalid(tmp_path, monkeypatch):
    monkeypatch.setenv("TE_WORKSPACE", str(tmp_path))
    with pytest.raises(ValueError):
        ws.save("prompts", [{"pattern": "only"}])


def test_load_falls_back_to_seed_with_notice(tmp_path, monkeypatch, capsys):
    monkeypatch.setenv("TE_WORKSPACE", str(tmp_path))
    if ws.source("charter") != "seed":
        pytest.skip("seed charter not present yet")
    text = ws.load("charter")
    assert isinstance(text, str) and len(text) > 20
    assert "seed" in capsys.readouterr().out


def test_load_missing_everywhere_raises(tmp_path, monkeypatch):
    monkeypatch.setenv("TE_WORKSPACE", str(tmp_path))
    monkeypatch.setattr(ws, "seed_root", lambda: tmp_path / "no-seed")
    with pytest.raises(FileNotFoundError):
        ws.load("scorecard")


def test_build_corpus_renders_pages(tmp_path, monkeypatch):
    monkeypatch.setenv("TE_WORKSPACE", str(tmp_path))
    monkeypatch.setattr(ws, "seed_root", lambda: tmp_path / "no-seed")
    ws.save("charter", "# Charter\n\nA helpdesk agent for the people who file tickets every day.")
    ws.save("prompts", [{"pattern": "persona", "input": "hi", "output": "hello", "model": "m"}])
    ws.save("transcripts", [{"id": "t1", "turns": [{"role": "user", "content": "my vpn is down"}],
                             "tool_calls": [{"name": "lookup_ticket", "args": {"id": 1}, "result": "open"}]}])
    pages = ws.build_corpus()
    names = {p.relative_to(tmp_path / "corpus").as_posix() for p in pages}
    assert {"charter.md", "prompts/persona.md", "transcripts/t1.md"} <= names
    assert ws.source("corpus") == "workspace"


def test_slug():
    assert ws._slug("Chain of Thought!") == "chain-of-thought"


def test_wiki_alone_does_not_hide_seed_corpus(tmp_path, monkeypatch):
    monkeypatch.setenv('TE_WORKSPACE', str(tmp_path / 'workspace'))
    seed = tmp_path / 'seed'
    monkeypatch.setattr(ws, 'seed_root', lambda: seed)
    (seed / 'corpus').mkdir(parents=True)
    (seed / 'corpus' / 'guide.md').write_text('# Actual corpus\n\nEvidence to retrieve.')
    ws.save('wiki', '# Wiki index\n\nNavigation generated from the seed corpus.')
    assert ws.source('wiki') == 'workspace'
    assert ws.source('corpus') == 'seed'
    assert ws.load_path('corpus') == seed / 'corpus'
    ws.save_dir('corpus', {'own.md': '# Actual group corpus\n\nGroup evidence.'})
    assert ws.source('corpus') == 'workspace'
