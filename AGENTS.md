# AI Agent Workspace Guardrails

> This repository adheres to strict Hexagonal Architecture and quality governance enforced by [**Hexaqual**](https://github.com/TheTrueSCU/hexaqual).

## Active Invariants

- Domain purity: `domain/` has no external dependencies.
- Hexagonal boundaries: `adapters/` communicates exclusively via `ports/` and never imports `infra/`.
- 1:1 Test Parity: Every source module has a corresponding unit test.
- Side-effect free assertions in all test suites.
- Rule definitions live in `.agents/rules/hexastack_template-invariants.md`.
