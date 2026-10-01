"""Unit tests verifying ItemRepositoryPort interface."""

from hexastack_template.ports.repositories import ItemRepositoryPort


def test_item_repository_port_abstract():
    """Verify ItemRepositoryPort declares abstract methods."""
    abstract_methods = ItemRepositoryPort.__abstractmethods__
    assert abstract_methods == frozenset({"get_by_id", "save"})
