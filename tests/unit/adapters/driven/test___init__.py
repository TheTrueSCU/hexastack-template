"""Unit tests for adapters.driven package initialization."""

import hexastack_template.adapters.driven


def test_adapters_driven_package_loaded():
    """Verify subpackage imports cleanly."""
    doc = hexastack_template.adapters.driven.__doc__
    assert doc is not None
