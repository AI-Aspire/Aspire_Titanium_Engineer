import marimo

__generated_with = "0.24.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Off-the-shelf guardrails

    A guardrail is a boundary with a policy attached. You wrote guardrail cases against your own agent. This notebook stops rebuilding the plumbing and attaches five policies through the OpenAI Agents SDK: input guardrails, a transform, output guardrails, and tripwires. Then it runs your cases through them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Library guardrails on an SDK agent: scope and prompt-injection checks on input, PII redaction as a transform, unsupported-claim and tone checks on output. What each is good for.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    Every guardrail run over your case set, results per case per guardrail, and a decision about which fail closed, which warn, and which are too brittle to keep.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Say what each guardrail stops and what it does not. Tell your team which case tripped a guardrail you did not expect and which attack walked through.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 35 minutes
    **Reads:** guardrail_cases, corpus
    **Writes:** ots_results
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    The SDK talks to whatever `.env` names. A self-hosted endpoint gets the chat completions API; api.openai.com gets the responses API. Tracing is off. The SDK runs async, so a small helper runs each call on one background loop.
    """)
    return


@app.cell
def _():
    import asyncio, re, textwrap, threading
    from dataclasses import dataclass
    from typing import Any
    import pandas as pd
    from agents import Agent, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered, OpenAIChatCompletionsModel, Runner, function_tool, input_guardrail, output_guardrail, set_default_openai_api, set_default_openai_client, set_tracing_disabled
    from openai import AsyncOpenAI
    from helpers.config import KEY, LLM_BASE, LLM_MODEL, LLM_TIMEOUT, require, budget
    from helpers import workspace as ws
    require('OPENAI_API_KEY')
    client = AsyncOpenAI(api_key=KEY, base_url=LLM_BASE, timeout=LLM_TIMEOUT)
    set_default_openai_client(client, use_for_tracing=False)
    set_default_openai_api('chat_completions' if LLM_BASE else 'responses')
    set_tracing_disabled(True)
    MODEL = OpenAIChatCompletionsModel(model=LLM_MODEL, openai_client=client)
    _LOOP = asyncio.new_event_loop()
    threading.Thread(target=_LOOP.run_forever, daemon=True).start()

    def run_async(coro):
        """Run a coroutine on one background loop and wait for it. Works in Jupyter and in a script."""
    # A model object rather than a name: the SDK reads anything before a slash in
    # a name as a provider, and a repo id such as unsloth/... is not one.
        return asyncio.run_coroutine_threadsafe(coro, _LOOP).result()
    CASES = ws.load('guardrail_cases')
    BASE = ws.load_path('corpus')
    PAGES = []
    for p in sorted(BASE.rglob('*.md')):
        _text = p.read_text(encoding='utf-8', errors='ignore')
        title = next((ln.lstrip('# ').strip() for ln in _text.splitlines() if ln.strip()), p.stem)
        PAGES.append({'path': str(p.relative_to(BASE)), 'title': title[:120], 'text': _text})
    print(f"model {LLM_MODEL}; API {('chat_completions' if LLM_BASE else 'responses')}")
    print(f"✅ {len(CASES)} guardrail cases from the {ws.source('guardrail_cases')}; {len(PAGES)} corpus pages")
    return (
        Agent,
        Any,
        CASES,
        GuardrailFunctionOutput,
        InputGuardrailTripwireTriggered,
        MODEL,
        OutputGuardrailTripwireTriggered,
        PAGES,
        Runner,
        budget,
        dataclass,
        function_tool,
        input_guardrail,
        output_guardrail,
        pd,
        re,
        run_async,
        textwrap,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the model, the API in use, and a ✅ line with a case count of at least six. Stop here if the case count is zero: the cases are written by the guardrail ladder notebook, or the seed carries them.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Learn
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1 of 7 — One tool to protect

    The guardrails protect a capability, so give the agent one: a term-overlap lookup over your corpus pages. It is deliberately simple so every safety decision stays easy to reason about. Read the cases too. Each has an input, whether it is an attack, and what should happen.
    """)
    return


