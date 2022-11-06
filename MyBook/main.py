from Paragraph import Paragraph
from Section import Section
from AlignCenter import AlignCenter
from AlignLeft import AlignLeft
from AlignRight import AlignRight


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
    print("Printing without Alignment")
    print()
    cap1.print()

    p1.setAlignStrategy(AlignCenter())
    p2.setAlignStrategy(AlignRight())
    p3.setAlignStrategy(AlignLeft())
    print()
    print("Printing with Alignment")
    print()
    cap1.print()


if __name__ == "__main__":
    main()
