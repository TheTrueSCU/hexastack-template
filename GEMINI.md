# AI Coding Assistant Protocol & Architectural Guardrails

> Primary local memory context for AI coding assistants (Antigravity CLI, Gemini, Claude, Cursor).

## Invariants & Rules
See [AGENTS.md](AGENTS.md) and [.agents/rules/hexastack_template-invariants.md](.agents/rules/hexastack_template-invariants.md).

## Commands
- `uv run hexaqual sanity`: Full pre-commit quality check (Ruff, Ty, complexipy, test parity, __all__).
- `uv run pytest`: Run unit and architecture test suites with coverage.
