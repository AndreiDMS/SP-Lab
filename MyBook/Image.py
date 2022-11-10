import time
import random

from Interfaces.ElementInterface import ElementInterface
from Interfaces.PictureInterface import PictureInterface
from Interfaces.Visitor import Visitor


class Image(ElementInterface, PictureInterface):
    """Image
    """

    def __init__(self, name, url="") -> None:
        super().__init__()
        self.name = name
        self._dim = random.randint(0, 1)
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

    def accept(self, visitor: Visitor):
        visitor.visitImage(self)
