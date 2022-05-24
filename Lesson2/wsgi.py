from Lesson2.request import Request
from Lesson2.view import View


class Framework:
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = Request(environ)
        view = self._get_view(request)
        response = self._get_response(request, view)
        start_response(response.status, list(response.headers.items()))
        # возвращаем тело ответа в виде списка из bite
        return [response.body.encode()]

    def _get_view(self, request: Request):
        path = request.path

        for url in self.urls:
            if url.path == path:
                return url.view
            return None

    def _get_response(self, request: Request, view: View):
        if hasattr(view, request.method):
            return getattr(view, request.method)(view, request)
        return 'Method not '

    # def _prepare_url(self, url: Url):
    #     if url[-1] == '/':
    #         return url[:-1]
    #     return url
