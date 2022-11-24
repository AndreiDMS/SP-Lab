
class Restaurant:

    def __init__(self, name):
        self.name = name
        self.meniu = {}

    def addToMenu(self, felMancare):
        self.meniu[felMancare.getNume()] = felMancare

    def getMenuItem(self, nume):
        return self.meniu[nume]
