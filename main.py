from Lesson2.urls import Url
from Lesson2.view import View
from Lesson2.wsgi import Framework
from Lesson2.response import Response


class MyView(View):
    def get(self, request):
        return Response(body='GET SUCCESS')

    def post(self, request):
        return Response(status='201 Created', body='POST SUCCESS', headers={'MY_HEADERS': '222'})


urls = [
    Url('/page', MyView),

]

app = Framework(urls)
