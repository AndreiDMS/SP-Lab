from Book import Book
from Section import Section
from Paragraph import Paragraph
from ImageProxy import ImageProxy
from Image import Image
from Table import Table
from BookStatistics import BookStatistics
from TOCCreator import TOCCreator


def main():
    book = Book("Book with TOC")
    book.add(Paragraph("Introducere"))
    cap1 = Section("Capitolul 1")
    p1 = Paragraph("Paragraph 1")
    cap1.add(p1)
    p2 = Paragraph("Paragraph 2")
    cap1.add(p2)
    p3 = Paragraph("Paragraph 3")
    cap1.add(p3)
    p4 = Paragraph("Paragraph 4")
    cap1.add(p4)
    cap1.add(ImageProxy("ImageOne"))
    cap1.add(Image("ImageTwo"))
    cap1.add(Paragraph("Some text"))
    cap1.add(Table("Table 1"))
    book.add(cap1)
    cap2 = Section("Capitolul 2")
    book.add(cap2)

    stats = BookStatistics()
    tocCreator = TOCCreator()

    book.accept(stats)
    book.accept(tocCreator)

    book.add(tocCreator.getTOC())
    book.print()

    stats.printStatistics()


if __name__ == "__main__":
    main()
