import os
from jinja2 import Template


def render(template_name, **kwargs):
    """
    :param template_name: имя шаблона
    :param kwargs: параметры
    :return:
    """
    file_path = os.path.join(template_name)
    # Открываем шаблон по имени
    with open(file_path, encoding='utf-8') as f:
        # Читаем
        template = Template(f.read())
    # рендерим шаблон с параметрами
    return template.render(**kwargs)
