.PHONY: deps execute-marimo syntax help setup setup-graph setup-optim setup-all marimo scrub lint links check check-day execute seed seed-validate banner diagrams clean

# Read-only gates run with --no-sync so they never add or remove a package.
# Anything that executes a notebook uses --all-groups so the optional groups
# are present. A bare `uv run --group dev` would uninstall them.

help:
	@echo "setup         install the shared environment (keeps optional groups already present)"
	@echo "setup-graph   add the GraphRAG group (spacy, networkx) and the spaCy model"
	@echo "setup-optim   add the prompt-optimisation group (dspy)"
	@echo "setup-all     every optional group"
	@echo "marimo        regenerate the .py mirror next to every notebook"
	@echo "scrub         remove notebook outputs that must not be committed"
	@echo "lint          prose and brand lint (docs/STYLE.md)"
	@echo "links         check relative links in markdown and notebooks"
	@echo "syntax        compile every code cell and resolve every import"
	@echo "deps          every import is declared in a pyproject"
	@echo "check         what CI runs"
	@echo "check-day D=N validate the workspace through day N"
	@echo "execute F=NN  run one module's notebook for real (costs model calls)"
	@echo "execute-marimo F=NN  the same, through the marimo mirrors"
	@echo "seed          regenerate data/seed by running the notebooks"
	@echo "seed-validate validate the committed seed"
	@echo "banner        render images/banner.svg from cohort.toml"
	@echo "diagrams      render images/diagrams/src/*.dot to svg"

# `uv sync` removes anything not in the groups it was asked for, so a plain
# sync would silently uninstall a group a student installed on purpose. Keep
# every group already present. marker = a package only that group installs.
OPTIONAL_GROUPS = graph:spacy optim:dspy

setup:
	@groups=" --group dev"; \
	for pair in $(OPTIONAL_GROUPS); do \
		g=$${pair%%:*}; marker=$${pair##*:}; \
		if uv run --no-sync python -c "import $$marker" >/dev/null 2>&1; then \
			echo "keeping optional group already installed: $$g"; \
			groups="$$groups --group $$g"; \
		fi; \
	done; \
	echo "uv sync$$groups"; \
	uv sync $$groups

setup-graph:
	uv sync --group dev --group graph

setup-optim:
	uv sync --group dev --group optim

setup-all:
	uv sync --group dev --group graph --group optim

marimo:
	uv run --no-sync python scripts/make_marimo.py

scrub:
	uv run --no-sync python scripts/strip_outputs.py --scrub

lint:
	uv run --no-sync python scripts/nb_lint.py

links:
	uv run --no-sync python scripts/check_links.py

syntax:
	uv run --no-sync python scripts/check_syntax.py

deps:
	uv run --no-sync python scripts/check_deps.py

check:
	uv run --no-sync python scripts/nb_lint.py
	uv run --no-sync python scripts/check_syntax.py
	uv run --no-sync python scripts/check_deps.py
	uv run --no-sync python scripts/check_links.py
	uv run --no-sync python scripts/make_marimo.py --check
	uv run --no-sync python scripts/strip_outputs.py --check
	uv run --no-sync python scripts/check_workspace.py --seed
	uv run --no-sync python -m pytest tests/ -q

check-day:
	uv run --no-sync python scripts/check_workspace.py --day $(D)

execute:
	uv run --all-groups python scripts/check_execute.py $(F)

execute-marimo:
	uv run --all-groups python scripts/check_execute.py --marimo $(F)

seed:
	uv run --all-groups python scripts/make_seed.py

seed-validate:
	uv run --no-sync python scripts/check_workspace.py --seed

banner:
	uv run --no-sync python scripts/make_banner.py

diagrams:
	uv run --no-sync python scripts/make_diagrams.py

clean:
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
