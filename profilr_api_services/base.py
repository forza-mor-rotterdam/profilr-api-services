from __future__ import annotations
from urllib.parse import urlencode

import requests
from django.core.cache import cache
from requests import Response, Request

from .exceptions import (
    ApiServiceForbiddenException,
    ApiServiceNotFoundException,
)
from typing import Any, cast


class BaseAPIService:
    _headers: dict = {}
    def __init__(self, *args, **kwargs):
        assert not args
        assert not kwargs

    def get_headers(self):
        if type(self._headers) is not dict:
            raise NotImplementedError
        return self._headers


class APIService(BaseAPIService):
    _api_base_url: str | None = None
    _json_enabled: bool = False
    _timeout: tuple[int, ...] = (5, 10)
    _cache_timeout: int = 60 * 5

    GET: str = "get"
    POST: str = "post"

    def __init__(self, api_base_url: str, *args: list[Any] | tuple[Any], **kwargs: dict):
        self._api_base_url = api_base_url.strip().rstrip("/")
        super().__init__(*args, **kwargs)

    def add_headers(self, headers: dict) -> dict:
        new_headers: dict = cast(dict, self._headers.update(headers))
        return new_headers

    def remove_headers(self, header_key: str) -> dict:
        self._headers.pop(header_key)
        return self._headers

    @classmethod
    def get_user_token_from_request(cls, request) -> str | None:
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        auth_parts = auth_header.split(" ") if auth_header else []
        if len(auth_parts) == 2 and auth_parts[0] == "Bearer":
            return auth_parts[1]
        return

    def process_response(self, response: Response) -> Response | Any:
        return response

    def do_request(
        self,
        path: str,
        user_token: str | None = None,
        method: str = GET,
        data: dict = {},
        no_cache: bool=False,
        cache_timeout: int=_cache_timeout,
        raw_response: bool=False,
    ) -> Response | list | dict:
        url = f"{self._api_base_url}/{path}"
        cache_key = f"{url}?{urlencode(data)}"
        response = cache.get(cache_key)
        action: Request = getattr(requests, method, APIService.GET)
        if not response or no_cache:
            headers = {}
            headers.update(self._headers)
            if user_token is not None:
                headers.update({"Authorization": f"Bearer {user_token}"})
            action_params: dict = {
                "url": url,
                "headers": headers,
                "json" if self._json_enabled else "data": data,
                "timeout": self._timeout,
            }
            response: Response = action(**action_params)

            if int(response.status_code) >= 200 and int(response.status_code) < 300:
                cache.set(cache_key, response, cache_timeout)
            elif response.status_code == 401:
                raise ApiServiceForbiddenException(f"url={url}")
            elif response.status_code == 404:
                raise ApiServiceNotFoundException(f"url={url}")
        else:
            print(f"fetch from cache: {cache_key}")
        return response if raw_response else self.process_response(response)
