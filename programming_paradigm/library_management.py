class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        print(f"Book '{title}' is not available.")
        return False

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                return True
        print(f"Book '{title}' does not exist in the library.")
        return False

    def list_available_books(self):
        """Print all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")