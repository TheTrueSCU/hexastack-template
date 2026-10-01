"""Application CQRS command and query handlers."""

from hexastack_template.domain.commands import CreateItemCommand, ItemCreatedResponse
from hexastack_template.domain.models import Item
from hexastack_template.ports.repositories import ItemRepositoryPort


def handle_create_item(
    cmd: CreateItemCommand, repo: ItemRepositoryPort
) -> ItemCreatedResponse:
    """Handler processing CreateItemCommand."""
    item = Item(title=cmd.title, description=cmd.description)
    repo.save(item)
    return ItemCreatedResponse(id=item.id, title=item.title)
