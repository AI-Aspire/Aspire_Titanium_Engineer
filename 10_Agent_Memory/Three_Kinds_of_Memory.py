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
    # Three kinds of memory

    A model has no memory of its own. Everything it remembers is something a harness chose to put back in front of it. This notebook builds that harness by hand: episodes written from your trajectories, a long-term store with embedding recall, a token-budgeted context assembler, and compaction that never loses the thread.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Learn | Create | Grow

    ### Learn
    Three kinds of memory in one loop: episodic, semantic, working. What each stores, where it lives, the test that catches its failure, and how compaction keeps a budget.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Create
    Episodes written from your trajectories, a long-term store you can read, and a MEMORY.md distilled from your own agent's runs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Grow
    Production memory is per user, scoped, and forgets on purpose. Show your team one assembled prompt's token breakdown and what was compacted.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Estimated time:** 45 minutes
    **Reads:** trajectories
    **Writes:** episodes, memory
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Setup

    One chat model and one embeddings endpoint, both from `.env`. Token counts use `tiktoken`. The memory store is a folder of markdown files in a temporary directory; the path is printed so you can open them.
    """)
    return


@app.cell
def _():
    import json, re, tempfile, textwrap
    from dataclasses import dataclass, field
    from pathlib import Path

    import numpy as np
    import tiktoken
    from openai import OpenAI

    from helpers.config import KEY, LLM_BASE, LLM_MODEL, EMBED_BASE, EMBED_MODEL, require, budget
    from helpers import workspace as ws, ui
    from helpers.llm import client

    require("OPENAI_API_KEY")
    _chat = client()
    _embed = client(base_url=EMBED_BASE)
    try:
        _enc = tiktoken.get_encoding("cl100k_base")
        def count_tokens(text: str) -> int:
            return len(_enc.encode(text or "", disallowed_special=()))
    except Exception:                       # offline: a character estimate keeps the budget maths working
        def count_tokens(text: str) -> int:
            return max(1, len(text or "") // 4)

    def chat(messages: list[dict], temperature: float = 0.2) -> str:
        r = _chat.chat.completions.create(model=LLM_MODEL, messages=messages, temperature=temperature)
        return (r.choices[0].message.content or "").strip()

    def embed(texts) -> np.ndarray:
        """Embed a list of texts to an (n, d) float32 array, L2-normalised."""
        if isinstance(texts, str):
            texts = [texts]
        out = []
        for i in range(0, len(texts), 64):
            r = _embed.embeddings.create(model=EMBED_MODEL, input=texts[i:i + 64])
            out.extend(d.embedding for d in r.data)
        arr = np.asarray(out, dtype=np.float32)
        return arr / np.clip(np.linalg.norm(arr, axis=1, keepdims=True), 1e-12, None)

    TRAJECTORIES = ws.load("trajectories")
    STORE_ROOT = Path(tempfile.mkdtemp(prefix="memory-"))
    print(f"✅ chat {LLM_MODEL}; embeddings {EMBED_MODEL}; {len(TRAJECTORIES)} trajectories; store at {STORE_ROOT}")
    return (
        Path,
        STORE_ROOT,
        TRAJECTORIES,
        budget,
        chat,
        count_tokens,
        dataclass,
        embed,
        field,
        json,
        np,
        re,
        textwrap,
        ui,
        ws,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line with both model names, a trajectory count above three, and a store path. Stop here if the count is zero: run the trajectory evals notebook first, or let the seed carry it.
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
    ## Task 1 of 7 — See the gap

    The naive agent's memory is the conversation buffer. It works inside one session and vanishes the moment the session ends. Run the same assistant twice: once with the fact in the buffer, once in a fresh session. The second answer is the gap every memory system exists to close.
    """)
    return


