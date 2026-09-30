"""Unit tests for CQRS handlers."""

from hexastack_template.adapters.driven.database import InMemoryItemRepository
from hexastack_template.domain.commands import CreateItemCommand
from hexastack_template.infra.handlers import handle_create_item


def test_handle_create_item():
    """Verify handle_create_item persists and returns created response."""
    repo = InMemoryItemRepository()
    cmd = CreateItemCommand(title="Handled Item", description="From test")
    resp = handle_create_item(cmd, repo=repo)
    res_title = resp.title
    assert res_title == "Handled Item"
    saved = repo.get_by_id(resp.id)
    assert saved is not None
