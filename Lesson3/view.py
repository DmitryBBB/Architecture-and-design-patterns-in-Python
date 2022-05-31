from Lesson3.request import Request
from Lesson3.response import Response


class View:
    def get(self, request: Request, *args, **kwargs) -> Response:
        pass

    def post(self, request: Request, *args, **kwargs) -> Response:
        pass