# hexastack-template

> Official enterprise Python hexagonal architecture template with CQRS, FastAPI, NiceGUI DevTools, and Day-1 AI guardrails.

Scaffolded with **[Hexastack](https://github.com/TheTrueSCU/hexastack)** — The Hexagonal Architecture Framework for Python.

## Architecture

This project enforces clean **Ports & Adapters (Hexagonal Architecture)**:

```text
src/hexastack_template/
├── domain/                      # 100% Pure Python Entities, Value Objects & CQRS Messages
│   ├── models.py
│   └── commands.py
├── ports/                       # Inverted Interfaces (Abstract Repositories & Gateways)
│   └── repositories.py
├── adapters/
│   ├── driving/                 # INBOUND Adapters (HTTP REST, CLI, UI)
│   │   ├── cli.py
│   │   └── http.py
│   └── driven/                  # OUTBOUND Adapters (Database, Outbox, External APIs)
│       └── database.py
└── infra/                       # Kernel, Bootstrapper & Dependency Injection
    ├── bootstrap.py
    └── config.py
```

## Getting Started

```bash
# 1. Install dependencies & pre-commit hooks
uv sync
uv run pre-commit install

# 2. Run test suite & coverage
uv run pytest

# 3. Launch interactive development environment
uv run hexastack-template dev
```
