from __future__ import annotations
from abc import ABC, abstractmethod


class Visitor(ABC):

    @abstractmethod
    def visitPizza(self, pizza):
        pass

    @abstractmethod
    def visitPaste(self, paste):
        pass

    @abstractmethod
    def visitSalata(self, salata):
        pass
