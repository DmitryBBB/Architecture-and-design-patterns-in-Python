from view import View
from wsgi import Framework
from urls import Url


class MyView(View):
    def get(self, request):
        print('GET')

    def post(self, request):
        print('POST')


urls = [
    Url('/Lesson2', MyView)

]

app = Framework(urls)