import time
import random

from Interfaces import ElementInterface
from Interfaces import PictureInterface


class Image(ElementInterface, PictureInterface):
    """Image
    """

    def __init__(self, name, url="") -> None:
        super().__init__()
        self.name = name
        self._dim = random.randint(0, 5)
        time.sleep(self._dim)
        self._content = name
        self._url = url

    def print(self):
        print("Image with name:", self.name)

    def content(self):
        return self._content

    def dim(self):
        return self._dim

    def url(self):
        return self._url
