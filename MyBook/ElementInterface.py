from __future__ import annotations
from abc import ABC, abstractmethod


class ElementInterface(ABC):

    def add(self, element: ElementInterface):
        """Leaf elements don't have to implement this method
        """

    def remove(self, element: ElementInterface):
        """Leaf elements don't have to implement this method
        """

    def get(self, index: int):
        """Leaf elements don't have to implement this method
        """

    @abstractmethod
    def print(self):
        pass
