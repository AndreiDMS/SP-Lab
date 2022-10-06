
class Book:
    def __init__(self, name):
        self.name = name
        self.content = []

    def createNewParagraph(self, paragraphName):
        self.content.append(paragraphName)

    def createNewImage(self, imageName):
        self.content.append(imageName)

    def createNewTable(self, tableName):
        self.content.append(tableName)

    def print(self):
        print(self.name)
        for element in self.content:
            print(element)
