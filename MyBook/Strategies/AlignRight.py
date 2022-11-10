from Interfaces import AlignStrategyInterface


class AlignRight(AlignStrategyInterface):

    def render(self, paragraph):
        print(f"{'Paragraph: ' + paragraph: >100}")
