"""Unit tests verifying Item domain model."""

from hexastack_template.domain.models import Item


def test_item_creation():
    """Verify Item entity creation with default and custom values."""
    item = Item(title="Test Item", description="Test Description")
    res_title = item.title
    res_completed = item.completed
    assert res_title == "Test Item"
    assert res_completed is False
    assert item.id is not None
