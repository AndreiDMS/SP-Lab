import time

from Author import Author
from Book import Book
from ImageProxy import ImageProxy
from Paragraph import Paragraph
from Section import Section


def main():
    # noapteBuna = Book("Noapte buna, copii!")
    # rpGheo = Author("Radu Pavel Gheo")
    # noapteBuna.addAuthor(rpGheo)
    # cap1 = Section("Capitolul 1")
    # cap11 = Section("Capitolul 1.1")
    # cap111 = Section("Capitolul 1.1.1")
    # cap1111 = Section("Subchapter 1.1.1.1")
    # noapteBuna.addContent(Paragraph("Multumesc celor care ..."))
    # noapteBuna.addContent(cap1)
    # cap1.add(Paragraph("Moto capitol"))
    # cap1.add(cap11)
    # cap11.add(Paragraph("Text from subchapter 1.1"))
    # cap11.add(cap111)
    # cap111.add(Paragraph("Text from subchapter 1.1.1"))
    # cap111.add(cap1111)
    # cap1111.add(Image("Image subchapter 1.1.1.1"))
    # noapteBuna.print()

    startTime = time.time() * 1000

    img1 = ImageProxy("Pamela Anderson")
    img2 = ImageProxy("Kim Kardashian")
    img3 = ImageProxy("Kirby Griffin")
    playboyS1 = Section("Front Cover")
    playboyS1.add(img1)
    playboyS2 = Section("Summer Girls")
    playboyS2.add(img2)
    playboyS2.add(img3)
    playboy = Book("Playboy")

    playboy.addContent(playboyS1)
    playboy.addContent(playboyS2)
    endTime = time.time() * 1000

    print("Creation of the content took " + str(endTime -
                                                startTime) + " milliseconds")
    startTime = time.time() * 1000
    playboyS1.print()
    endTime = time.time() * 1000
    print("Printing of the section 1 took " + str(endTime -
                                                  startTime) + " milliseconds")
    startTime = time.time() * 1000
    playboyS1.print()
    endTime = time.time() * 1000
    print("Printing again the section 1 took " + str(endTime -
                                                     startTime) + " milliseconds")


if __name__ == "__main__":
    main()
