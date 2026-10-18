"""Hexastack bootstrapper and application assembly."""

from typing import Any

from hexastack_core.infra.bootstrap import bootstrap

import hexastack_template.adapters.driving.cli
import hexastack_template.adapters.driving.http
import hexastack_template.infra.handlers
from hexastack_template.adapters.driven.database import InMemoryItemRepository
from hexastack_template.ports.repositories import ItemRepositoryPort


def create_app() -> Any:
    """Bootstrap full Hexastack microservice kernel."""
    result = bootstrap(
        packages_to_scan=[
            hexastack_template.adapters.driving.cli,
            hexastack_template.adapters.driving.http,
            hexastack_template.infra.handlers,
        ],
    )
    repo = InMemoryItemRepository()
    result.container.add_instance(repo, declared_class=ItemRepositoryPort)
    return result
