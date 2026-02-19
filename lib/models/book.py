from lib.models.contract import Contract

class Book:
    all_books = []

    def __init__(self, title: str):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        return [c for c in Contract.all_contracts if c.book == self]

    def authors(self):
        return [c.author for c in self.contracts()]

    def __repr__(self):
        return f"<Book: {self.title}>"
