"""Unit tests verifying domain CQRS commands."""

from hexastack_template.domain.commands import CreateItemCommand, ItemCreatedResponse


def test_create_item_command():
    """Verify CreateItemCommand instantiation and field values."""
    cmd = CreateItemCommand(title="New Task", description="Details")
    res_title = cmd.title
    assert res_title == "New Task"


def test_item_created_response():
    """Verify ItemCreatedResponse model."""
    resp = ItemCreatedResponse(id="item-123", title="New Task")
    res_id = resp.id
    assert res_id == "item-123"
