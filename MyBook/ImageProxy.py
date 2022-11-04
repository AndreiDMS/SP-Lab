
from ElementInterface import ElementInterface
from PictureInterface import PictureInterface
from Image import Image


class ImageProxy(ElementInterface, PictureInterface):
    """Image
    """

    def __init__(self, name, imagePath=None) -> None:
        super().__init__()
        self.name = name
        self.imagePath = imagePath
        self.realImage = None

    def loadImage(self):
        if not self.realImage:
            self.realImage = Image(self.name, self.imagePath)
        return self.realImage

    def print(self):
        self.loadImage().print()

    def content(self):
        return self.loadImage().content()

    def dim(self):
        return self.loadImage().dim()

    def url(self):
        return self.loadImage().url()
