"""Hexagonal architecture boundary tests for hexastack_template."""

from hexastack_core.testing import assert_clean_architecture


def test_hexastack_template_clean_architecture():
    """Assert hexastack_template strictly complies with Hexagonal layer isolation."""
    assert_clean_architecture("hexastack_template")
