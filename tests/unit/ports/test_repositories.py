"""Unit tests verifying ItemRepositoryPort interface."""

import pytest
from hexastack_template.ports.repositories import ItemRepositoryPort


def test_item_repository_port_abstract():
    """Verify ItemRepositoryPort cannot be instantiated directly."""
    with pytest.raises(TypeError):
        ItemRepositoryPort()  # type: ignore[abstract]
