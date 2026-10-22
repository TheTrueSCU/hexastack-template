"""Application CLI entrypoint for hexastack-template."""

from __future__ import annotations

import sys

from hexastack_template.infra.bootstrap import create_app

__all__ = [
    "main",
]


def main() -> None:
    """CLI script entrypoint executing the bootstrapped application."""
    app = create_app()
    cli_app = app.get("cli_app")
    if cli_app is not None:
        cli_app()
    else:
        sys.stderr.write("CLI application failed to bootstrap.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
