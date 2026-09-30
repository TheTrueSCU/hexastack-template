"""Abstract storage repository ports."""

from abc import ABC, abstractmethod
from typing import Optional
from hexastack_template.domain.models import Item


class ItemRepositoryPort(ABC):
    """Abstract repository port for persisting Item entities."""

    @abstractmethod
    def save(self, item: Item) -> None:
        """Persist an item."""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, item_id: str) -> Optional[Item]:
        """Retrieve an item by identifier."""
        raise NotImplementedError
