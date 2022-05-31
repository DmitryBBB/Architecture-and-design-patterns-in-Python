import os.path

from Lesson3.main import Framework
from urls import urlpatterns

settings = {
    'BASE_DIR': os.path.dirname(os.path.abspath(__file__)),
    'TEMPLATE_DIR_NAME': 'templates'
}

app = Framework(
    urls=urlpatterns,
    settings=settings
)


