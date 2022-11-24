from Mancaruri.FelMancareInterface import FelMancareInterface


class Salata(FelMancareInterface):

    def __init__(self, nume, pret):
        super().__init__(nume, pret)

    def addComanda(self, comanda):
        pass

    def accept(self, visitor):
        visitor.visitSalata(self)
