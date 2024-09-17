# This file was auto-generated by Fern from our API Definition.

import typing
from .numeric_evaluator_stats_response import NumericEvaluatorStatsResponseParams
from .boolean_evaluator_stats_response import BooleanEvaluatorStatsResponseParams
from .select_evaluator_stats_response import SelectEvaluatorStatsResponseParams
from .text_evaluator_stats_response import TextEvaluatorStatsResponseParams

VersionStatsResponseEvaluatorVersionStatsItemParams = typing.Union[
    NumericEvaluatorStatsResponseParams,
    BooleanEvaluatorStatsResponseParams,
    SelectEvaluatorStatsResponseParams,
    TextEvaluatorStatsResponseParams,
]
