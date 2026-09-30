"""Shared pytest fixtures."""

import pytest
from hexastack_template.adapters.driven.database import InMemoryItemRepository


@pytest.fixture
def item_repo():
    """Provide a clean in-memory item repository fixture."""
    return InMemoryItemRepository()
