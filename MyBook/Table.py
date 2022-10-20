
from ElementInterface import ElementInterface


class Table(ElementInterface):
    """Table
    """

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def print(self):
        print("Table with title:", self.name)
