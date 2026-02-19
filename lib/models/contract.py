class Contract:
    all_contracts = []

    def __init__(self, author, book, date: str, royalties: int):
        # Local import to avoid circular import
        from lib.models.author import Author
        from lib.models.book import Book

        # Validate types
        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        if not isinstance(book, Book):
            raise TypeError("book must be a Book instance")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date: str):
        return [c for c in cls.all_contracts if c.date == date]

    def __repr__(self):
        return f"<Contract: {self.author.name} - {self.book.title} - {self.date} - {self.royalties}>"
