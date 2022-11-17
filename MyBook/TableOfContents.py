from Interfaces.ElementInterface import ElementInterface


class TableOfContents(ElementInterface):
    """TableOfContents
    """

    def __init__(self) -> None:
        super().__init__()
        self.__content = []

    def add(self, text):
        self.__content.append(text)

    def print(self):
        print("\nTable of Contents")
        for element in self.__content:
            print(element)

    def accept(self, visitor):
        pass