@app.cell
def _(TRAJECTORIES, chat, textwrap):
    SYSTEM = "You are the internal helpdesk assistant. Answer in one or two sentences."
    buffer = [{"role": "system", "content": SYSTEM}]


    def naive_turn(msg: str) -> str:
        buffer.append({"role": "user", "content": msg})
        reply = chat(buffer)
        buffer.append({"role": "assistant", "content": reply})
        return reply


    first_user = next(s["content"] for s in TRAJECTORIES[0]["steps"] if s["role"] == "user")
    naive_turn(first_user + " By the way, I am on the finance team and my laptop is a Mac.")
    print("same session:", textwrap.shorten(naive_turn("Which team am I on?"), 140))
    buffer = [{"role": "system", "content": SYSTEM}]          # a new session: the buffer is gone
    print("new session: ", textwrap.shorten(naive_turn("Which team am I on, and what laptop do I have?"), 140))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the team named in the first answer and an "I do not know" in the second. Stop here if the second answer names the team: your model call is sharing state somewhere it should not.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2 of 7 — Write episodes from your trajectories

    Episodic memory is what happened. Write each trajectory into a two-sentence episode, but pull the facts that matter from the trace, not from the model's account of itself: which tools ran, and whether the run passed. Then check the summary against the trace. A memory that records a plausible story instead of the real one is an audit trail that lies.
    """)
    return


@app.cell
def _(TRAJECTORIES, budget, chat, ui, ws):
    def observed(tr: dict) -> dict:
        """What actually happened, read from the trace."""
        steps = tr["steps"]
        return {"tools": [s["name"] for s in steps if s["role"] == "tool"],
                "user_turns": [s["content"] for s in steps if s["role"] == "user"],
                "passed": bool(tr["passed"])}


    EPISODE_SYS = ("Summarise this agent run in two sentences for a memory file: what the user wanted, what the agent did, "
                   "and whether it passed. Name every tool exactly as listed. Third person, plain, no praise.")

    EPISODES = []
    for tr in ui.track(TRAJECTORIES[:budget(10, 4)], "summarising"):
        o = observed(tr)
        transcript = "\n".join(f"{s['role']}: {s.get('content') or s.get('name')}" for s in tr["steps"])
        summary = chat([{"role": "system", "content": EPISODE_SYS},
                        {"role": "user", "content": f"passed: {o['passed']}\ntools: {sorted(set(o['tools']))}\n\n{transcript}"}])
        EPISODES.append({"id": f"ep-{tr['id']}", "summary": summary, "trajectory_id": tr["id"], "task_id": tr["task_id"],
                         "tools": o["tools"], "passed": o["passed"]})

    untrue = [e["id"] for e in EPISODES if any(t not in e["summary"] for t in set(e["tools"]))]
    print(f"{len(EPISODES)} episodes; {len(untrue)} summaries omit a tool that ran: {untrue or 'none'}")
    ws.save("episodes", EPISODES)
    print(EPISODES[0]["summary"])
    return (EPISODES,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see an episode count, a list of summaries that omit a tool the trace shows, a ✅ line, and one summary. Read one flagged summary against its trajectory. Stop here if every summary is flagged: the model is paraphrasing tool names, so tighten the prompt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Which fact in your first episode came from the trace and which came from the model? What would you lose if only the model's version were kept?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3 of 7 — A long-term store you can read

    Semantic memory is distilled facts. Keep one fact per markdown file with a small frontmatter, plus a `MEMORY.md` index loaded every session. Recall is embedding similarity on the query. Each memory carries a subject, and writing a new fact about the same subject retires the old one. That is the test that matters: not "can it recall" but "does it recall the current value".
    """)
    return


