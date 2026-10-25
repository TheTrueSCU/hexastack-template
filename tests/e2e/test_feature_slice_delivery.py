"""User Journey HT-02: First Domain Feature Slice Delivery demo test.

Notes/Architectural Intent:
    Demonstrates authoring a new domain model, inverted repository port,
    driven storage adapter, and CQRS command handler in accordance with Hexagonal
    Architecture, verifying layer purity and boundary isolation.
"""

from __future__ import annotations

import os
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Annotated

import pytest
import typer
from hexaqual.adapters.testing.narrator import CliNarrator
from hexastack_core.testing import assert_clean_architecture


@dataclass(frozen=True)
class Order:
    """Domain entity representing a customer order."""

    customer_id: str
    items: list[str]
    total_amount: float
    id: str = field(default_factory=lambda: str(uuid.uuid4()))


class OrderRepositoryPort(ABC):
    """Abstract port for order persistence."""

    @abstractmethod
    def save(self, order: Order) -> None:
        """Persist order."""
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, order_id: str) -> Order | None:
        """Retrieve order by ID."""
        raise NotImplementedError


class InMemoryOrderRepository(OrderRepositoryPort):
    """In-memory driven adapter for OrderRepositoryPort."""

    def __init__(self) -> None:
        self._orders: dict[str, Order] = {}

    def save(self, order: Order) -> None:
        self._orders[order.id] = order

    def get_by_id(self, order_id: str) -> Order | None:
        return self._orders.get(order_id)


@pytest.mark.demo
def test_feature_slice_delivery_journey() -> None:
    """Execute and record the First Domain Feature Slice Delivery demo."""
    app = typer.Typer(name="hexastack-template")
    repo = InMemoryOrderRepository()

    @app.command("place-order")
    def place_order_cmd(
        customer_id: Annotated[str, typer.Option("--customer-id", "-c")],
        item: Annotated[list[str], typer.Option("--item", "-i")],
        amount: Annotated[float, typer.Option("--amount", "-a")],
    ) -> None:
        """Place a new customer order."""
        order = Order(customer_id=customer_id, items=item, total_amount=amount)
        repo.save(order)
        typer.echo(
            f"Order {order.id} placed for customer {customer_id} (amount: ${amount:.2f})"
        )

    @app.command("list-orders")
    def list_orders_cmd() -> None:
        """List all placed customer orders."""
        for o in repo._orders.values():
            typer.echo(f"Order {o.id}: {o.customer_id} (${o.total_amount:.2f})")

    repo_root = Path(__file__).resolve().parent.parent.parent
    output_dir = repo_root / "docs" / "assets" / "demos"

    narrator = CliNarrator(
        app,
        output_name="hexastack-template-first-feature",
        output_dir=output_dir,
    )

    # Step 1: Explain architectural slice
    narrator.step("1. Scaffolding new domain slice: Order entity & OrderRepositoryPort")

    # Step 2: Dispatch place-order command
    narrator.step("2. Dispatching place-order driving command with items and total")
    res = narrator.run_command(
        [
            "place-order",
            "-c",
            "cust-42",
            "-i",
            "Cloud Gateway",
            "-i",
            "Event Broker",
            "-a",
            "149.99",
        ]
    )
    exit_code = res.exit_code
    assert exit_code == 0
    assert "placed for customer cust-42" in res.stdout

    # Step 3: Query orders via driving command
    narrator.step("3. Querying placed orders through list-orders driving command")
    res_list = narrator.run_command(["list-orders"])
    exit_code_list = res_list.exit_code
    assert exit_code_list == 0
    assert "cust-42" in res_list.stdout

    # Step 4: Verify persistence in repository adapter
    narrator.step("4. Verifying order state in InMemoryOrderRepository adapter")
    saved_orders = list(repo._orders.values())
    order_count = len(saved_orders)
    assert order_count == 1
    assert saved_orders[0].customer_id == "cust-42"

    # Step 5: Verify hexagonal boundary isolation
    narrator.step("5. Validating Hexagonal Architecture layer boundary isolation")
    assert_clean_architecture("hexastack_template")

    artifacts = narrator.finish()

    if os.environ.get("RECORD_DEMO") == "1":
        vtt = artifacts.get("vtt")
        vtt_exists = vtt is not None and vtt.is_file()
        assert vtt_exists is True

        webm = artifacts.get("webm")
        webm_exists = webm is not None and webm.is_file()
        assert webm_exists is True
