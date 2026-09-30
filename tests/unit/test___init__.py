"""Unit tests for root package initialization."""

import hexastack_template


def test_package_has_docstring():
    """Verify root package contains module docstring."""
    doc = hexastack_template.__doc__
    assert doc is not None
