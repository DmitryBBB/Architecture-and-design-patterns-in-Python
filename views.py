from Lesson3.templator import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', data=request.get('date', None))


class About:
    def __call__(self, request):
        return '200 OK', 'about'

class Contacts:
    def __call__(self, request):
        return '200 OK', render('contacts.html', data=request.get('date', None))