@app.cell
def _(Path, STORE_ROOT, dataclass, embed, field, np, re):
    TYPES = ('user', 'feedback', 'project', 'reference')
    _FM = re.compile('^---\\s*\\n(.*?)\\n---\\s*\\n(.*)$', re.S)

    @dataclass
    class Memory:
        name: str
        description: str
        body: str
        mtype: str = 'project'
        subject: str = ''
        vec: np.ndarray = field(default=None, repr=False)

        def to_markdown(self) -> str:
            return f'---\nname: {self.name}\ndescription: {self.description}\nsubject: {self.subject}\nmetadata:\n  type: {self.mtype}\n---\n\n{self.body.strip()}\n'

    def parse_memory(text: str, fallback: str) -> Memory:
        m = _FM.match(text.strip())
        if not m:
            return Memory(fallback, fallback, text.strip())
        fm, body = (m.group(1), m.group(2))

        def f(key):
            mm = re.search(f'^\\s*{key}:\\s*(.+)$', fm, re.M)
            return mm.group(1).strip() if mm else ''
        return Memory(f('name') or fallback, f('description') or fallback, body.strip(), f('type') or 'project', f('subject'))

    class MemoryStore:
        """One fact per markdown file, a MEMORY.md index, recall by embedding similarity."""

        def __init__(self, root: Path):
            self.root = Path(root)
            self.root.mkdir(parents=True, exist_ok=True)
            files = [f for f in sorted(self.root.glob('*.md')) if f.name != 'MEMORY.md']
            self.memories = {f.stem: parse_memory(f.read_text(encoding='utf-8'), f.stem) for f in files}
            if self.memories:
                for m, v in zip(self.memories.values(), embed([f'{m.description}\n{m.body}' for m in self.memories.values()])):
                    m.vec = v

        def write(self, name: str, description: str, body: str, mtype: str='project', subject: str='') -> Memory:
            if subject:
                for old in [k for k, m in self.memories.items() if m.subject == subject and k != name]:
                    (self.root / f'{old}.md').unlink(missing_ok=True)
                    del self.memories[old]
            mem = Memory(name, description, body, mtype, subject, embed(f'{description}\n{body}')[0])  # supersede: one current fact per subject
            self.memories[name] = mem
            (self.root / f'{name}.md').write_text(mem.to_markdown(), encoding='utf-8')
            lines = [f'- [{m.name}]({m.name}.md): {m.description}' for m in self.memories.values()]
            (self.root / 'MEMORY.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')
            return mem

        def recall(self, query: str, k: int=5) -> list[Memory]:
            mems = [m for m in self.memories.values() if m.vec is not None]
            if not mems:
                return []
            q = embed(query)[0]
            order = np.argsort(-np.array([float(m.vec @ q) for m in mems]))[:k]
            return [mems[i] for i in order]

        def index_text(self) -> str:
            p = self.root / 'MEMORY.md'
            return p.read_text(encoding='utf-8') if p.exists() else ''
    store = MemoryStore(STORE_ROOT / 'semantic')
    store.write('agent-search-tool', 'How the agent answers', 'The agent has one tool, search_kb, over the corpus pages.', 'project', subject='agent.tools')
    store.write('user-team', "The user's team", 'The user is on the finance team.', 'user', subject='user.team')
    store.write('reply-style', 'How users want replies', 'Keep replies under five lines and name the section used.', 'feedback')
    print(store.index_text())
    for _m in store.recall('which team is the user on?', k=2):
        print(f'recall -> ({_m.mtype}) {_m.name}: {_m.body}')
    return MemoryStore, TYPES, store


