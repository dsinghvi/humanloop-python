# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.paginated_session_response import PaginatedSessionResponse
from ..types.session_response import SessionResponse


class SessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SessionResponse:
        """
        Retrieve the Session with the given ID.

        Parameters
        ----------
        id : str
            Unique identifier for Session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionResponse
            Successful Response

        Examples
        --------
        from humanloop.client import Humanloop

        client = Humanloop(
            api_key="YOUR_API_KEY",
        )
        client.sessions.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sessions/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(SessionResponse, construct_type(type_=SessionResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete the Session with the given ID.

        Parameters
        ----------
        id : str
            Unique identifier for Session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from humanloop.client import Humanloop

        client = Humanloop(
            api_key="YOUR_API_KEY",
        )
        client.sessions.delete(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sessions/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(
        self,
        *,
        file_id: typing.Optional[str] = None,
        version_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[SessionResponse]:
        """
        Get a list of Sessions.

        Parameters
        ----------
        file_id : typing.Optional[str]
            Unique identifier for File to return Sessions for. Sessions that contain any Logs associated to this File will be returned.

        version_id : typing.Optional[str]
            Unique identifier for Version to return Sessions for. Sessions that contain any Logs associated to this Version will be returned.

        page : typing.Optional[int]
            Page number for pagination.

        size : typing.Optional[int]
            Page size for pagination. Number of Sessions to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[SessionResponse]
            Successful Response

        Examples
        --------
        from humanloop.client import Humanloop

        client = Humanloop(
            api_key="YOUR_API_KEY",
        )
        client.sessions.list()
        """
        page = page or 1
        _response = self._client_wrapper.httpx_client.request(
            "sessions",
            method="GET",
            params={"file_id": file_id, "version_id": version_id, "page": page, "size": size},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(PaginatedSessionResponse, construct_type(type_=PaginatedSessionResponse, object_=_response.json()))  # type: ignore
                _has_next = True
                _get_next = lambda: self.list(
                    file_id=file_id, version_id=version_id, page=page + 1, size=size, request_options=request_options
                )
                _items = _parsed_response.records
                return SyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SessionResponse:
        """
        Retrieve the Session with the given ID.

        Parameters
        ----------
        id : str
            Unique identifier for Session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionResponse
            Successful Response

        Examples
        --------
        from humanloop.client import AsyncHumanloop

        client = AsyncHumanloop(
            api_key="YOUR_API_KEY",
        )
        await client.sessions.get(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sessions/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(SessionResponse, construct_type(type_=SessionResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete the Session with the given ID.

        Parameters
        ----------
        id : str
            Unique identifier for Session.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from humanloop.client import AsyncHumanloop

        client = AsyncHumanloop(
            api_key="YOUR_API_KEY",
        )
        await client.sessions.delete(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sessions/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self,
        *,
        file_id: typing.Optional[str] = None,
        version_id: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[SessionResponse]:
        """
        Get a list of Sessions.

        Parameters
        ----------
        file_id : typing.Optional[str]
            Unique identifier for File to return Sessions for. Sessions that contain any Logs associated to this File will be returned.

        version_id : typing.Optional[str]
            Unique identifier for Version to return Sessions for. Sessions that contain any Logs associated to this Version will be returned.

        page : typing.Optional[int]
            Page number for pagination.

        size : typing.Optional[int]
            Page size for pagination. Number of Sessions to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[SessionResponse]
            Successful Response

        Examples
        --------
        from humanloop.client import AsyncHumanloop

        client = AsyncHumanloop(
            api_key="YOUR_API_KEY",
        )
        await client.sessions.list()
        """
        page = page or 1
        _response = await self._client_wrapper.httpx_client.request(
            "sessions",
            method="GET",
            params={"file_id": file_id, "version_id": version_id, "page": page, "size": size},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(PaginatedSessionResponse, construct_type(type_=PaginatedSessionResponse, object_=_response.json()))  # type: ignore
                _has_next = True
                _get_next = lambda: self.list(
                    file_id=file_id, version_id=version_id, page=page + 1, size=size, request_options=request_options
                )
                _items = _parsed_response.records
                return AsyncPager(has_next=_has_next, items=_items, get_next=_get_next)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    typing.cast(HttpValidationError, construct_type(type_=HttpValidationError, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
