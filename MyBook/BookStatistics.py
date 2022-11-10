from Interfaces.Visitor import Visitor


class BookStatistics(Visitor):

    def __init__(self):
        self._book = 0
        self._sections = 0
        self._paragraphs = 0
        self._tables = 0
        self._images = 0

    def visitBook(self, book):
        self._book += 1

    def visitTableOfContents(self, toc):
        pass

    def visitSection(self, section):
        self._sections += 1

    def visitParagraph(self, paragraph):
        self._paragraphs += 1

    def visitImageProxy(self, imageProxy):
        self._images += 1

    def visitImage(self, image):
        self._images += 1

    def visitTable(self, table):
        self._tables += 1

    def printStatistics(self):
        print(f"Number of sections is {self._sections}")
        print(f"Number of images is {self._images}")
        print(f"Number of paragraphs is {self._paragraphs}")
        print(f"Number of tables is {self._tables}")
