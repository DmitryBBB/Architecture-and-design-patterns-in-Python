from Lesson3.urls import Url
from view import HomePage

urlpatterns = [
    Url('^$', HomePage),
    # Url('^/math$', MathSum),
]
