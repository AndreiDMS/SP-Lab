from Paragraph import Paragraph
from Section import Section
from ImageProxy import ImageProxy
from Image import Image
from Table import Table
from BookStatistics import BookStatistics


def main():
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
    stats = BookStatistics()
    cap1.accept(stats)
    stats.printStatistics()


if __name__ == "__main__":
    main()
