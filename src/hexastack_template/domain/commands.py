"""CQRS command and query contracts."""

from hexastack_core.domain import Command
from pydantic import BaseModel


class CreateItemCommand(Command):
    """Command to create a new domain item."""

    title: str
    description: str = ''


class ItemCreatedResponse(BaseModel):
    """Result returned after item creation."""

    id: str
    title: str
