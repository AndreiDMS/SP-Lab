from Interfaces import AlignStrategyInterface


class AlignCenter(AlignStrategyInterface):

    def render(self, paragraph):
        print(f"{'Paragraph: ' + paragraph: ^100}")
