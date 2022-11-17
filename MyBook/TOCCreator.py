from Interfaces.Visitor import Visitor
from TableOfContents import TableOfContents


class TOCCreator(Visitor):

    def __init__(self):
        self._toc = TableOfContents()
        self._pageCounter = 0

    def getTOC(self):
        return self._toc

    def visitBook(self, book):
        self._pageCounter += 1

    def visitSection(self, section):
        self._toc.add(f"{section.name:.<15}{self._pageCounter+1:.>20}")

    def visitParagraph(self, paragraph):
        self._pageCounter += 1

    def visitImageProxy(self, imageProxy):
        self._pageCounter += 1

    def visitImage(self, image):
        self._pageCounter += 1

    def visitTable(self, table):
        self._pageCounter += 1
