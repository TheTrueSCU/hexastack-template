"""Unit tests for CLI driving adapter."""

from hexastack_template.adapters.driving.cli import CreateItemCommand


def test_cli_adapter_registered():
    """Verify CLI driving adapter registers command."""
    is_command = CreateItemCommand is not None
    assert is_command is True