@app.cell
def _(store):
    store.write("user-team-now", "The user's team", "The user moved to the data platform team in June.", "user", subject="user.team")
    hits = store.recall("which team is the user on?", k=3)
    print("recalled:", [m.name for m in hits])
    stale = [m.name for m in hits if m.subject == "user.team" and "data platform" not in m.body]
    print("stale facts recalled:", stale or "none")
    print(sorted(p.name for p in store.root.glob("*.md")))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see the index, a recall that ranks the team fact first, and after the change a `user-team-now` file with the old `user-team.md` gone and no stale fact recalled. Stop here if both team facts come back: the supersede-on-subject branch did not run.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4 of 7 — Assemble working memory under a budget

    Working memory is whatever goes in the prompt this turn. The assembler stacks the tiers in priority order: instructions, recalled memories, the session summary, then the recent turns. When the total is over budget it drops recalled memories from the bottom, never the instructions or the recent turns. The breakdown shows where every token went.
    """)
    return


@app.cell
def _(count_tokens, store):
    def semantic_block(recalled: list) -> str:
        if not recalled:
            return ''
        return 'RELEVANT MEMORIES (recalled from the long-term store):\n' + '\n'.join((f'- ({m.mtype}) {m.description}\n  {m.body}' for m in recalled))

    def assemble(instructions: str, recalled: list, summary: str, recent: list[dict], *, budget_tokens: int=6000) -> dict:
        """Stack the tiers; trim recalled memories first and never the root set."""
        working = sum((count_tokens(m['content']) + 4 for m in recent))
        recalled = list(recalled)
        while True:
            sem = semantic_block(recalled)
            system = '\n\n'.join((p for p in (instructions, sem, summary) if p))
            if count_tokens(system) + working <= budget_tokens or not recalled:
                break
            recalled = recalled[:-1]
        breakdown = {'procedural (instructions)': count_tokens(instructions), 'semantic (recalled)': count_tokens(sem), 'episodic (summary)': count_tokens(summary), 'working (recent turns)': working}
        return {'messages': [{'role': 'system', 'content': system}] + recent, 'breakdown': breakdown, 'recalled': recalled}  # drop the least relevant memory
    INSTRUCTIONS = 'You are the internal helpdesk assistant. Follow recalled preferences. Name the section you used.'
    recent = [{'role': 'user', 'content': 'My VPN connects but I cannot reach staging. What should I check?'}]
    for budget_tokens in (6000, 120):
        _ctx = assemble(INSTRUCTIONS, store.recall(recent[0]['content'], k=3), '', recent, budget_tokens=budget_tokens)
        print(f"budget {budget_tokens}: {len(_ctx['recalled'])} memories kept")
        for tier, tok in _ctx['breakdown'].items():
            print(f'   {tier:<26} {tok:>5} tokens')
    print('\nthe system prompt the model sees at the small budget:\n' + _ctx['messages'][0]['content'])
    return INSTRUCTIONS, assemble


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see two breakdowns: all three memories kept at the large budget, fewer at the small one, with the instructions and the user turn unchanged in both. Stop here if the small budget dropped the instructions: the root set is being trimmed.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    At the small budget, which memory was dropped first and why? What order would be wrong for your product?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5 of 7 — Compact without losing the thread

    When the session grows past its budget, do not truncate. Compact generationally: the recent turns stay at full fidelity, older turns are condensed into a summary, and the raw text moves to an archive that stays retrievable. The proof is that a fact from a summarised turn is still answerable, and the raw turn behind it can be pulled back.
    """)
    return


