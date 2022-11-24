from Vizitatori.Visitor import Visitor


class CalculatorPret(Visitor):

    def __init__(self):
        self._total = 0
        self._pretPizza = 0
        self._pretPaste = 0
        self._pretSalate = 0

    def visitPizza(self, pizza):
        self._pretPizza += pizza.getPret()
        self._total += pizza.getPret()

    def visitPaste(self, paste):
        self._pretPaste += paste.getPret()
        self._total += paste.getPret()

    def visitSalata(self, salata):
        self._pretSalate += salata.getPret()
        self._total += salata.getPret()

    def printPret(self):
        print("Pret comenzi")
        print("Pizza", self._pretPizza)
        print("Paste", self._pretPaste)
        print("Salate", self._pretSalate)
        print("Tota", self._total)
