
from Interfaces.ElementInterface import ElementInterface
from Interfaces.PictureInterface import PictureInterface
from Interfaces.Visitor import Visitor
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

    def accept(self, visitor: Visitor):
        visitor.visitImageProxy(self)
