# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.unchecked_base_model import UncheckedBaseModel
from .evaluator_arguments_type import EvaluatorArgumentsType
from .evaluator_return_type_enum import EvaluatorReturnTypeEnum


class CodeEvaluatorRequest(UncheckedBaseModel):
    arguments_type: EvaluatorArgumentsType = pydantic.Field()
    """
    Whether this evaluator is target-free or target-required.
    """

    return_type: EvaluatorReturnTypeEnum = pydantic.Field()
    """
    The type of the return value of the evaluator.
    """

    evaluator_type: typing.Literal["python"] = "python"
    code: str = pydantic.Field()
    """
    The code for the evaluator. This code will be executed in a sandboxed environment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
