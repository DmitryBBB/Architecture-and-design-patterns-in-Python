from urls import Url
from view import View
from request import Request


class Framework:
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        view = self._get_view(request)
        print(self._get_response(request, view))
        start_response('200 OK', [('Content-Type', 'text/html')])
        # возвращаем тело ответа в виде списка из bite
        return [b'Hello world from a simple WSGI application!']

    def _get_view(self, request: Request):
        path = request.path
        for url in self.urls:
            if url.path == path:
                return url.view
            else:
                return [b'404 Not found']

    def _get_response(self, request: Request, view: View):
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        return 'Метод не поддерживается'

    # def _prepare_url(self, url: Url):
    #     if url[-1] == '/':
    #         return url[:-1]
    #     return url
