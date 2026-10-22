"""Unit tests for root application entrypoint."""

from unittest.mock import MagicMock, patch

import pytest

from hexastack_template.entrypoint import main


def test_entrypoint_callable():
    """Verify application entrypoint is callable."""
    is_callable = callable(main)
    assert is_callable is True


def test_entrypoint_success():
    """Verify entrypoint invokes cli_app when returned by bootstrap."""
    mock_cli = MagicMock()
    with patch(
        "hexastack_template.entrypoint.create_app",
        return_value={"cli_app": mock_cli},
    ):
        main()
        called = mock_cli.called
        assert called is True


def test_entrypoint_failure():
    """Verify entrypoint exits with code 1 when bootstrap fails."""
    with patch("hexastack_template.entrypoint.create_app", return_value={}):
        with pytest.raises(SystemExit) as exc_info:
            main()
        code = exc_info.value.code
        assert code == 1
