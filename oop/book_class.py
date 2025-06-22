# book_class.py

class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Constructor: Initializes a Book instance with title, author, and year.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor: Prints a message when the Book object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        String representation of the Book instance.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Official string representation that can recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
if __name__ == "__main__":
    # Creating an instance of Book
    my_book = Book("The Hobbit", "J.R.R. Tolkien", 1937)

    # Displaying __str__ output
    print("String representation:")
    print(my_book)

    # Displaying __repr__ output
    print("\nOfficial representation:")
    print(repr(my_book))

# Deleting the object to trigger __del__
    del my_book