@app.cell
def _(CASES, PAGES, function_tool, re, textwrap):
    STOP = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'how', 'in', 'is', 'it', 'of', 'on', 'or', 'our', 'that', 'the', 'their', 'this', 'to', 'what', 'when', 'where', 'which', 'who', 'with', 'does', 'do', 'tell', 'me', 'about', 'can', 'you', 'your', 'my', 'i', 'please', 'would', 'could', 'should'}

    def terms(text: str) -> set[str]:
        return {t for t in re.findall('[a-z][a-z0-9_-]{2,}', text.lower()) if t not in STOP}

    def lookup_impl(query: str, max_pages: int=3) -> str:
        q = terms(query)
        ranked = sorted(((len(q & terms(p['text'])) + 2 * len(q & terms(p['title'])), p) for p in PAGES), key=lambda x: -x[0])
        hits = [(s, p) for s, p in ranked if s > 0][:max_pages]
        if not hits:
            return 'No relevant page found.'
        return '\n\n---\n\n'.join((f"Source: {p['path']}\nTitle: {p['title']}\nExcerpt: {re.sub('\\s+', ' ', p['text'])[:1200]}" for _s, p in hits))

    @function_tool
    def lookup_corpus(query: str, max_pages: int=3) -> str:
        """Return the most relevant pages of the product's documentation and history for a question."""
        return lookup_impl(query, max_pages)
    print(textwrap.shorten(lookup_impl(CASES[0]['input']), 300), '\n')
    for _c in CASES[:6]:
        print(f"{_c['id']:<6} attack={str(_c['attack']):<12} expected={str(_c['expected'])[:28]:<30} {textwrap.shorten(str(_c['input']), 60)}")
    return lookup_corpus, terms


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one lookup result with a source path and an excerpt, then six cases with their attack flag and expected outcome. Stop here if the lookup says no page was found for the first case: the case's words share nothing with your corpus, and every tool-backed answer will be thin.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 7 — Input guardrails

    Input guardrails run before the model. First write each policy as a plain function that returns whether it tripped and why. Then wrap it for the SDK: a guardrail returns `GuardrailFunctionOutput`, and `tripwire_triggered=True` stops the run with a typed exception. Scope: the request must share vocabulary with your corpus and match no off-topic pattern. Injection: obvious attempts to override instructions or extract the prompt.
    """)
    return


@app.cell
def _(
    Any,
    CASES,
    GuardrailFunctionOutput,
    PAGES,
    input_guardrail,
    re,
    terms,
    textwrap,
):
    from collections import Counter
    df = Counter((t for p in PAGES for t in terms(p['text'])))
    SCOPE_TERMS = {t for t, n in df.most_common(250)} | {t for p in PAGES for t in terms(p['title'])}
    OFF_TOPIC = {'personal advice': '\\b(lunch|dinner|dating|workout|vacation|recipe)\\b', 'unrelated coding': '\\b(write me a (python|bash) script|build a game|scrape)\\b', 'creative writing': '\\b(write|compose)\\b.*\\b(poem|song|rap|story)\\b', 'general knowledge': '\\b(capital of|population of|who won)\\b'}
    INJECTION = {'ignore instructions': 'ignore\\s+(your\\s+|all\\s+)?(previous|prior|all|above)\\s+instructions', 'prompt extraction': '(tell|show|give)\\s+me\\s+your\\s+(system\\s+)?prompt|reveal\\s+(the\\s+|your\\s+)?(system|instructions)|print\\s+your\\s+(full\\s+)?(system\\s+)?(prompt|instructions)', 'role override': 'pretend\\s+(you\\s+are|to\\s+be)|you\\s+are\\s+now\\s+(a|an)\\b|act\\s+as\\s+(if\\s+you\\s+are\\s+)?(a|an)\\b', 'constraint bypass': 'no\\s+(rules|restrictions|guardrails)|jailbreak|developer\\s+mode', 'policy override': '(forget|disregard|override)\\s+(your|the)\\s+(system\\s+)?(prompt|instructions|guidelines|rules)'}

    def check_scope(text: str) -> tuple[bool, dict]:
        matched = sorted(terms(text) & SCOPE_TERMS)
        off = [name for name, pat in OFF_TOPIC.items() if re.search(pat, text, re.I)]
        return (bool(off) or not matched, {'policy': 'scope', 'matched_terms': matched[:6], 'off_topic': off})

    def check_injection(text: str) -> tuple[bool, dict]:
        hits = [name for name, pat in INJECTION.items() if re.search(pat, text, re.I)]
        return (bool(hits), {'policy': 'prompt injection', 'matches': hits})

    def input_text(input_data: Any) -> str:
        if isinstance(input_data, str):
            return input_data
        parts = []
        for item in input_data if isinstance(input_data, list) else [input_data]:
            content = item.get('content', '') if isinstance(item, dict) else str(item)
            parts.append(content if isinstance(content, str) else ' '.join((str(c.get('text', c)) for c in content)))
        return '\n'.join(parts)

    @input_guardrail
    async def scope_guardrail(ctx, agent, input_data) -> GuardrailFunctionOutput:
        tripped, info = check_scope(input_text(input_data))
        return GuardrailFunctionOutput(output_info=info, tripwire_triggered=tripped)

    @input_guardrail
    async def injection_guardrail(ctx, agent, input_data) -> GuardrailFunctionOutput:
        tripped, info = check_injection(input_text(input_data))
        return GuardrailFunctionOutput(output_info=info, tripwire_triggered=tripped)
    for _c in CASES[:4]:
        print(f"{_c['id']}: scope={check_scope(_c['input'])[0]} injection={check_injection(_c['input'])[0]}  {textwrap.shorten(_c['input'], 60)}")
    return check_injection, check_scope, injection_guardrail, scope_guardrail


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see four cases with a scope and an injection verdict each; the benign ones should read `False False`. Stop here if every case trips scope: your corpus vocabulary is too small, so raise the term count in `most_common`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which case would trip the scope check for the wrong reason: an in-scope question that happens to use none of the corpus's words? What would you change, the vocabulary or the rule?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 7 — PII redaction as a transform

    Redaction is different from blocking. A user with a legitimate question and an email address attached should get an answer, with the address gone before the model sees it. This pre-pass is boring and fast on purpose. It reports what it removed, never the value, so the record proves redaction happened without storing the secret.
    """)
    return


