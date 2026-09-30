"""Unit tests for HTTP driving adapter."""

import hexastack_template.adapters.driving.http as http_adapter


def test_http_adapter_loaded():
    """Verify HTTP driving adapter loads cleanly."""
    assert http_adapter is not None
