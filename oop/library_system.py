# library_system.py

class Book:
    """Base class representing a generic book."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """Class representing a library composed of multiple books."""
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """Add a book to the library collection."""
        self.books.append(book)

    def list_books(self):
        """Print out details of all books in the library using their __str__ method."""
        for book in self.books:
            print(book)

# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    library = Library()

    # Create instances of each type of Book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 512)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    library.add_book(classic_book)
    library.add_book(digital_novel)
    library.add_book(paper_novel)

    # List all books in the library
    print("Books in the library:")
    library.list_books()

if __name__ == "__main__":
    main()