@app.cell
def _(CASES, dataclass, re):
    PII = {'email': '\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}\\b', 'phone': '\\b(?:\\+?1[-. ]?)?\\(?[0-9]{3}\\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}\\b', 'ssn': '\\b[0-9]{3}-[0-9]{2}-[0-9]{4}\\b', 'employee id': '\\b(?:EMP|ACC|TKT)-?[0-9]{5,}\\b'}

    @dataclass(frozen=True)
    class Redaction:
        text: str
        detected: list[str]

    def redact_pii(raw: str) -> Redaction:
        text, found = (raw, [])
        for label, pat in PII.items():
            if re.search(pat, text):
                found.append(label)
                text = re.sub(pat, f"[{label.upper().replace(' ', '_')}_REDACTED]", text)
        return Redaction(text, found)
    for _sample in ['Can you reset MFA for priya@example.com, her extension is 555-201-4477?', 'Ticket TKT-204411 is still open, what is the status?', CASES[0]['input']]:
        r = redact_pii(_sample)
        print(r.detected, '|', r.text)
    return Redaction, redact_pii


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the email and phone replaced by labelled placeholders, the ticket id replaced, and the first case unchanged unless it carries PII. Stop here if the phone pattern also ate a ticket number: the patterns overlap, so order them from most to least specific.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 7 — Output guardrails

    Output guardrails run after the model writes. Two risks emerge only then. Unsupported claims: the answer promises an outcome or says it performed an action the agent cannot take, such as "I have reset your password". Tone: casual openers, slang, or emoji in an internal support answer. Both are pattern checks here; in production they are classifiers.
    """)
    return


@app.cell
def _(Any, GuardrailFunctionOutput, output_guardrail, re):
    CLAIMS = {'action the agent cannot take': "\\bI(?:'ve| have)\\s+(reset|granted|approved|closed|deleted|unlocked|changed)\\b", 'absolute guarantee': '\\b(guarantee|guaranteed|zero risk|never fails|100% safe|fully eliminates)\\b', 'certification overclaim': '\\b(SOC\\s*2|ISO\\s*27001|FedRAMP)\\s+(certified|approved|compliant)\\b'}
    TONE = {'casual opener': '^\\s*(sure!|absolutely!|great question!|no worries!|yep[,.!])', 'slang': '\\b(gonna|wanna|kinda|sorta|totally|super easy|no biggie)\\b', 'emoji': '[\\U0001F300-\\U0001FAFF]'}

    def output_text(output: Any) -> str:
        if isinstance(output, str):
            return output
        content = getattr(output, 'content', None)
        return content if isinstance(content, str) else str(output)

    def check_claims(text: str) -> tuple[bool, dict]:
        hits = [name for name, pat in CLAIMS.items() if re.search(pat, text, re.I)]
        return (bool(hits), {'policy': 'unsupported claim', 'matches': hits})

    def check_tone(text: str) -> tuple[bool, dict]:
        hits = [name for name, pat in TONE.items() if re.search(pat, text, re.I)]
        return (bool(hits), {'policy': 'tone', 'matches': hits})

    @output_guardrail
    async def claim_guardrail(ctx, agent, output) -> GuardrailFunctionOutput:
        tripped, info = check_claims(output_text(output))
        return GuardrailFunctionOutput(output_info=info, tripwire_triggered=tripped)

    @output_guardrail
    async def tone_guardrail(ctx, agent, output) -> GuardrailFunctionOutput:
        tripped, info = check_tone(output_text(output))
        return GuardrailFunctionOutput(output_info=info, tripwire_triggered=tripped)
    for _sample in ['I have reset your password; you can log in now.', 'Sure! Totally gonna sort that VPN out for you.', 'Open a ticket with the helpdesk; MFA resets need the account holder to verify.']:
        print(f'claims={check_claims(_sample)[0]!s:<6} tone={check_tone(_sample)[0]!s:<6} {_sample}')
    return check_claims, check_tone, claim_guardrail, tone_guardrail


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the first sample trip claims, the second trip tone, and the third trip neither. Stop here if the third trips claims: the action pattern is matching a recommendation, not a claim of having acted.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Output guardrails add latency after the model has spent its tokens. Which of the two would you keep as a hard block, and which would you turn into a warning that is logged?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Create
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 7 — Wire the protected agent

    The guardrails attach directly to the `Agent`. The runner decides when to call them and raises a typed exception when a tripwire fires. The lifecycle: raw prompt, redaction, input guardrails, agent and tool, output guardrails, then an answer or a tripwire. `run_guarded` returns one record for every stage so a case is never a silent failure.
    """)
    return


