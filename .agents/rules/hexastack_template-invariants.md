---
trigger: always_on
description: Architectural invariants and hexagonal boundary rules for hexastack-template.
---

## Architectural Invariants for hexastack-template

1. **Hexagonal Architecture Layer Isolation**:
   - `domain/` contains 100% pure entities, value objects, and business logic with ZERO framework imports.
   - `ports/` defines abstract ABC interfaces (`@abstractmethod`).
   - `adapters/` contains driving (HTTP, CLI, gRPC) and driven (database, cache, buses) implementations. Adapters must NEVER import from `infra/`.
   - `infra/` contains assembly, dependency injection (rodi), bootstrapper, and environment configuration.
   - Enforced by `import-linter` via `uv run lint-imports` or `hexaqual sanity`.

2. **Docstrings & Public APIs**:
   - Every public module, class, and function must have Google-style docstrings with `Args:`, `Returns:`, `Raises:`, and a `Notes/Architectural Intent:` section.

3. **1:1 Test Symmetry & Side-Effect Free Assertions**:
   - Every `src/hexastack_template/<path>.py` file requires a matching `tests/unit/<path>/test_<name>.py` and `__init__.py`.
   - In test assertions, assign method return values to variables first before evaluating `assert` to avoid CodeQL side-effect alerts.
   - Cognitive complexity must remain <= 25 per function (enforced by `complexipy`).
