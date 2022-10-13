
from ElementInterface import ElementInterface


class Paragraph(ElementInterface):
    """Paragraph
    """

    def __init__(self, name) -> None:
        self.name = name

    def print(self):
        print("Paragraph:", self.name)
