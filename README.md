# hexastack-template

[![Use this template](https://img.shields.io/badge/GitHub-Use%20this%20template-2ea44f?logo=github)](https://github.com/TheTrueSCU/hexastack-template/generate)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/TheTrueSCU/hexastack-template?quickstart=1)
[![CI](https://github.com/TheTrueSCU/hexastack-template/actions/workflows/ci.yml/badge.svg)](https://github.com/TheTrueSCU/hexastack-template/actions/workflows/ci.yml)
[![Canary Drift Monitor](https://github.com/TheTrueSCU/hexastack-template/actions/workflows/canary.yml/badge.svg)](https://github.com/TheTrueSCU/hexastack-template/actions/workflows/canary.yml)
[![Version](https://img.shields.io/badge/version-v0.1.0-blue.svg)](https://github.com/TheTrueSCU/hexastack-template)
[![Hexastack](https://img.shields.io/static/v1?label=hexastack&message=v0.10.1&color=6366f1)](https://github.com/TheTrueSCU/hexastack)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Governed by Hexaqual](https://img.shields.io/badge/governed%20by-hexaqual-0ea5e9.svg)](https://github.com/TheTrueSCU/hexaqual)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> Official enterprise Python hexagonal architecture template with Copier support, CQRS, FastAPI, NiceGUI DevTools, and Day-1 AI guardrails.

Scaffolded with **[Hexastack](https://github.com/TheTrueSCU/hexastack)** — The Hexagonal Architecture Framework for Python.

## ⚡ Quickstart with Copier (Recommended)

Generate a production-grade microservice with customizable project name, slug, author, and subpackage modules:

```bash
# 1. Generate project interactively via Copier
uvx copier copy gh:TheTrueSCU/hexastack-template my-service

# 2. Change into the generated project directory
cd my-service

# 3. Install dependencies and initialize Git hooks
uv sync --all-groups
uv run pre-commit install

# 4. Run full test suite & coverage (>=90%)
uv run pytest

# 5. Launch interactive development environment (FastAPI + NiceGUI DevTools)
uv run my-service dev
```

### Upstream Template Updates

Projects generated with Copier can pull downstream template enhancements, security improvements, and dependency updates:

```bash
cd my-service
uvx copier update
```

---

## 🚀 1-Click Cloud Workspace

Experience the complete stack instantly in your browser (no local setup required):

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/TheTrueSCU/hexastack-template?quickstart=1)

Codespaces automatically provisions Python 3.12+, `uv`, pre-configured VS Code extensions, and launches the FastAPI service and NiceGUI DevTools console.

---

## 🎬 Interactive Demos & User Journeys

Explore verified terminal user journeys rendered headlessly via Playwright:

| User Journey | Recording | Captions | Description |
|---|---|---|---|
| **HT-01: Quickstart Experience** | [`hexastack-template-quickstart.webm`](docs/assets/demos/hexastack-template-quickstart.webm) | [WebVTT Track](docs/assets/demos/hexastack-template-quickstart.vtt) | Clone-to-green initialization, CLI inspection, and CQRS command dispatch. |
| **HT-02: Feature Slice Delivery** | [`hexastack-template-first-feature.webm`](docs/assets/demos/hexastack-template-first-feature.webm) | [WebVTT Track](docs/assets/demos/hexastack-template-first-feature.vtt) | Scaffolding an Order domain slice with 100% test parity and boundary verification. |

---

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
