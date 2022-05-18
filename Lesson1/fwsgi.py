from template_engine import render


# page controller

def index_view(request):
    print(request)
    return '200 OK', render('templates/index.html', car_brand='none')


def volga_view(request):
    print(request)
    return '200 OK', render('templates/index.html', car_brand='volga')


def yaz_view(request):
    print(request)
    return '200 OK', render('templates/index.html', car_brand='yaz')


def tagaz_view(request):
    print(request)
    return '200 OK', render('templates/index.html', car_brand='tagaz')


def not_found_404_view(request):
    print(request)
    return '404 OOops', [b'404 UNKNOWN car_brand!']


class Other:
    def __call__(self, request):
        return '200 OK', render('templates/index.html', car_brand='other car_brand')


routes = {
    '/': index_view,
    '/volga': volga_view,
    '/yaz': yaz_view,
    '/tagaz': tagaz_view,
    '/other': Other(),

}


# Front controllers
def opposite(request):
    request['opposite'] = 'opposite'


def similar_brand_front(request):
    request['similar_brand'] = 'similar_brand'


fronts = [opposite, similar_brand_front]


class Application:

    def __init__(self, urlpatterns: dict, front_controllers: list):
        """
        :param urlpatterns: словарь связок url: view
        :param front_controllers: список front controllers
        """
        self.urlpatterns = routes
        self.front_controllers = fronts

    def __call__(self, env, start_response):
        # текущий url
        path = env['PATH_INFO']

        if path in self.urlpatterns:
            # получаем view по url
            view = self.urlpatterns[path]
            request = {}
            # добавляем в запрос данные из front controllers
            for controller in self.front_controllers:
                controller(request)
            # вызываем view, получаем результат
            code, text = view(request)
            # возвращаем заголовки
            start_response(code, [('Content-Type', 'text/html')])
            # возвращаем тело ответа
            return [text.encode('utf-8')]
        else:
            # Если url нет в urlpatterns - то страница не найдена
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b"Not Found"]


application = Application(routes, fronts)
