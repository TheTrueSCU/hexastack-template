"""Property-based fuzzing tests for domain entities."""

from hypothesis import given, strategies as st
from hexastack_template.domain.models import Item


@given(title=st.text(min_size=1), description=st.text())
def test_item_property_invariants(title: str, description: str):
    """Verify invariants hold across randomized item inputs."""
    item = Item(title=title, description=description)
    res_title = item.title
    res_desc = item.description
    assert res_title == title
    assert res_desc == description
    assert len(item.id) > 0
