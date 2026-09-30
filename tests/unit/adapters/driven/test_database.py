"""Unit tests for InMemoryItemRepository adapter."""

from hexastack_template.adapters.driven.database import InMemoryItemRepository
from hexastack_template.domain.models import Item


def test_in_memory_repository_save_and_get():
    """Verify saving and retrieving items in memory."""
    repo = InMemoryItemRepository()
    item = Item(title="Persisted Item")
    repo.save(item)
    saved = repo.get_by_id(item.id)
    assert saved is not None
    assert saved.title == "Persisted Item"


def test_in_memory_repository_get_nonexistent():
    """Verify get_by_id returns None for nonexistent item."""
    repo = InMemoryItemRepository()
    res = repo.get_by_id("non-existent")
    assert res is None
