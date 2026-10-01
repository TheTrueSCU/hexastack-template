"""Unit tests for CLI driving adapter."""

from unittest.mock import MagicMock, patch

import pytest

from hexastack_template.adapters.driving.cli import main


def test_cli_module_loaded():
    """Verify CLI main entrypoint is callable."""
    is_callable = callable(main)
    assert is_callable is True


def test_cli_main_success():
    """Verify CLI main invokes cli_app when available."""
    mock_cli = MagicMock()
    with patch(
        "hexastack_template.infra.bootstrap.create_app",
        return_value={"cli_app": mock_cli},
    ):
        main()
        called = mock_cli.called
        assert called is True


def test_cli_main_failure():
    """Verify CLI main exits when cli_app is missing."""
    with patch("hexastack_template.infra.bootstrap.create_app", return_value={}):
        with pytest.raises(SystemExit) as exc_info:
            main()
        code = exc_info.value.code
        assert code == 1
