"""Unit tests for adapters.driving package initialization."""

import hexastack_template.adapters.driving


def test_adapters_driving_package_loaded():
    """Verify subpackage imports cleanly."""
    doc = hexastack_template.adapters.driving.__doc__
    assert doc is not None
