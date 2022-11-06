from __future__ import annotations
from abc import ABC, abstractmethod


class AlignStrategyInterface(ABC):

    def __init__(self):
        self.lineWidth = 100

    @abstractmethod
    def render(self, paragrah):
        pass
