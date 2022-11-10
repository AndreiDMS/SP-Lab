from typing import List
from Interfaces.ElementInterface import ElementInterface


class CompoundElement(ElementInterface):
    """CompoundElement
    """

    def __init__(self) -> None:
        super(CompoundElement, self).__init__()
        self.elements: List[ElementInterface] = []

    def add(self, element: ElementInterface):
        if element.parent:
            raise Exception("Element is already added to another section")
        self.elements.append(element)
        element.parent = self

    def remove(self, element: ElementInterface):
        self.elements.remove(element)
        element.parent = None

    def print(self):
        for element in self.elements:
            element.print()

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)
