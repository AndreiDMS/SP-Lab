from CompoundElement import CompoundElement
from Interfaces.Visitor import Visitor


class Section(CompoundElement):

    def __init__(self, name):
        super(Section, self).__init__()
        self.name = name

    def print(self):
        print(self.name)
        super(Section, self).print()

    def accept(self, visitor: Visitor):
        visitor.visitSection(self)
        super(Section, self).accept(visitor)
