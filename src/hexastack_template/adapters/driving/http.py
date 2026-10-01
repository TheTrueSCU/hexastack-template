"""FastAPI REST routing adapters."""

from hexastack_fastapi.infra.decorators import api_command

from hexastack_template.domain.commands import CreateItemCommand

api_command("/items", method="POST", summary="Create a new Item")(CreateItemCommand)
