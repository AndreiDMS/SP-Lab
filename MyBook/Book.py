from CompoundElement import CompoundElement


class Book(CompoundElement):
    """ Book
    """

    def __init__(self, name):
        super(Book, self).__init__()
        self.name = name
        self.author = None

    def addContent(self, content):
        self.add(content)

    def addAuthor(self, author):
        self.author = author

    def print(self):
        print("Book:", self.name)

        print("\nAuthors:")
        if self.author:
            self.author.print()

        print("\n")
        super(Book, self).print()
