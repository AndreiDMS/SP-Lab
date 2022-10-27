
from ElementInterface import ElementInterface
from Image import Image


class ImageProxy(ElementInterface):
    """Image
    """

    def __init__(self, name, imagePath=None) -> None:
        super().__init__()
        self.name = name
        self.imagePath = imagePath
        self.dim = None
        self.realImage = None

    def loadImage(self):
        if not self.realImage:
            self.realImage = Image(self.name)
        return self.realImage

    def print(self):
        self.loadImage().print()
