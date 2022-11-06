from __future__ import annotations
from abc import ABC, abstractmethod


class ImageLoaderInterface(ABC):

    @abstractmethod
    def load(self):
        pass