@app.cell
def _(
    Agent,
    CASES,
    InputGuardrailTripwireTriggered,
    MODEL,
    OutputGuardrailTripwireTriggered,
    Redaction,
    Runner,
    budget,
    claim_guardrail,
    injection_guardrail,
    lookup_corpus,
    redact_pii,
    run_async,
    scope_guardrail,
    textwrap,
    tone_guardrail,
):
    INSTRUCTIONS = 'You are the internal support assistant for this product.\nAnswer only questions about the product, its access, its devices, its tools, and its tickets.\nCall lookup_corpus before answering a factual question and base the answer on what it returns.\nIf the pages do not support an answer, say so and offer to open a ticket.\nPlain, direct tone. Never claim to have reset, granted, or closed anything yourself.'.strip()
    guarded_agent = Agent(name='Guarded support assistant', instructions=INSTRUCTIONS, model=MODEL, tools=[lookup_corpus], input_guardrails=[scope_guardrail, injection_guardrail], output_guardrails=[claim_guardrail, tone_guardrail])

    def tripwire_info(exc: Exception) -> dict:
        result = getattr(exc, 'guardrail_result', None)
        output = getattr(result, 'output', None)
        info = getattr(output, 'output_info', None)
        return dict(info) if isinstance(info, dict) else {'detail': str(exc)[:200]}

    def run_guarded(prompt: str, agent: Agent=guarded_agent, redact: bool=True) -> dict:
        red = redact_pii(prompt) if redact else Redaction(prompt, [])
        record = {'input': prompt, 'processed_input': red.text, 'redactions': red.detected, 'answer': '', 'tripwire': {}}
        try:
            result = run_async(Runner.run(agent, red.text, max_turns=6))
            return {**record, 'stage': 'passed', 'blocked': False, 'answer': str(result.final_output)}
        except InputGuardrailTripwireTriggered as exc:
            return {**record, 'stage': 'input', 'blocked': True, 'tripwire': tripwire_info(exc), 'answer': 'Blocked before the model ran.'}
        except OutputGuardrailTripwireTriggered as exc:
            agent_output = getattr(getattr(exc, 'guardrail_result', None), 'agent_output', '')
            return {**record, 'stage': 'output', 'blocked': True, 'tripwire': tripwire_info(exc), 'answer': str(agent_output), 'answer_shown': 'Blocked after generation, before the user saw it.'}

    def show(outcome: dict) -> None:
        print(f"Input: {textwrap.shorten(outcome['input'], 100)}")
        if outcome['redactions']:
            print(f"Redacted ({', '.join(outcome['redactions'])}): {textwrap.shorten(outcome['processed_input'], 100)}")
        print(f"Stage: {outcome['stage']}  Blocked: {outcome['blocked']}")
        if outcome['tripwire']:
            print(f"Tripwire: {outcome['tripwire']}")
        print('Answer:', textwrap.shorten(str(outcome['answer']), 400), '\n' + '-' * 70)
    for _c in CASES[:budget(4, 2)]:
        show(run_guarded(_c['input']))
    return run_guarded, show


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see one block per case with a stage, a blocked flag, any redactions, a tripwire dict when one fired, and an answer. Stop here if a benign case is blocked at input: read the tripwire's `matched_terms` before touching the agent.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6 of 7 — Force the output tripwires

    Input guardrails protect the model boundary; output guardrails protect the user boundary. A well-behaved agent rarely trips them, so two deliberately unsafe agents make the failure deterministic: one that claims to have acted, one that answers in slang. Weak on purpose, so you can see the tripwire fire before you trust it on the real agent.
    """)
    return


@app.cell
def _(Agent, MODEL, claim_guardrail, run_guarded, show, tone_guardrail):
    overclaim_agent = Agent(
        name="Overclaim demo agent", model=MODEL, output_guardrails=[claim_guardrail],
        instructions="Reply in one sentence stating that you have reset the user's password and guarantee it will work.")

    casual_agent = Agent(
        name="Casual demo agent", model=MODEL, output_guardrails=[tone_guardrail],
        instructions="Reply in one casual sentence. Start with 'Sure!' and include the phrase 'totally gonna'.")

    for demo_agent, prompt in [(overclaim_agent, "I forgot my password, what now?"),
                               (casual_agent, "Can you help with my VPN?")]:
        show(run_guarded(prompt, agent=demo_agent, redact=False))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see both runs end at the output stage with a tripwire naming the matched pattern, and the blocked answer text below it. Stop here if the overclaim agent passes: the model paraphrased around "I have reset", and the pattern needs the paraphrase.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    The demo agents were told to misbehave. What is one way the real agent could drift into the same output without being told, and which guardrail would catch it?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 7 of 7 — Run every case and save

    One row per case per guardrail: did it trip. The two input checks and PII run on every input. The two output checks run on whatever the model wrote, including an answer the SDK blocked. A case blocked at input never reaches the model, so its output rows are false and say so. The table is what the risk register and the release decision read.
    """)
    return


