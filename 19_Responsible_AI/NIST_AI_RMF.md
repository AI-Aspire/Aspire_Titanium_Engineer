# The NIST AI risk management framework

The framework is a voluntary standard from the US National Institute of Standards and Technology. It does not tell you which model to use or which guardrail to buy. It gives you four verbs and asks you to show your work for each one. The official page, with the framework and its playbook, is at https://www.nist.gov/itl/ai-risk-management-framework.

## Govern

Who is accountable, and what are the rules. Govern is the function that runs across the other three. It answers: who owns this system, who signs off on a release, what gets logged, and what happens when a risk is found. A risk register with no owner column is a Govern failure. A rubric aspect that nobody measures is one too.

## Map

Where could this go wrong, in context. Map is done before you measure anything. It names the users, the setting, the data the system reads, and the ways it can fail. Your charter's "where it will be wrong" section is a Map artifact. So is a list of the tools an agent can call and what each one can damage.

## Measure

Can you show the risk with a number. Measure turns each mapped risk into a test with a result: a judge score, a pass rate, a faithfulness score, a count of attacks that got through. The number is only as good as the test behind it, so Measure also asks whether the judge agrees with a person and whether the test set covers the risk at all.

## Manage

What you do about it. Manage takes each measured risk and records a decision: fix it, guard it, accept it, or stop. A guardrail that blocks an attack is a Manage action, and so is a release decision that says hold. The evidence for Manage is the before and after: the attack that worked, the change, and the attack rerun.

## How the register uses them

| Function | Question | Artifact that answers it |
|---|---|---|
| Govern | Who owns it and what is unmeasured | rubric, owners |
| Map | Where will it be wrong | charter |
| Measure | Can you show it with a number | judge_scores, ragas_scores, trajectories |
| Manage | What did you do about it | ladder_results, owasp_findings |

Every row in the register names one function. If a row fits two, pick the one whose question the evidence answers.
