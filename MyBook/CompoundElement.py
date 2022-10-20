from typing import List
from ElementInterface import ElementInterface


class CompoundElement(ElementInterface):
    """CompoundElement
    """

    def __init__(self) -> None:
        self.elements: List[ElementInterface] = []

    def add(self, element: ElementInterface):
        self.elements.append(element)

    def remove(self, element: ElementInterface):
        self.elements.remove(element)

    def print(self):
        for element in self.elements:
            element.print()
