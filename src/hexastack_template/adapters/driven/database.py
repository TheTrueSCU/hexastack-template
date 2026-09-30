"""In-memory and persistent database adapters."""

from typing import Optional
from hexastack_template.domain.models import Item
from hexastack_template.ports.repositories import ItemRepositoryPort


class InMemoryItemRepository(ItemRepositoryPort):
    """In-memory repository adapter for local development and unit tests."""

    def __init__(self) -> None:
        self._storage: dict[str, Item] = {}

    def save(self, item: Item) -> None:
        self._storage[item.id] = item

    def get_by_id(self, item_id: str) -> Optional[Item]:
        return self._storage.get(item_id)
