"""Domain entities and value objects."""

from dataclasses import dataclass, field
import uuid


@dataclass
class Item:
    """Domain entity representing a managed item."""

    title: str
    description: str = ''
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    completed: bool = False
