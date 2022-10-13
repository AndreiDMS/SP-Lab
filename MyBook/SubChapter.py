
from Image import Image
from Table import Table
from Paragraph import Paragraph


class SubChapter():
    """SubChapter
    """

    def __init__(self, name) -> None:
        self.name = name
        self.content = []

    def createNewParagraph(self, paragraphName):
        paragraph = Paragraph(paragraphName)
        self.content.append(paragraph)

    def createNewImage(self, imageName):
        image = Image(imageName)
        self.content.append(image)

    def createNewTable(self, tableName):
        table = Table(tableName)
        self.content.append(table)

    def print(self):
        print("Subchapter:", self.name)
        for element in self.content:
            element.print()
