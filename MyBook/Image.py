import time

from ElementInterface import ElementInterface


class Image(ElementInterface):
    """Image
    """

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        time.sleep(1)

    def print(self):
        print("Image with name:", self.name)
