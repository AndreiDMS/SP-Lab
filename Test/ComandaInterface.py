from __future__ import annotations
from abc import ABC, abstractmethod


class ComandaInterface(ABC):
    def __init__(self):
        self._parent = None

    @property
    def parent(self) -> ComandaInterface:
        return self._parent

    @parent.setter
    def parent(self, parent: ComandaInterface):
        self._parent = parent

    @abstractmethod
    def addComanda(self, comanda: ComandaInterface):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass
