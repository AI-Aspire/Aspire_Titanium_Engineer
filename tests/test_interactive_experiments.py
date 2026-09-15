"""Measurement and trace invariants for the extracted teaching experiments."""
import importlib.util
from pathlib import Path
from types import SimpleNamespace

import pytest
from langchain_core.messages import AIMessage, ToolMessage

ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


a = module('agentic_tools', '07_Agentic_Retrieval/agentic_tools.py')
e = module('eval_tools', '09_Agent_Evals/eval_tools.py')
r = module('research_tools', '17_Deep_Research/research_tools.py')


def test_agent_loop_records_actual_evidence_and_stops_at_budget(monkeypatch):
    call = SimpleNamespace(id='1', function=SimpleNamespace(name='read', arguments='{}'))
    message = SimpleNamespace(tool_calls=[call], content=None)
    fake = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(
        create=lambda **kw: SimpleNamespace(choices=[SimpleNamespace(message=message)]))))
    monkeypatch.setattr(a, 'client', fake, raising=False)
    result = a.run_agent('question', [], {'read': lambda: 'actual evidence'}, max_turns=2)
    assert result['stopped'] == 'max_turns'
    assert len(result['trace']) == 2
    assert result['evidence_chars'] == 2 * len('actual evidence')
    assert all(t['result'] == 'actual evidence' for t in result['trace'])


def test_tool_results_follow_call_ids_not_completion_order():
    class Agent:
        def invoke(self, payload):
            return {'messages': payload['messages'] + [
                AIMessage(content='', tool_calls=[
                    {'name': 'search_kb', 'args': {'query': 'a'}, 'id': 'a'},
                    {'name': 'search_kb', 'args': {'query': 'b'}, 'id': 'b'}]),
                ToolMessage(content='second evidence', tool_call_id='b'),
                ToolMessage(content='first evidence', tool_call_id='a'),
                AIMessage(content='answer')]}
    answer, steps = e.agent_reply(Agent(), [{'role': 'user', 'content': 'q'}])
    assert answer == 'answer'
    assert [(s['call_id'], s['result']) for s in steps] == [('a', 'first evidence'), ('b', 'second evidence')]


def test_simulator_signals_are_exact_and_hidden_task_is_not_agent_input(monkeypatch):
    seen = []
    def reply(agent, history):
        seen.append(str(history))
        return 'Please clarify.', []
    messages = iter(['I am done checking the settings; what next?', 'GIVE UP'])
    monkeypatch.setattr(e, 'agent_reply', reply)
    monkeypatch.setattr(e, 'user_sim', lambda task, history: next(messages))
    tr = e.simulate({'id': 't', 'opening': 'help', 'success': {'reference': 'HIDDEN'}}, None)
    assert len(seen) == 2
    assert tr['ended'] == 'user gave up'
    assert all('HIDDEN' not in h for h in seen)


def test_fact_check_requires_search_and_reads_all_agent_turns():
    task = {'success': {'type': 'facts', 'facts': ['entitlement', 'approval']}}
    tr = {'steps': [{'role': 'assistant', 'content': 'Request the entitlement.'},
                    {'role': 'assistant', 'content': 'Anything else?'}], 'tools': ['search_kb']}
    assert e.verify(task, tr)['pass']
    tr['tools'] = []
    assert not e.verify(task, tr)['pass']


def test_pass_power_is_all_success_not_any_success():
    assert e.pass_k([True, True, False], 2) == pytest.approx(1 / 3)
    assert e.pass_k([True, True, False], 3) == 0
    with pytest.raises(ValueError):
        e.pass_k([True], 2)


def test_failure_modes_ignores_perfect_tasks_and_orders_failure_rate():
    report = '| a | lookup | 2/3 | 0 |\n| b | decline | 0/3 | 0 |\n| c | lookup | 3/3 | 1 |'
    assert [x['task'] for x in r.failure_modes(report)] == ['b', 'a']


def test_citation_audit_handles_grouped_and_linked_sources(monkeypatch):
    monkeypatch.setattr(r, 'WEB', False, raising=False)
    state = {'tasks': ['task'], 'trace_events': [{'node': 'research', 'corpus_hits': 2, 'web_hits': 0,
             'search_sources': ['a.md', 'b.md'], 'extracted': ['a.md']}],
             'final_report': r.FinalReport(markdown='Evidence [a.md, b.md]. [invented](missing.md)',
                                          sources=['a.md', 'b.md'], gaps=[])}
    audit = r.citation_audit(state)
    assert audit['unobserved_citations'] == ['missing.md']
    assert audit['search_only_citations'] == ['b.md']


def test_research_budget_rejects_unbounded_loop_count():
    with pytest.raises(ValueError):
        r.ResearchConfig(max_researcher_loops=100)


def test_search_demonstration_exposes_the_documented_tool_interface(monkeypatch):
    monkeypatch.setattr(e, 'SECTIONS', e.sections('vpn.md', '# VPN\n\nRoute staging through the tunnel.'), raising=False)
    assert '[vpn.md > intro]' in e.search_kb.invoke({'query': 'staging tunnel'})
    assert e.search_kb.invoke({'query': 'unmatchedxyz'}) == 'No section matched.'
