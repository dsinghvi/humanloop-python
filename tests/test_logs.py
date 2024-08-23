# This file was auto-generated by Fern from our API Definition.

import typing

from humanloop import AsyncHumanloop, Humanloop

from .utilities import validate_response


async def test_delete(client: Humanloop, async_client: AsyncHumanloop) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.logs.delete(id="string") is None  # type: ignore[func-returns-value]

    assert await async_client.logs.delete(id="string") is None  # type: ignore[func-returns-value]


async def test_get(client: Humanloop, async_client: AsyncHumanloop) -> None:
    expected_response: typing.Any = {
        "id": "log_123efg",
        "created_at": "2024-05-01T12:00:00Z",
        "output": "This is a sample output.",
        "prompt": {
            "id": "pr_123abc",
            "name": "Test Prompt",
            "path": "test-prompt",
            "version_id": "pv_456def",
            "created_at": "2024-05-01T12:00:00Z",
            "updated_at": "2024-05-01T12:00:00Z",
            "status": "committed",
            "last_used_at": "2024-05-01T12:00:00Z",
            "model": "gpt-4",
            "version_logs_count": 1,
            "total_logs_count": 1,
            "inputs": [{"name": "question"}],
        },
        "evaluator_logs": [],
    }
    expected_types: typing.Any = {
        "id": None,
        "created_at": "datetime",
        "output": None,
        "prompt": {
            "id": None,
            "name": None,
            "path": None,
            "version_id": None,
            "created_at": "datetime",
            "updated_at": "datetime",
            "status": None,
            "last_used_at": "datetime",
            "model": None,
            "version_logs_count": "integer",
            "total_logs_count": "integer",
            "inputs": ("list", {0: {"name": None}}),
        },
        "evaluator_logs": ("list", {}),
    }
    response = client.logs.get(id="prv_Wu6zx1lAWJRqOyL8nWuZk")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.logs.get(id="prv_Wu6zx1lAWJRqOyL8nWuZk")
    validate_response(async_response, expected_response, expected_types)
