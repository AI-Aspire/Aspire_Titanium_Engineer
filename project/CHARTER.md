<!-- template -->
# Charter

## The problem

Who has it, how often, and what it costs them today. One paragraph.

## The users

Name two real people or roles. What do they ask for, in their words?

## The product vision

What does the finished thing do in one sentence? What does it refuse to do?

## What a good answer looks like

Three example questions your users would ask, with what a correct answer must
contain. These become your first vibe checks.

1.
2.
3.

## Is it an agent at all

Answer each with yes or no. Fewer than two yeses means a function will do,
and a function is cheaper to test.

- Does the work take more than one step, decided as it goes?
- Does it need a tool the model does not have on its own?
- Does it have to recover when a step fails?
- Is the goal open enough that the path cannot be written down in advance?

## Five golden examples

Five inputs your users would send, each with the output you would accept and
one line on why. Write them before any model runs. They become your first
eval cases and the test your pitch is held to.

| Input | Acceptable output | Why |
|---|---|---|
| | | |

## The napkin

Tokens per request, times the price, times requests per day, next to what the
same work costs a person today. One line. The number it does not show is
latency, and that one you measure.

## Where it will be wrong

Two places you expect it to fail, and how you would notice.
