from __future__ import annotations
from abc import ABC, abstractmethod


class PictureInterface(ABC):

    @abstractmethod
    def url(self):
        pass

    @abstractmethod
    def dim(self):
        pass

    @abstractmethod
    def content(self):
        pass
