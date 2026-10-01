# hexastack-template

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/TheTrueSCU/hexastack-template?quickstart=1)
[![CI](https://github.com/TheTrueSCU/hexastack-template/actions/workflows/ci.yml/badge.svg)](https://github.com/TheTrueSCU/hexastack-template/actions/workflows/ci.yml)
[![Canary Drift Monitor](https://github.com/TheTrueSCU/hexastack-template/actions/workflows/canary.yml/badge.svg)](https://github.com/TheTrueSCU/hexastack-template/actions/workflows/canary.yml)
[![Hexastack](https://img.shields.io/badge/hexastack-v0.7.0-6366f1.svg)](https://github.com/TheTrueSCU/hexastack)
[![Governed by Hexaqual](https://img.shields.io/badge/governed%20by-hexaqual-0ea5e9.svg)](https://github.com/TheTrueSCU/hexaqual)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> Official enterprise Python hexagonal architecture template with CQRS, FastAPI, NiceGUI DevTools, and Day-1 AI guardrails.

Scaffolded with **[Hexastack](https://github.com/TheTrueSCU/hexastack)** — The Hexagonal Architecture Framework for Python.

## 🚀 1-Click Cloud Workspace

Experience the complete stack instantly in your browser (no local setup required):

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/TheTrueSCU/hexastack-template?quickstart=1)

Codespaces automatically provisions Python 3.12, `uv`, pre-configured VS Code extensions, and launches the FastAPI service and NiceGUI DevTools console.

## 🏛️ Architecture

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

## 🛠️ Getting Started

### Local Setup

```bash
# 1. Install dependencies & pre-commit hooks
uv sync
uv run pre-commit install

# 2. Run test suite & coverage (>=90%)
uv run pytest

# 3. Launch interactive development environment (FastAPI + NiceGUI DevTools)
uv run hexastack-template dev
```

### Endpoints & DevTools

- **API Documentation (Swagger UI)**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **Reactive DevTools Console**: `http://localhost:8000/devtools`
- **Health Check**: `http://localhost:8000/healthz`

---

## 🔒 Upstream Synchronization & Governance

This template repository is cryptographically governed and automatically synchronized in lockstep with [**Hexastack**](https://github.com/TheTrueSCU/hexastack):

- **Automated Sync**: Every upstream release of `hexastack` generates an automated, signed Pull Request updating dependencies and running full CI checks.
- **Canary Drift Monitoring**: A weekly scheduled workflow validates environment dependencies and headlessly verifies devcontainer health.
- **Strict Guardrails**: Branch protection enforces signed commits, DCO sign-offs, linear history, and 100% green test and accessibility audits.
