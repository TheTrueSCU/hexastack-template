"""Unit tests for domain package initialization."""

import hexastack_template.domain


def test_domain_package_loaded():
    """Verify subpackage imports cleanly."""
    doc = hexastack_template.domain.__doc__
    assert doc is not None
