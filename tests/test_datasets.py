# This file was auto-generated by Fern from our API Definition.

import typing

from humanloop import CreateDatapointRequest
from humanloop.client import AsyncHumanloop, Humanloop

from .utilities import validate_response


async def test_create(client: Humanloop, async_client: AsyncHumanloop) -> None:
    expected_response: typing.Any = {
        "id": "id",
        "name": "name",
        "version_id": "version_id",
        "directory_id": "directory_id",
        "environments": [{"id": "id", "created_at": "2024-01-15T09:30:00Z", "name": "name", "tag": "default"}],
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "created_by": {"id": "id", "email_address": "email_address", "full_name": "full_name"},
        "status": "uncommitted",
        "last_used_at": "2024-01-15T09:30:00Z",
        "path": "path",
        "commit_message": "commit_message",
        "datapoints_count": 1,
        "datapoints": [
            {"inputs": {"inputs": "inputs"}, "messages": [{"role": "user"}], "target": {"target": "target"}, "id": "id"}
        ],
    }
    expected_types: typing.Any = {
        "id": None,
        "name": None,
        "version_id": None,
        "directory_id": None,
        "environments": ("list", {0: {"id": None, "created_at": "datetime", "name": None, "tag": None}}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "created_by": {"id": None, "email_address": None, "full_name": None},
        "status": None,
        "last_used_at": "datetime",
        "path": None,
        "commit_message": None,
        "datapoints_count": "integer",
        "datapoints": (
            "list",
            {
                0: {
                    "inputs": ("dict", {0: (None, None)}),
                    "messages": ("list", {0: {"role": None}}),
                    "target": ("dict", {0: (None, None)}),
                    "id": None,
                }
            },
        ),
    }
    response = client.datasets.create(datapoints=[CreateDatapointRequest()])
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.datasets.create(datapoints=[CreateDatapointRequest()])
    validate_response(async_response, expected_response, expected_types)


async def test_get(client: Humanloop, async_client: AsyncHumanloop) -> None:
    expected_response: typing.Any = {
        "id": "id",
        "name": "name",
        "version_id": "version_id",
        "directory_id": "directory_id",
        "environments": [{"id": "id", "created_at": "2024-01-15T09:30:00Z", "name": "name", "tag": "default"}],
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "created_by": {"id": "id", "email_address": "email_address", "full_name": "full_name"},
        "status": "uncommitted",
        "last_used_at": "2024-01-15T09:30:00Z",
        "path": "path",
        "commit_message": "commit_message",
        "datapoints_count": 1,
        "datapoints": [
            {"inputs": {"inputs": "inputs"}, "messages": [{"role": "user"}], "target": {"target": "target"}, "id": "id"}
        ],
    }
    expected_types: typing.Any = {
        "id": None,
        "name": None,
        "version_id": None,
        "directory_id": None,
        "environments": ("list", {0: {"id": None, "created_at": "datetime", "name": None, "tag": None}}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "created_by": {"id": None, "email_address": None, "full_name": None},
        "status": None,
        "last_used_at": "datetime",
        "path": None,
        "commit_message": None,
        "datapoints_count": "integer",
        "datapoints": (
            "list",
            {
                0: {
                    "inputs": ("dict", {0: (None, None)}),
                    "messages": ("list", {0: {"role": None}}),
                    "target": ("dict", {0: (None, None)}),
                    "id": None,
                }
            },
        ),
    }
    response = client.datasets.get(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.datasets.get(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: Humanloop, async_client: AsyncHumanloop) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.datasets.delete(id="id") is None  # type: ignore[func-returns-value]

    assert await async_client.datasets.delete(id="id") is None  # type: ignore[func-returns-value]


async def test_update(client: Humanloop, async_client: AsyncHumanloop) -> None:
    expected_response: typing.Any = {
        "id": "id",
        "name": "name",
        "version_id": "version_id",
        "directory_id": "directory_id",
        "environments": [{"id": "id", "created_at": "2024-01-15T09:30:00Z", "name": "name", "tag": "default"}],
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "created_by": {"id": "id", "email_address": "email_address", "full_name": "full_name"},
        "status": "uncommitted",
        "last_used_at": "2024-01-15T09:30:00Z",
        "path": "path",
        "commit_message": "commit_message",
        "datapoints_count": 1,
        "datapoints": [
            {"inputs": {"inputs": "inputs"}, "messages": [{"role": "user"}], "target": {"target": "target"}, "id": "id"}
        ],
    }
    expected_types: typing.Any = {
        "id": None,
        "name": None,
        "version_id": None,
        "directory_id": None,
        "environments": ("list", {0: {"id": None, "created_at": "datetime", "name": None, "tag": None}}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "created_by": {"id": None, "email_address": None, "full_name": None},
        "status": None,
        "last_used_at": "datetime",
        "path": None,
        "commit_message": None,
        "datapoints_count": "integer",
        "datapoints": (
            "list",
            {
                0: {
                    "inputs": ("dict", {0: (None, None)}),
                    "messages": ("list", {0: {"role": None}}),
                    "target": ("dict", {0: (None, None)}),
                    "id": None,
                }
            },
        ),
    }
    response = client.datasets.update(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.datasets.update(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_list_versions(client: Humanloop, async_client: AsyncHumanloop) -> None:
    expected_response: typing.Any = {
        "records": [
            {
                "id": "id",
                "name": "name",
                "version_id": "version_id",
                "directory_id": "directory_id",
                "environments": [{"id": "id", "created_at": "2024-01-15T09:30:00Z", "name": "name", "tag": "default"}],
                "created_at": "2024-01-15T09:30:00Z",
                "updated_at": "2024-01-15T09:30:00Z",
                "created_by": {"id": "id", "email_address": "email_address"},
                "status": "uncommitted",
                "last_used_at": "2024-01-15T09:30:00Z",
                "path": "path",
                "commit_message": "commit_message",
                "datapoints_count": 1,
                "datapoints": [{"id": "id"}],
            }
        ]
    }
    expected_types: typing.Any = {
        "records": (
            "list",
            {
                0: {
                    "id": None,
                    "name": None,
                    "version_id": None,
                    "directory_id": None,
                    "environments": ("list", {0: {"id": None, "created_at": "datetime", "name": None, "tag": None}}),
                    "created_at": "datetime",
                    "updated_at": "datetime",
                    "created_by": {"id": None, "email_address": None},
                    "status": None,
                    "last_used_at": "datetime",
                    "path": None,
                    "commit_message": None,
                    "datapoints_count": "integer",
                    "datapoints": ("list", {0: {"id": None}}),
                }
            },
        )
    }
    response = client.datasets.list_versions(id="id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.datasets.list_versions(id="id")
    validate_response(async_response, expected_response, expected_types)


async def test_commit(client: Humanloop, async_client: AsyncHumanloop) -> None:
    expected_response: typing.Any = {
        "id": "id",
        "name": "name",
        "version_id": "version_id",
        "directory_id": "directory_id",
        "environments": [{"id": "id", "created_at": "2024-01-15T09:30:00Z", "name": "name", "tag": "default"}],
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "created_by": {"id": "id", "email_address": "email_address", "full_name": "full_name"},
        "status": "uncommitted",
        "last_used_at": "2024-01-15T09:30:00Z",
        "path": "path",
        "commit_message": "commit_message",
        "datapoints_count": 1,
        "datapoints": [
            {"inputs": {"inputs": "inputs"}, "messages": [{"role": "user"}], "target": {"target": "target"}, "id": "id"}
        ],
    }
    expected_types: typing.Any = {
        "id": None,
        "name": None,
        "version_id": None,
        "directory_id": None,
        "environments": ("list", {0: {"id": None, "created_at": "datetime", "name": None, "tag": None}}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "created_by": {"id": None, "email_address": None, "full_name": None},
        "status": None,
        "last_used_at": "datetime",
        "path": None,
        "commit_message": None,
        "datapoints_count": "integer",
        "datapoints": (
            "list",
            {
                0: {
                    "inputs": ("dict", {0: (None, None)}),
                    "messages": ("list", {0: {"role": None}}),
                    "target": ("dict", {0: (None, None)}),
                    "id": None,
                }
            },
        ),
    }
    response = client.datasets.commit(id="id", version_id="version_id", commit_message="commit_message")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.datasets.commit(
        id="id", version_id="version_id", commit_message="commit_message"
    )
    validate_response(async_response, expected_response, expected_types)


async def test_deploy(client: Humanloop, async_client: AsyncHumanloop) -> None:
    expected_response: typing.Any = {
        "id": "id",
        "name": "name",
        "version_id": "version_id",
        "directory_id": "directory_id",
        "environments": [{"id": "id", "created_at": "2024-01-15T09:30:00Z", "name": "name", "tag": "default"}],
        "created_at": "2024-01-15T09:30:00Z",
        "updated_at": "2024-01-15T09:30:00Z",
        "created_by": {"id": "id", "email_address": "email_address", "full_name": "full_name"},
        "status": "uncommitted",
        "last_used_at": "2024-01-15T09:30:00Z",
        "path": "path",
        "commit_message": "commit_message",
        "datapoints_count": 1,
        "datapoints": [
            {"inputs": {"inputs": "inputs"}, "messages": [{"role": "user"}], "target": {"target": "target"}, "id": "id"}
        ],
    }
    expected_types: typing.Any = {
        "id": None,
        "name": None,
        "version_id": None,
        "directory_id": None,
        "environments": ("list", {0: {"id": None, "created_at": "datetime", "name": None, "tag": None}}),
        "created_at": "datetime",
        "updated_at": "datetime",
        "created_by": {"id": None, "email_address": None, "full_name": None},
        "status": None,
        "last_used_at": "datetime",
        "path": None,
        "commit_message": None,
        "datapoints_count": "integer",
        "datapoints": (
            "list",
            {
                0: {
                    "inputs": ("dict", {0: (None, None)}),
                    "messages": ("list", {0: {"role": None}}),
                    "target": ("dict", {0: (None, None)}),
                    "id": None,
                }
            },
        ),
    }
    response = client.datasets.deploy(id="id", version_id="version_id", environment_id="environment_id")
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.datasets.deploy(
        id="id", version_id="version_id", environment_id="environment_id"
    )
    validate_response(async_response, expected_response, expected_types)
