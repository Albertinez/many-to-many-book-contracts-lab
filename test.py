from lib.models.author import Author
from lib.models.book import Book
from lib.models.contract import Contract

# Create authors
a1 = Author("Author One")
a2 = Author("Author Two")

# Create books
b1 = Book("Book One")
b2 = Book("Book Two")

# Sign contracts
a1.sign_contract(b1, "2026-02-19", 500)
a2.sign_contract(b1, "2026-02-19", 300)
a1.sign_contract(b2, "2026-02-20", 200)

# Test outputs
print("Author 1 books:", a1.books())            # [Book One, Book Two]
print("Book 1 authors:", b1.authors())          # [Author One, Author Two]
print("Author 1 total royalties:", a1.total_royalties())  # 700

# Test contracts_by_date
print("Contracts on 2026-02-19:", Contract.contracts_by_date("2026-02-19"))
