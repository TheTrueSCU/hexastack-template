# Architectural Decision Records (ADRs)

> This document maintains the persistent, immutable architectural decisions, foundational invariants, and rejected alternatives for projects built with **Hexastack Template**. Downstream projects generated from this template inherit these architectural guardrails and should append their own domain-specific decisions here.

---

## Index of Architectural Decisions

- [ADR-001: Strict Hexagonal Layer Boundaries & Dependency Inversion](#adr-001-strict-hexagonal-layer-boundaries--dependency-inversion)
- [ADR-002: CQRS Pattern & Mediated Pipeline Dispatch](#adr-002-cqrs-pattern--mediated-pipeline-dispatch)
- [ADR-003: Dual-Implementation Oracle Verification & Hermetic Testing](#adr-003-dual-implementation-oracle-verification--hermetic-testing)
- [ADR-004: Anti-Fake-Pass Exercise Gates & 1:1 Test Symmetry](#adr-004-anti-fake-pass-exercise-gates--11-test-symmetry)
- [ADR-005: Hexaqual Governance, Gate Audits & Day-1 AI Guardrails](#adr-005-hexaqual-governance-gate-audits--day-1-ai-guardrails)

---

## ADR-001: Strict Hexagonal Layer Boundaries & Dependency Inversion

### Context
Enterprise Python projects frequently suffer from architectural drift and framework lock-in, where database ORMs (SQLAlchemy, SQLModel), web frameworks (FastAPI), or CLI libraries bleed into core domain business rules.

### Decision
1. **Domain Purity (`domain/`)**:
   - `domain/` contains pure entities, value objects, and business logic with ZERO framework imports.
   - Pydantic models or dataclasses in domain represent pure business state.
2. **Ports as Inversion Boundaries (`ports/`)**:
   - `ports/` defines abstract ABC interfaces (`@abstractmethod`) specifying driving (inbound) and driven (outbound) contracts.
3. **Adapters Implement Ports (`adapters/`)**:
   - `adapters/driving/` contains HTTP routes (FastAPI), CLI commands (Typer), and background workers.
   - `adapters/driven/` contains persistence (SQLAlchemy, SQLModel, in-memory) and external services.
   - Adapters must NEVER import from `infra/` or sibling adapters.
4. **Infrastructure Orchestration (`infra/`)**:
   - `infra/` bootstraps dependency injection containers (`rodi`), configuration management, and application lifecycle.
5. **Enforcement**:
   - Boundaries are continuously verified via `import-linter` (`.importlinter`) and `hexaqual sanity`.

### Rejected Alternatives
- *Direct framework imports in domain*: Rejected to ensure business logic remains testable in isolation and portable across presentation frameworks.

---

## ADR-002: CQRS Pattern & Mediated Pipeline Dispatch

### Context
Mixing write-heavy business operations (mutating state, dispatching events, enforcing transactional boundaries) with read-heavy queries leads to bloated services and complex concurrency models.

### Decision
1. **Command and Query Separation**:
   - State-changing operations are encapsulated in strongly typed `Command` objects and handled by dedicated `CommandHandler`s.
   - Read-only operations are encapsulated in `Query` objects and handled by `QueryHandler`s.
2. **Mediated Execution Pipeline**:
   - Handlers are executed through an in-memory CQRS bus supporting composable middleware (logging, metrics, authentication, validation).

### Rejected Alternatives
- *Fat Service Objects*: Rejected due to violation of Single Responsibility Principle and difficulty testing execution steps in isolation.

---

## ADR-003: Dual-Implementation Oracle Verification & Hermetic Testing

### Context
Production adapters (e.g. database repositories, caches) can exhibit edge-case behavior deviations from memory or reference implementations, leading to unexpected runtime regressions.

### Decision
1. **Hermetic In-Memory Defaults**:
   - Every driven port must have a zero-dependency in-memory reference implementation for fast, hermetic local testing without external servers.
2. **Dual-Implementation Oracle Testing**:
   - Production adapters are cross-evaluated against naive in-memory oracles via Hypothesis property-based state machines to prove functional equivalence ($f_{\text{prod}}(x) \equiv f_{\text{oracle}}(x)$).

### Rejected Alternatives
- *Testing only with live databases in all test runs*: Slows developer feedback loops and introduces test flakiness.

---

## ADR-004: Anti-Fake-Pass Exercise Gates & 1:1 Test Symmetry

### Context
Silent test omissions, empty filter matches, and side-effectful test assertions weaken code quality confidence.

### Decision
1. **Anti-Fake-Pass Exercise Gate**:
   - The test runner enforces non-zero test execution. Empty test suites are treated as fatal errors unless `--allow-empty` is explicitly specified.
2. **1:1 Test Symmetry Parity**:
   - Every module in `src/<package>/<path>.py` requires a corresponding unit test file in `tests/unit/<path>/test_<name>.py` and `__init__.py`.
   - Verified via `hexaqual parity test`.
3. **Side-Effect-Free Test Assertions**:
   - Return values must be assigned to variables prior to assertions (e.g., `res = repo.save(entity); assert res is True`) to prevent CodeQL side-effect warnings.

### Rejected Alternatives
- *Allowing empty test executions to pass*: Masks broken file globs and misconfigured test filters.

---

## ADR-005: Hexaqual Governance, Gate Audits & Day-1 AI Guardrails

### Context
Quality configurations decay as projects scale, and AI coding assistants suffer from context compaction amnesia without explicit local guardrails.

### Decision
1. **Pinned Composite Actions**:
   - CI workflows pin composite actions with immutable commit SHAs (`TheTrueSCU/hexaqual@7de5ade62e96ac7623b5ec649997e562eea2822d # v0.9.3`).
2. **Automated Quality Gate Auditing**:
   - CI executes `uv run hexaqual sanity --audit-gates` to verify all 10 canonical gates remain active.
3. **Anti-Drift Documentation Linter**:
   - CI executes `uv run hexaqual docs drift` to guarantee code and documentation stay synchronized.
4. **Day-1 AI Guardrails**:
   - Local `.agents/rules/` and `GEMINI.md` maintain active architectural invariants and re-anchoring protocols.
