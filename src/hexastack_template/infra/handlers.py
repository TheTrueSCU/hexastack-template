"""Application CQRS command and query handlers."""

from hexastack_cqrs.infra.decorators import command_handler

from hexastack_template.domain.commands import CreateItemCommand, ItemCreatedResponse
from hexastack_template.domain.models import Item
from hexastack_template.ports.repositories import ItemRepositoryPort


@command_handler(CreateItemCommand)
class CreateItemHandler:
    """Handler processing CreateItemCommand with injected ItemRepositoryPort."""

    def __init__(self, repo: ItemRepositoryPort) -> None:
        self.repo = repo

    def __call__(self, cmd: CreateItemCommand) -> ItemCreatedResponse:
        """Handle CreateItemCommand and persist new Item.

        Args:
            cmd: Command payload with item title and description.

        Returns:
            ItemCreatedResponse with generated ID and title.
        """
        item = Item(title=cmd.title, description=cmd.description)
        self.repo.save(item)
        return ItemCreatedResponse(id=item.id, title=item.title)


def handle_create_item(
    cmd: CreateItemCommand, repo: ItemRepositoryPort
) -> ItemCreatedResponse:
    """Functional wrapper for CreateItemHandler.

    Args:
        cmd: Command payload with item title and description.
        repo: Repository port implementation.

    Returns:
        ItemCreatedResponse with generated ID and title.
    """
    return CreateItemHandler(repo)(cmd)
