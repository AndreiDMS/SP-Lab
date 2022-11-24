from ComandaInterface import ComandaInterface


class Comanda(ComandaInterface):

    def __init__(self, name):
        self.name = name
        self.subComenzi = []

    def addComanda(self, comanda):
        self.subComenzi.append(comanda)

    def accept(self, visitor):
        for element in self.subComenzi:
            element.accept(visitor)
