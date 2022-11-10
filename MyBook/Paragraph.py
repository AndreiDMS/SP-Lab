from Interfaces.ElementInterface import ElementInterface
from Interfaces.Visitor import Visitor


class Paragraph(ElementInterface):
    """Paragraph
    """

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.textAlignment = None

    def print(self):
        if self.textAlignment:
            self.textAlignment.render(self.name)
        else:
            print("Paragraph:", self.name)

    def setAlignStrategy(self, alignmentStrategy):
        self.textAlignment = alignmentStrategy

    def accept(self, visitor: Visitor):
        visitor.visitParagraph(self)
