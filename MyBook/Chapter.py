from SubChapter import SubChapter

class Chapter:
    """Chapter
    """

    def __init__(self, name) -> None:
        self.name = name
        self.subChapters = []

    def createSubChapter(self, subChapterName):
        subChapter = SubChapter(subChapterName)
        self.subChapters.append(subChapter)
        return len(self.subChapters) - 1

    def getSubChapter(self, subChapterIndex):
        return self.subChapters[subChapterIndex]

    def print(self):
        print("Chapter:", self.name)
        for subChapter in self.subChapters:
            subChapter.print()
