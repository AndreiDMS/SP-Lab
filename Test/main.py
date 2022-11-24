from Restaurant import Restaurant
from Comanda import Comanda
from Mancaruri.Pizza import Pizza
from Mancaruri.Paste import Paste
from Mancaruri.Salata import Salata
from Vizitatori.CalculatorPret import CalculatorPret


def main():
    print("Test SP")

    R1 = Restaurant("R1")
    R2 = Restaurant("R2")

    R1.addToMenu(Pizza("Pizza 1", 30))
    R1.addToMenu(Salata("Salata 1", 45))
    R1.addToMenu(Paste("Paste 1", 25))

    R2.addToMenu(Pizza("Pizza 2", 25))
    R2.addToMenu(Salata("Salata 2", 40))
    R2.addToMenu(Paste("Paste 2", 30))

    comanda = Comanda("Comanda 1")
    subcomanda1 = Comanda("Comanda R1")
    subcomanda2 = Comanda("Comanda R2")
    comanda.addComanda(subcomanda1)
    comanda.addComanda(subcomanda2)

    subcomanda1.addComanda(R1.getMenuItem("Pizza 1"))
    subcomanda1.addComanda(R1.getMenuItem("Pizza 1"))
    subcomanda1.addComanda(R1.getMenuItem("Paste 1"))
    subcomanda2.addComanda(R2.getMenuItem("Pizza 2"))
    subcomanda2.addComanda(R2.getMenuItem("Salata 2"))

    cPret = CalculatorPret()
    comanda.accept(cPret)
    cPret.printPret()


if __name__ == "__main__":
    main()
