from dataclasses import dataclass

from Lesson2.view import View


@dataclass
class Url:
    path: str
    view: View()
