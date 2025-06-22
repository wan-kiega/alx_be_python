# library_management.py

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private availability status

    def check_out(self):
        """Marks the book as checked out."""
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self._is_checked_out = True

    def return_book(self):
        """Marks the book as available."""
        if not self._is_checked_out:
            print(f"'{self.title}' was not checked out.")
        else:
            self._is_checked_out = False

    def is_available(self) -> bool:
        """Returns True if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # Private list of Book instances

    def add_book(self, book: Book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title: str):
        """Checks out a book by its title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"Checked out '{title}'.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title: str):
        """Returns a book to the library."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"Returned '{title}'.")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """Lists all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are currently available.")
        else:
            print("Available books:")
            for book in available_books:
                print(f"{book.title} by {book.author}")

# main.py

from library_management import Book, Library


def main():
    # Create a library
    library = Library()

    # Add books to the library
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # List available books
    print("Available Books:")
    library.list_available_books()

    # Check out a book
    print("\nChecking out '1984':")
    library.check_out_book("1984")

    # Try to check it out again
    print("\nTrying to check out '1984' again:")
    library.check_out_book("1984")

    # List available books after checkout
    print("\nAvailable Books After Checkout:")
    library.list_available_books()

    # Return the book
    print("\nReturning '1984':")
    library.return_book("1984")

    # List available books again
    print("\nAvailable Books After Return:")
    library.list_available_books()


if __name__ == "__main__":
    main()