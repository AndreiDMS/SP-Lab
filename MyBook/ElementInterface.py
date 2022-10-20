from __future__ import annotations
from abc import ABC, abstractmethod


class ElementInterface(ABC):

    def __init__(self):
        self._parent = None

    @property
    def parent(self) -> ElementInterface:
        return self._parent

    @parent.setter
    def parent(self, parent: ElementInterface):
        self._parent = parent

    def add(self, element: ElementInterface):
        """Leaf elements don't have to implement this method
        """

    def remove(self, element: ElementInterface):
        """Leaf elements don't have to implement this method
        """

    def get(self, index: int) -> ElementInterface:
        """Leaf elements don't have to implement this method
        """

    @abstractmethod
    def print(self):
        pass
