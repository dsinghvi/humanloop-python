# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ..core.unchecked_base_model import UncheckedBaseModel
from .environment_response import EnvironmentResponse
from .files_tool_type import FilesToolType
from .input_response import InputResponse
from .tool_function import ToolFunction
from .user_response import UserResponse
from .version_status import VersionStatus


class ToolResponse(UncheckedBaseModel):
    """
    Request to create a new Tool.
    """

    id: str = pydantic_v1.Field()
    """
    Unique identifier for the Tool.
    """

    name: str = pydantic_v1.Field()
    """
    Name of the Tool, which is used as a unique identifier.
    """

    version_id: str = pydantic_v1.Field()
    """
    Unique identifier for the specific Tool Version. If no query params provided, the default deployed Tool Version is returned.
    """

    directory_id: typing.Optional[str] = None
    environments: typing.Optional[typing.List[EnvironmentResponse]] = pydantic_v1.Field(default=None)
    """
    The list of environments the Tool Version is deployed to.
    """

    created_at: dt.datetime
    updated_at: dt.datetime
    created_by: typing.Optional[UserResponse] = pydantic_v1.Field(default=None)
    """
    The user who created the Tool.
    """

    status: VersionStatus = pydantic_v1.Field()
    """
    The status of the Tool Version.
    """

    last_used_at: dt.datetime
    path: str = pydantic_v1.Field()
    """
    Path of the Tool, including the name, which is used as a unique identifier.
    """

    function: typing.Optional[ToolFunction] = pydantic_v1.Field(default=None)
    """
    Callable function specification of the Tool shown to the model for tool calling.
    """

    source_code: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Code source of the Tool.
    """

    setup_values: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field(default=None)
    """
    Values needed to setup the Tool, defined in JSON Schema format: https://json-schema.org/
    """

    tool_type: typing.Optional[FilesToolType] = pydantic_v1.Field(default=None)
    """
    Type of Tool.
    """

    commit_message: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Message describing the changes made.
    """

    version_logs_count: int = pydantic_v1.Field()
    """
    The number of logs that have been generated for this Tool Version
    """

    total_logs_count: int = pydantic_v1.Field()
    """
    The number of logs that have been generated across all Tool Versions
    """

    inputs: typing.List[InputResponse] = pydantic_v1.Field()
    """
    Inputs associated to the Prompt. Inputs correspond to any of the variables used within the Tool template.
    """

    signature: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Signature of the Tool.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
