from __future__ import annotations
from abc import ABC, abstractmethod


class FelMancareInterface(ABC):

    def __init__(self, nume, pret):
        self.nume = nume
        self.pret = pret

    def getPret(self):
        return self.pret

    def getNume(self):
        return self.nume
