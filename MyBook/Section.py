from CompoundElement import CompoundElement


class Section(CompoundElement):

    def __init__(self, name):
        super(Section, self).__init__()
        self.name = name

    def print(self):
        print(self.name)
        super(Section, self).print()
