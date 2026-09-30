"""Unit tests for CLI driving adapter."""

from hexastack_template.adapters.driving.cli import main


def test_cli_module_loaded():
    """Verify CLI main entrypoint is callable."""
    is_callable = callable(main)
    assert is_callable is True
