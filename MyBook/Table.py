
from Interfaces.ElementInterface import ElementInterface
from Interfaces.Visitor import Visitor


class Table(ElementInterface):
    """Table
    """

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def print(self):
        print("Table with title:", self.name)

    def accept(self, visitor: Visitor):
        visitor.visitTable(self)
