"""Hexastack bootstrapper and application assembly."""

from typing import Any

from hexastack_core.infra.bootstrap import bootstrap
from hexastack_cqrs.infra.decorators import command_handler

import hexastack_template.adapters.driving.cli
import hexastack_template.adapters.driving.http
from hexastack_template.adapters.driven.database import InMemoryItemRepository
from hexastack_template.domain.commands import CreateItemCommand
from hexastack_template.infra.handlers import handle_create_item
from hexastack_template.ports.repositories import ItemRepositoryPort

# Bind command handler
command_handler(CreateItemCommand)(handle_create_item)


def create_app() -> Any:
    """Bootstrap full Hexastack microservice kernel."""
    result = bootstrap(
        packages_to_scan=[
            hexastack_template.adapters.driving.cli,
            hexastack_template.adapters.driving.http,
        ],
    )
    repo = InMemoryItemRepository()
    result.container.add_instance(repo, declared_class=ItemRepositoryPort)
    return result
