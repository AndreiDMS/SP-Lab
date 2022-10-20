
from ElementInterface import ElementInterface


class Image(ElementInterface):
    """Image
    """

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def print(self):
        print("Image with name:", self.name)