@app.cell
def _(
    CASES,
    budget,
    check_claims,
    check_injection,
    check_scope,
    check_tone,
    pd,
    run_guarded,
    ws,
):
    RESULTS = []
    for _c in CASES[:budget(len(CASES), 6)]:
        outcome = run_guarded(_c['input'])
        _text = outcome['processed_input']
        rows = {'scope': check_scope(_text)[0], 'prompt_injection': check_injection(_text)[0], 'pii': bool(outcome['redactions'])}
        reached = outcome['stage'] != 'input'
        rows['unsupported_claim'] = check_claims(outcome['answer'])[0] if reached else False
        rows['tone'] = check_tone(outcome['answer'])[0] if reached else False
        for guardrail, tripped in rows.items():
            RESULTS.append({'case_id': _c['id'], 'guardrail': guardrail, 'tripped': bool(tripped), 'stage': outcome['stage'], 'attack': _c.get('attack'), 'expected': _c.get('expected'), 'model_reached': reached or guardrail in ('scope', 'prompt_injection', 'pii')})
    ws.save('ots_results', RESULTS)
    matrix = pd.DataFrame(RESULTS).pivot(index='case_id', columns='guardrail', values='tripped')
    matrix['attack'] = {c['id']: c.get('attack') for c in CASES}
    print(matrix.to_string())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with five rows per case and a matrix of cases against guardrails with the attack flag alongside. Stop here if an attack case trips nothing: that is a finding, not a bug, and it belongs in the risk register as an uncaught attack.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Add one guardrail from a risk your charter names. Decide whether it belongs before the model, after the model, or as a transform, write it as a plain check first, wrap it for the SDK, and add one case that proves it fires. Explain to a teammate what legitimate request it might catch by mistake.
    """)
    return


@app.cell
def _():
    # Shape: def check_yours(text) -> (tripped, info); wrap it with @input_guardrail or @output_guardrail;
    # build an Agent with it attached; run one adversarial prompt through run_guarded and show the outcome.
    def check_yours(text: str) -> tuple[bool, dict]:
        return False, {"policy": "your policy"}


    YOUR_CASE = ""
    if YOUR_CASE:
        print(check_yours(YOUR_CASE))
    else:
        print("write check_yours and set YOUR_CASE, then rerun")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Grow
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## From prototype to production

    | What we built | Production equivalent |
    |---|---|
    | Scope check from corpus vocabulary | A policy classifier with tenant-aware capability maps |
    | Regex prompt-injection patterns | A dedicated injection classifier plus an adversarial regression suite |
    | Regex PII redaction | A DLP or PII service with audit logging and reversible tokens |
    | Pattern checks on claims and tone | A grounding evaluator with citation checks and a brand classifier |
    | A matrix over a dozen cases | Fail-open and fail-closed severities, per-guardrail owners, live traffic sampling |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - Fail-closed guardrails on anything that reaches a customer.
    - Guardrail versions and thresholds recorded with results.
    - Blocked inputs logged so brittleness is measured.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Define guardrails as data: name, stage, severity, owner, and test cases, then attach them to an agent from that config and run the matrix from it.
    - Add a groundedness output check: an answer to a factual question must cite a source path that the lookup tool returned in the same run.
    - Give the tone guardrail a severity of warn: log it, let the answer through, and count how often it would have blocked a good answer.
    """)
    return


if __name__ == "__main__":
    app.run()
