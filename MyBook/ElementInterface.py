
from abc import ABC, abstractmethod


class ElementInterface(ABC):

    @abstractmethod
    def print(self):
        pass
