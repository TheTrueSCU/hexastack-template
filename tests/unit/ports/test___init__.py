"""Unit tests for ports package initialization."""

import hexastack_template.ports


def test_ports_package_loaded():
    """Verify subpackage imports cleanly."""
    doc = hexastack_template.ports.__doc__
    assert doc is not None
