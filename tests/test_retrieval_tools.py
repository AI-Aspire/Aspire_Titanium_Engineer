"""Checks for the measurement and label boundaries of the callable ladder."""
import importlib.util
import json
from pathlib import Path

import pytest

PATH = Path(__file__).resolve().parents[1] / '06_Advanced_Retrieval' / 'retrieval_tools.py'
spec = importlib.util.spec_from_file_location('retrieval_tools', PATH)
tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)


def test_rrf_rewards_agreement_and_uses_one_based_ranks():
    # B's two rank-2 votes beat either document appearing once at rank 1.
    assert tools.rrf([[0, 1], [2, 1]]) == [1, 0, 2]
    assert tools.rrf([]) == []


def test_metrics_are_page_based_with_misses_and_duplicate_chunks():
    case = {'pages': ['answer.md']}
    pages = ['distractor.md', 'distractor.md', 'answer.md', 'answer.md']
    assert tools.score_case(case, [0, 1, 2, 3], pages) == (1.0, 1 / 3)
    assert tools.score_case(case, [3, 2], pages) == (1.0, 1.0)
    assert tools.score_case(case, [0, 1], pages) == (0.0, 0.0)
    assert tools.score_case(case, [], pages) == (0.0, 0.0)


def test_reject_labels_from_another_corpus(tmp_path):
    path = tmp_path / 'cases.json'
    path.write_text(json.dumps([{'id': 'c1', 'question': 'q', 'reference': 'answer', 'pages': ['missing.md']}]))
    with pytest.raises(ValueError, match='outside this corpus'):
        tools.load_cases({'present.md': 'text'}, path)


def test_skip_unlabelled_cases_and_reject_empty_denominator():
    class FakeLadder:
        page_of = ['a.md', 'b.md']
        trace = {}

        def search(self, name, question, k):
            assert question != 'skip'
            return [0, 1][:k]

        def hits(self, ranked):
            return ranked

    cases = [{'id': 'a', 'question': 'first', 'pages': ['a.md']},
             {'id': 'b', 'question': 'second', 'pages': ['b.md']},
             {'id': 'none', 'question': 'skip', 'pages': []}]
    rows, details = tools.evaluate(FakeLadder(), cases, ['bm25'], 2)
    assert rows[0]['hit_rate'] == 1.0
    assert rows[0]['mrr'] == 0.75
    assert rows[0]['cases'] == 2
    assert len(details) == 2
    with pytest.raises(ValueError, match='No cases'):
        tools.evaluate(FakeLadder(), [cases[-1]], ['bm25'], 2)
