class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        return f"Title: {self.title}, author: {self.author}, year: {self.year}"


if __name__ == "__main__":
    book = Book("Harry Potter", "J.K. Rowling", 2001)
    print(book.info())
