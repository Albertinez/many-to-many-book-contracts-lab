from lib.models.contract import Contract

class Author:
    all_authors = []

    def __init__(self, name: str):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        return [c for c in Contract.all_contracts if c.author == self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date: str, royalties: int):
        from lib.models.contract import Contract
        return Contract(author=self, book=book, date=date, royalties=royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())

    def __repr__(self):
        return f"<Author: {self.name}>"
