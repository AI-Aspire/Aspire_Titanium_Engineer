"""case_lookup skill: prints an eval case, a trajectory, or the closest cases as JSON.

The agent harness runs `python run.py <id or question words>` and reads the result.
It is not wired in as an API tool; the SKILL.md tells the agent when to run it.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import eval_lookup  # noqa: E402

if __name__ == "__main__":
    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print(json.dumps({"error": "give an id or the words of a question"}))
    else:
        print(json.dumps({"query": query, "result": eval_lookup.lookup(query)}))
