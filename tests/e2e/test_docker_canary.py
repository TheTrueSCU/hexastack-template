"""User Journey HT-03: Hermetic Container Build & Canary Validation journey test.

Notes/Architectural Intent:
    Validates Dockerfile multi-stage build rules, rootless user security controls,
    canary drift workflow integrity, and container health check contracts without
    requiring an active external Docker daemon during hermetic test execution.
"""

from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.demo
def test_dockerfile_multi_stage_security_invariants() -> None:
    """Verify Dockerfile enforces multi-stage caching, rootless execution, and health checks."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    dockerfile_path = repo_root / "Dockerfile"
    dockerfile_exists = dockerfile_path.is_file()
    assert dockerfile_exists is True

    content = dockerfile_path.read_text(encoding="utf-8")

    # 1. Multi-stage builder & runtime isolation
    assert "AS builder" in content
    assert "AS runtime" in content
    assert "uv:python3.13" in content

    # 2. Rootless security user declaration
    assert "useradd -r -u 10001 -g appuser" in content
    assert "USER appuser:appuser" in content

    # 3. Healthcheck contract & ports
    assert "HEALTHCHECK" in content
    assert "http://localhost:8000/health" in content
    assert "EXPOSE 8000 50051" in content

    # 4. Entrypoint and default command
    assert 'ENTRYPOINT ["hexastack-template"]' in content
    assert 'CMD ["dev"]' in content


@pytest.mark.demo
def test_dockerignore_security_hygiene() -> None:
    """Verify .dockerignore excludes sensitive credentials, git state, and local caches."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    dockerignore_path = repo_root / ".dockerignore"
    dockerignore_exists = dockerignore_path.is_file()
    assert dockerignore_exists is True

    ignored = dockerignore_path.read_text(encoding="utf-8").splitlines()
    clean_ignored = [
        line.strip() for line in ignored if line.strip() and not line.startswith("#")
    ]

    expected_exclusions = [
        ".git",
        ".venv",
        ".pytest_cache",
        ".secrets.baseline",
        ".env",
    ]
    for exclusion in expected_exclusions:
        assert any(exclusion in line for line in clean_ignored)


@pytest.mark.demo
def test_canary_workflow_integrity() -> None:
    """Verify canary.yml workflow executes scheduled drift monitoring and pipeline visualization."""
    repo_root = Path(__file__).resolve().parent.parent.parent
    canary_path = repo_root / ".github" / "workflows" / "canary.yml"
    canary_exists = canary_path.is_file()
    assert canary_exists is True

    content = canary_path.read_text(encoding="utf-8")

    # Scheduled cron execution & workflow dispatch
    assert "schedule:" in content
    assert "workflow_dispatch:" in content

    # Hexaflow pipeline visualization
    assert "hexaflow graph render" in content
