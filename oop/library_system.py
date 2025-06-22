# library_system.py

class Book:
    """Base class representing a generic book."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class EBook(Book):
    """Derived class representing an electronic book."""
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    """Derived class representing a printed book."""
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    """Class representing a library composed of multiple books."""
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        """Add a book to the library collection."""
        self.books.append(book)

    def list_books(self):
        """Print out details of all books in the library."""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")

# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    library = Library()

    # Create instances of each type of Book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 512)
    paper_novel = PrintBook("The catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    library.add_book(classic_book)
    library.add_book(digital_novel)
    library.add_book(paper_novel)

    # List all books in the library
    print("Books in the library:")
    library.list_books()

if __name__ == "__main__":
    main()