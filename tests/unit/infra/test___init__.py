"""Unit tests for infra package initialization."""

import hexastack_template.infra


def test_infra_package_loaded():
    """Verify subpackage imports cleanly."""
    doc = hexastack_template.infra.__doc__
    assert doc is not None
