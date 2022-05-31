import re
from typing import List, Type

from Lesson3.request import Request
from Lesson3.response import Response
from Lesson3.view import View
from Lesson3.exeption import NotAllowed, NotFound
from Lesson3.urls import Url


class Framework:
    def __init__(self, urls: List[Url], settings: dict):
        self.urls = urls
        self.settings =settings

    def __call__(self, environ, start_response):
        view = self._get_view(environ)
        request = self._get_request(environ)
        response = self._get_response(environ, view, request)
        start_response(str(response.status_code), response.headers.items())
        return iter([response.body])

    """Method '/'?"""

    def _prepare_url(self, url: str):
        if url[-1] == '/':
            return url[:-1]
        return url

    def _find_view(self, raw_url: str) -> Type[View]:
        """Найти вью или отдать ошибку 404"""
        url = self._prepare_url(raw_url)
        for path in self.urls:
            m = re.match(path.url, url)
            if m is not None:
                return path.view
        raise NotFound

    def _get_view(self, environ: dict) -> View:
        raw_url = environ['PATH_INFO']
        view = self._find_view(raw_url)()
        return view

    def _get_request(self, environ: dict):
        return Request(environ, self.settings)

    def _get_response(self, environ: dict, view: View, request: Request) -> Response:
        method = environ['REQUEST_METHOD'].lower()
        if not hasattr(view, method):
            raise NotAllowed
        return getattr(view, method)(request)
