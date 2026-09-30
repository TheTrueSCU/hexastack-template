"""Unit tests for adapters package initialization."""

import hexastack_template.adapters


def test_adapters_package_loaded():
    """Verify subpackage imports cleanly."""
    doc = hexastack_template.adapters.__doc__
    assert doc is not None