@app.cell
def _(INSTRUCTIONS, assemble, chat, count_tokens, dataclass, field):
    @dataclass
    class Turn:
        role: str
        content: str

        @property
        def tokens(self) -> int:
            return count_tokens(self.content) + 4

    @dataclass
    class SummaryNode:
        text: str
        covers: int
        raw: list = field(default_factory=list)
    SUMMARISE_SYS = 'Condense this earlier slice of a conversation into a compact briefing that preserves decisions, facts, names, numbers, and open threads. Third person. It replaces the raw turns in the working context.'

    class EpisodicMemory:

        def __init__(self, budget_tokens: int=1500, keep_recent: int=6):
            self.turns: list[Turn] = []
            self.summaries: list[SummaryNode] = []
            self.archive: list[Turn] = []
            self.budget_tokens, self.keep_recent = (budget_tokens, keep_recent)
      # young: full fidelity
        def append(self, role: str, content: str) -> None:  # old: condensed
            self.turns.append(Turn(role, content))  # ancient: raw, still retrievable

        def active_tokens(self) -> int:
            return sum((t.tokens for t in self.turns)) + sum((count_tokens(s.text) for s in self.summaries))

        def maybe_compact(self) -> bool:
            if self.active_tokens() <= self.budget_tokens or len(self.turns) <= self.keep_recent:
                return False
            old, recent = (self.turns[:-self.keep_recent], self.turns[-self.keep_recent:])
            text = chat([{'role': 'system', 'content': SUMMARISE_SYS}, {'role': 'user', 'content': '\n'.join((f'{t.role}: {t.content}' for t in old))}])
            self.summaries.append(SummaryNode(text, len(old), old))
            self.archive.extend(old)
            self.turns = recent
            return True

        def summary_block(self) -> str:
            return 'EARLIER IN THIS SESSION (condensed):\n' + '\n'.join((s.text for s in self.summaries)) if self.summaries else ''

        def recent_messages(self) -> list[dict]:
            return [{'role': t.role, 'content': t.content} for t in self.turns]

        def retrieve_raw(self, query: str, k: int=4) -> list[Turn]:
            words = query.lower().split()
            scored = [(sum((w in t.content.lower() for w in words)), t) for t in self.archive]
            return [t for s, t in sorted(scored, key=lambda x: -x[0]) if s > 0][:k]
    ep = EpisodicMemory(budget_tokens=60, keep_recent=2)
    for _msg in ['My ticket number is 48213.', 'I am on the finance team.', 'The failing app is the expense portal.', 'I use a Mac.']:
        ep.append('user', _msg)
        ep.append('assistant', 'Noted.')
        print(f'compacted={str(ep.maybe_compact()):<5} active_turns={len(ep.turns)} summaries={len(ep.summaries)} archived={len(ep.archive)}')
    print('\ncondensed:', ep.summary_block() or '(none)')
    question = [{'role': 'user', 'content': 'What is my ticket number?'}]
    _ctx = assemble(INSTRUCTIONS, [], ep.summary_block(), ep.recent_messages() + question)  # tiny on purpose, to force compaction
    print('\nanswer from the summary:', chat(_ctx['messages']))
    print('raw turns behind it:', [t.content for t in ep.retrieve_raw('ticket number 48213')])
    return (EpisodicMemory,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see `compacted=True` at least once, a condensed summary that keeps the ticket number, an answer that states it, and the raw turn retrieved from the archive. Stop here if the answer does not know the number: the summary dropped it, so tighten the summarise prompt.
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
    ## Task 6 of 7 — Remember across sessions

    All three kinds in one loop. Each turn: recall from the store, log to the episode, assemble the prompt, answer, compact if needed. At session end, extract durable facts into the store. Then start a fresh harness over the same store with an empty conversation and ask. If it answers, the agent remembers without a bigger window.
    """)
    return


@app.cell
def _(
    EpisodicMemory,
    INSTRUCTIONS,
    MemoryStore,
    STORE_ROOT,
    TYPES,
    assemble,
    chat,
    json,
    re,
):
    EXTRACT_SYS = 'Review the session and decide what is worth remembering long-term: durable facts only, such as the\nuser\'s identity, stated preferences, decisions made, and project state. Not chit-chat, and nothing already in the\nexisting memory index. Return ONLY a JSON list (0-4 items) of objects:\n{"name": "<short-kebab-slug>", "description": "<one line, used later for recall>", "body": "<the fact>",\n "type": "user|feedback|project|reference", "subject": "<dotted topic such as user.team, or empty>"}'

    def slug(s: str) -> str:
        return re.sub('-+', '-', re.sub('[^a-z0-9]+', '-', s.lower())).strip('-')[:60] or 'memory'

    def parse_json_list(text: str) -> list:
        t = re.sub('^```(?:json)?\\s*|\\s*```$', '', text.strip(), flags=re.S)
        try:
            out = json.loads(t)
        except json.JSONDecodeError:
            m = re.search('\\[.*\\]', t, re.S)
            out = json.loads(m.group(0)) if m else []
        return out if isinstance(out, list) else []

    def write_facts(store_: MemoryStore, items: list) -> list[dict]:
        written = []
        for it in items:
            if isinstance(it, dict) and it.get('name') and it.get('body'):
                mtype = it.get('type') if it.get('type') in TYPES else 'project'
                store_.write(slug(it['name']), (it.get('description') or it['name']).strip(), it['body'].strip(), mtype, it.get('subject') or '')
                written.append(it)
        return written

    class MemoryHarness:

        def __init__(self, instructions: str, store_: MemoryStore, *, budget_tokens: int=6000, recall_k: int=4):
            self.instructions, self.store, self.budget_tokens, self.recall_k = (instructions, store_, budget_tokens, recall_k)
            self.episodic = EpisodicMemory()

        def turn(self, user_msg: str) -> dict:
            recalled = self.store.recall(user_msg, k=self.recall_k)
            self.episodic.append('user', user_msg)
            ctx = assemble(self.instructions, recalled, self.episodic.summary_block(), self.episodic.recent_messages(), budget_tokens=self.budget_tokens)
            reply = chat(ctx['messages'])
            self.episodic.append('assistant', reply)
            return {'reply': reply, 'recalled': ctx['recalled'], 'breakdown': ctx['breakdown'], 'compacted': self.episodic.maybe_compact()}

        def end_session(self) -> list[dict]:  # 1 prefetch (semantic)
            transcript = (self.episodic.summary_block() + '\n' + '\n'.join((f'{t.role}: {t.content}' for t in self.episodic.turns))).strip()  # 2 log (episodic)
            raw = chat([{'role': 'system', 'content': EXTRACT_SYS}, {'role': 'user', 'content': f"EXISTING MEMORY INDEX:\n{self.store.index_text() or '(empty)'}\n\nSESSION:\n{transcript}"}])
            return write_facts(self.store, parse_json_list(raw))  # 3 working
    s1 = MemoryHarness(INSTRUCTIONS, MemoryStore(STORE_ROOT / 'lifecycle'))  # 4 act
    for _msg in ["Hi, I'm Dana on the finance team. My laptop is a Mac and I mostly hit VPN problems.", 'Keep your answers short, please.']:
        s1.turn(_msg)
    written = s1.end_session()  # 5 compact
    print(f'session 1 extracted {len(written)} memories:')
    for w in written:
        print(f"   ({w.get('type')}) {w.get('name')}: {w.get('body')}")
    return EXTRACT_SYS, MemoryHarness, parse_json_list, write_facts


@app.cell
def _(INSTRUCTIONS, MemoryHarness, MemoryStore, STORE_ROOT, textwrap):
    s2 = MemoryHarness(INSTRUCTIONS, MemoryStore(STORE_ROOT / 'lifecycle'))  # fresh conversation, same store
    for _msg in ['What laptop do I have, and which team am I on?', 'How long should your answers be?']:
        r = s2.turn(_msg)
        print(f"[user] {_msg}\n   recalled: {[m.name for m in r['recalled']]}\n   {textwrap.shorten(r['reply'], 200)}\n")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see two to four extracted memories, then a fresh session that names the Mac, the finance team, and short answers, with the recalled memory names printed above each reply. Stop here if the second session recalls nothing: the store path differs between the two harnesses.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ❓ Question
    Extraction wrote what the model judged durable. Which of your episodes contains a fact it should have written and did not?

    Answer:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 7 of 7 — Write MEMORY.md

    The memory that matters for your product is about the agent, not one user: where it fails, what it relies on, what users keep asking. Distil those facts from the episodes into a project store, then render the index, the memories, and the episode log into one file. Later notebooks read it.
    """)
    return


