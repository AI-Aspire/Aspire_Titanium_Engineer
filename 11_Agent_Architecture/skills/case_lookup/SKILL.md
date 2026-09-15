---
name: case_lookup
description: Look up an eval case or an agent trajectory by id or by question, and say what it shows.
---
# case_lookup

Use this skill when the user asks about a specific eval case, a specific agent run, or whether
the agent passed a question.

1. Run `python run.py <id or the words of the question>` from this skill's directory.
2. Read the JSON it prints, then answer the user in plain English. For a case, quote the question
   and the reference answer and say which runs passed. For a trajectory, say whether it passed,
   which tools it called, and what its final answer was.
