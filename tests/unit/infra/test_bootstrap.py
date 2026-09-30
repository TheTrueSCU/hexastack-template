"""Unit tests for application bootstrap."""

from hexastack_template.infra.bootstrap import create_app


def test_create_app_bootstraps_successfully():
    """Verify create_app constructs container without error."""
    app = create_app()
    assert app is not None
