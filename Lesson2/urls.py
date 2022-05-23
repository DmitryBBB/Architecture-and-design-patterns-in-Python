from dataclasses import dataclass

from view import View


@dataclass
class Url:
    url: str
    view: View()
