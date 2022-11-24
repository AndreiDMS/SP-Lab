from Mancaruri.FelMancareInterface import FelMancareInterface
from ComandaInterface import ComandaInterface


class Pizza(FelMancareInterface, ComandaInterface):

    def __init__(self, nume, pret):
        super().__init__(nume, pret)

    def addComanda(self, comanda):
        pass

    def accept(self, visitor):
        visitor.visitPizza(self)
