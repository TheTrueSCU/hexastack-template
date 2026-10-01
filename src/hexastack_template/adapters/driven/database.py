"""In-memory and persistent database adapters."""

from hexastack_template.domain.models import Item
from hexastack_template.ports.repositories import ItemRepositoryPort


class InMemoryItemRepository(ItemRepositoryPort):
    """In-memory repository adapter for local development and unit tests."""

    def __init__(self) -> None:
        self._storage: dict[str, Item] = {}

    def save(self, item: Item) -> None:
        """Persist an item into in-memory storage."""
        self._storage[item.id] = item

    def get_by_id(self, item_id: str) -> Item | None:
        """Retrieve an item by identifier from in-memory storage."""
        return self._storage.get(item_id)
