import typing
from typing import Optional, List, Sequence
import os
import httpx
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider

from .decorators.flow import flow
from .decorators.prompt import prompt
from .decorators.tool import tool
from humanloop.core.client_wrapper import SyncClientWrapper
from humanloop.flows.client import FlowsClient
from humanloop.tools.client import ToolsClient
from .otel.exporter import HumanloopSpanExporter
from .otel.processor import HumanloopSpanProcessor
from .otel import instrument_provider, set_tracer
from .base_client import BaseHumanloop, AsyncBaseHumanloop
from .environment import HumanloopEnvironment
from .eval_utils import _run_eval, Dataset, File, Evaluator, EvaluatorCheck
from .prompts.client import PromptsClient
from .evaluations.client import EvaluationsClient
from .prompt_utils import populate_template


class ExtendedEvalsClient(EvaluationsClient):
    client: BaseHumanloop

    def run(
        self,
        file: File,
        name: Optional[str],
        dataset: Dataset,
        evaluators: Optional[Sequence[Evaluator]] = None,
        # logs: typing.Sequence[dict] | None = None,
        workers: int = 4,
    ) -> List[EvaluatorCheck]:
        """Evaluate your function for a given `Dataset` and set of `Evaluators`.

        :param file: the Humanloop file being evaluated, including a function to run over the dataset.
        :param name: the name of the Evaluation to run. If it does not exist, a new Evaluation will be created under your File.
        :param dataset: the dataset to map your function over to produce the outputs required by the Evaluation.
        :param evaluators: define how judgments are provided for this Evaluation.
        :param workers: the number of threads to process datapoints using your function concurrently.
        :return: per Evaluator checks.
        """
        if self.client is None:
            raise ValueError("Need Humanloop client defined to run evals")

        return _run_eval(
            client=self.client,
            file=file,
            name=name,
            dataset=dataset,
            evaluators=evaluators,
            workers=workers,
        )


class ExtendedPromptsClient(PromptsClient):
    def __init__(self, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    decorate = staticmethod(prompt)
    decorate.__doc__ = prompt.__doc__
    populate_template = staticmethod(populate_template)


class ExtendedToolsClient(ToolsClient):
    def __init__(self, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    decorate = staticmethod(tool)
    decorate.__doc__ = tool.__doc__


class ExtendedFlowsClient(FlowsClient):
    def __init__(self, client_wrapper: SyncClientWrapper):
        super().__init__(client_wrapper=client_wrapper)

    decorate = staticmethod(flow)
    decorate.__doc__ = flow.__doc__


class Humanloop(BaseHumanloop):
    """
    See docstring of BaseHumanloop.

    This class extends the base client that contains the auto generated SDK functionality with custom evaluation utilities.
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: HumanloopEnvironment = HumanloopEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("HUMANLOOP_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        """See docstring of BaseHumanloop.__init__(...)

        This method extends the base client with evaluation utilities.
        """
        super().__init__(
            base_url=base_url,
            environment=environment,
            api_key=api_key,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
        )

        self._tracer_provider = TracerProvider(
            resource=Resource(
                attributes={
                    "instrumentor": "humanloop.sdk",
                }
            ),
        )
        instrument_provider(provider=self._tracer_provider)
        self._tracer_provider.add_span_processor(
            HumanloopSpanProcessor(
                exporter=HumanloopSpanExporter(
                    client=self,
                )
            ),
        )
        tracer = self._tracer_provider.get_tracer("humanloop.sdk")
        set_tracer(tracer)

        eval_client = ExtendedEvalsClient(client_wrapper=self._client_wrapper)
        eval_client.client = self
        self.evaluations = eval_client
        self.prompts = ExtendedPromptsClient(client_wrapper=self._client_wrapper)
        self.flows = ExtendedFlowsClient(client_wrapper=self._client_wrapper)
        self.tools = ExtendedToolsClient(client_wrapper=self._client_wrapper)


class AsyncHumanloop(AsyncBaseHumanloop):
    """
    See docstring of AsyncBaseHumanloop.

    TODO: Add custom evaluation utilities for async case.
    """

    pass
