from Chapter import Chapter
class Book:
    """ Book
    """
    def __init__(self, name):
        self.name = name
        self.author = None
        self.chapters = []

    def addAuthor(self, author):
        self.author = author

    def createChapter(self, chapterName):
        chapter = Chapter(chapterName)
        self.chapters.append(chapter)
        return len(self.chapters) - 1

    def getChapter(self, chapterIndex):
        return self.chapters[chapterIndex]

    def print(self):
        print("Book:", self.name)
        if self.author:
            self.author.print()
        for chapter in self.chapters:
            chapter.print()
