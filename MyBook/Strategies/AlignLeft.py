from Interfaces.AlignStrategyInterface import AlignStrategyInterface


class AlignLeft(AlignStrategyInterface):

    def render(self, paragraph):
        print(f"{'Paragraph: ' + paragraph: <100}")