@app.cell
def _(
    EPISODES,
    EXTRACT_SYS,
    MemoryStore,
    STORE_ROOT,
    chat,
    parse_json_list,
    write_facts,
    ws,
):
    AGENT_EXTRACT_SYS = EXTRACT_SYS.replace("the\nuser's identity, stated preferences, decisions made, and project state", 'what the agent is good at, where it fails, and which tools it relies on')
    episode_log = '\n'.join((f"- [{e['id']}] task={e['task_id']} passed={e['passed']} tools={sorted(set(e['tools']))}: {e['summary']}" for e in EPISODES))
    agent_store = MemoryStore(STORE_ROOT / 'agent')
    facts = write_facts(agent_store, parse_json_list(chat([{'role': 'system', 'content': AGENT_EXTRACT_SYS}, {'role': 'user', 'content': 'EXISTING MEMORY INDEX:\n(empty)\n\nSESSION:\n' + episode_log}])))
    lines = ['# MEMORY.md', '', f'Long-term memory for the agent under test, distilled from {len(EPISODES)} episodes.', '', '## Index', ''] + [f'- {m.name}: {m.description}' for m in agent_store.memories.values()]
    lines += ['', '## Memories', '']
    for _m in agent_store.memories.values():
        lines += [f'### {_m.name}', '', f'type: {_m.mtype}' + (f'; subject: {_m.subject}' if _m.subject else ''), '', _m.body, '']
    lines += ['## Episodes', ''] + [f"- {e['id']} (task {e['task_id']}, {('passed' if e['passed'] else 'failed')}): {e['summary']}" for e in EPISODES]
    MEMORY = '\n'.join(lines)
    ws.save('memory', MEMORY)
    # The store on disk links each index line to its file; this bundle carries the
    # memories inline, so the index names them rather than linking to files that are not here.
    print(MEMORY[:1500])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should see a ✅ line and the top of MEMORY.md with an index, at least two memories about the agent, and one line per episode. Stop here if the index is empty: the extraction returned no JSON list, so print the raw reply and fix the prompt.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Your turn

    Run the leakage test. Two users share the same assistant and the same question. Give each a store keyed by user, have each state a ticket number, end both sessions, then ask as the second user. Explain to a teammate what happens if the store is keyed by anything less specific than the user.
    """)
    return


@app.cell
def _(INSTRUCTIONS, MemoryHarness, MemoryStore, STORE_ROOT):
    alice = MemoryHarness(INSTRUCTIONS, MemoryStore(STORE_ROOT / "users" / "alice"))
    bob = MemoryHarness(INSTRUCTIONS, MemoryStore(STORE_ROOT / "users" / "bob"))
    alice.turn("I'm Alice in finance and my open ticket is 11111.")
    alice.end_session()
    bob.turn("I'm Bob in legal and my open ticket is 22222.")
    bob.end_session()
    answer = MemoryHarness(INSTRUCTIONS, MemoryStore(STORE_ROOT / "users" / "bob")).turn("What is my open ticket number?")["reply"]
    print(answer)
    print("leak:", "11111" in answer)
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
    | Markdown files plus a MEMORY.md index | A SQLite or vector store behind the same write and recall interface |
    | Embedding recall, top k | Hybrid recall with reranking and recency weighting |
    | Supersede on subject | Validity windows and conflict resolution |
    | Compaction with a raw archive | Generational compaction with an indexed, lossless lineage |
    | Extract at session end | Continuous extraction with dedup and merge |
    | One store per user in a folder | Per-tenant isolation, tested for leakage in the eval harness |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Responsible controls

    - Memory scoped per user; one user's memory never enters another's context.
    - A retention rule so stale facts are superseded, not accumulated.
    - A leakage test in the regression suite.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grow further

    - Index the raw archive by embedding so `retrieve_raw` is semantic, and let the agent pull a summarised turn back into working memory on demand.
    - Measure recall quality at 10, 100, and 1,000 memories. Plot the curve and find where the index stops being worth it.
    - Make the three tests above (truthfulness, staleness, leakage) run in your eval harness alongside the trajectory evals.
    """)
    return


if __name__ == "__main__":
    app.run()
