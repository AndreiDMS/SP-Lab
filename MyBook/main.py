from Book import Book

def main():
    discountTitanic = Book("Disco Titanic")

    discountTitanic.createNewParagraph("Paragraph 1")
    discountTitanic.createNewParagraph("Paragraph 2")
    discountTitanic.createNewParagraph("Paragraph 3")
    discountTitanic.createNewImage("Image 1")
    discountTitanic.createNewParagraph("Paragraph 4")
    discountTitanic.createNewTable("Table 1")
    discountTitanic.createNewParagraph("Paragraph 5")

    discountTitanic.print()

if __name__ == "__main__":
    main()
