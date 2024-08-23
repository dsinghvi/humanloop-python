# This file was auto-generated by Fern from our API Definition.

import typing

from ..types.tool_response import ToolResponse
from .dataset_response import DatasetResponseParams
from .evaluator_response import EvaluatorResponseParams
from .prompt_response import PromptResponseParams

FileEnvironmentResponseFileParams = typing.Union[
    PromptResponseParams, ToolResponse, DatasetResponseParams, EvaluatorResponseParams
]
