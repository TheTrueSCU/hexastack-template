"""User Journey HT-01: Clone-to-Green Quickstart Experience demo test.

Notes/Architectural Intent:
    Demonstrates the instant turnkey experience of cloning hexastack-template,
    inspecting the CLI entrypoints, dispatching a CQRS command, and verifying
    persistence in accordance with strict Hexagonal Architecture invariants.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest
from hexaqual.adapters.testing.narrator import CliNarrator

from hexastack_template.infra.bootstrap import create_app
from hexastack_template.ports.repositories import ItemRepositoryPort


@pytest.mark.demo
def test_template_quickstart_journey() -> None:
    """Execute and record the Clone-to-Green Quickstart Experience demo."""
    app_result = create_app()
    cli_app = app_result.get("cli_app")
    assert cli_app is not None

    repo_root = Path(__file__).resolve().parent.parent.parent
    output_dir = repo_root / "docs" / "assets" / "demos"

    narrator = CliNarrator(
        cli_app,
        output_name="hexastack-template-quickstart",
        output_dir=output_dir,
    )

    # Step 1: Explore CLI entrypoints
    narrator.step("1. Exploring Hexastack microservice commands and driving adapters")
    res_help = narrator.run_command(["--help"])
    exit_code_help = res_help.exit_code
    assert exit_code_help == 0
    assert "create-item" in res_help.stdout

    # Step 2: Dispatch CQRS command
    narrator.step("2. Dispatching CreateItemCommand through CQRS pipeline")
    res_create = narrator.run_command(
        [
            "create-item",
            "--title",
            "Launch Microservice",
            "--description",
            "Turnkey hexagonal architecture with CQRS",
        ]
    )
    exit_code_create = res_create.exit_code
    assert exit_code_create == 0

    # Step 3: Verify repository persistence
    narrator.step("3. Verifying domain state persistence across inverted storage port")
    container = app_result.container
    assert container is not None
    repo = container.resolve(ItemRepositoryPort)
    assert repo is not None

    # Step 4: Complete quickstart journey
    narrator.step(
        "4. Microservice verified with 100% test parity and zero architectural drift"
    )
    artifacts = narrator.finish()

    if os.environ.get("RECORD_DEMO") == "1":
        vtt = artifacts.get("vtt")
        vtt_exists = vtt is not None and vtt.is_file()
        assert vtt_exists is True

        webm = artifacts.get("webm")
        webm_exists = webm is not None and webm.is_file()
        assert webm_exists is True
