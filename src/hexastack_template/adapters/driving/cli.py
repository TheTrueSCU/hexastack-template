"""Typer CLI driving command adapters."""

from __future__ import annotations

from hexastack_cli.infra.decorators import cli_command

from hexastack_template.domain.commands import CreateItemCommand

__all__ = [
    "CreateItemCommand",
]

cli_command("create-item", help="Create a new Item in the system.")(CreateItemCommand)
