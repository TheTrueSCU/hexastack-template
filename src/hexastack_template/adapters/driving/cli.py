"""Typer CLI entrypoint and driving command adapters."""

import sys

from hexastack_cli.infra.decorators import cli_command

from hexastack_template.domain.commands import CreateItemCommand

cli_command("create-item", help="Create a new Item in the system.")(CreateItemCommand)


def main() -> None:
    """CLI entrypoint."""
    from hexastack_template.infra.bootstrap import create_app

    app = create_app()
    cli_app = app.get("cli_app")
    if cli_app is not None:
        cli_app()
    else:
        sys.stderr.write("CLI application failed to bootstrap.\n")
        sys.exit(1)
