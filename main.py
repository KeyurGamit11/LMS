import unittest

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append({"title": title, "borrowed": False})

    def display_books(self):
        if not self.books:
            print("The library has no books.")
            return

        available_books = [book["title"] for book in self.books if not book["borrowed"]]
        borrowed_books = [book["title"] for book in self.books if book["borrowed"]]

        print(f"The Library has {len(self.books)} books in total.")
        
        if available_books:
            print("Available books:")
            print("\n".join(f"- {book}" for book in available_books))
        else:
            print("No books are currently available.")

        if borrowed_books:
            print("Borrowed books:")
            print("\n".join(f"- {book}" for book in borrowed_books))
        else:
            print("No books are currently borrowed.")

    def return_book(self, title):
        book = next((book for book in self.books if book["title"] == title), None)
        if not book:
            print(f"'{title}' is not in the library.")
        elif not book["borrowed"]:
            print(f"'{title}' was not borrowed.")
        else:
            book["borrowed"] = False
            print(f"Thank you for returning '{title}'.")

    def borrow_book(self, title):
        book = next((book for book in self.books if book["title"] == title), None)
        if not book:
            print(f"Sorry, '{title}' is not available in the library.")
        elif book["borrowed"]:
            print(f"Sorry, '{title}' is already borrowed.")
        else:
            book["borrowed"] = True
            print(f"You have borrowed '{title}'.")


class TestLibrary(unittest.TestCase):
    
    def test_add_book(self):
        library = Library()
        library.add_book("Keyur")
        self.assertEqual(len(library.books), 1)
        self.assertEqual(library.books[0]['title'], "Keyur")
        self.assertFalse(library.books[0]['borrowed'])
    
    def test_borrow_book(self):
        library = Library()
        library.add_book("Discipline")
        library.borrow_book("Discipline")
        self.assertTrue(library.books[0]['borrowed'])

    def test_borrow_book_already_borrowed(self):
        library = Library()
        library.add_book("Stay Hard")
        library.borrow_book("Stay Hard")
        library.borrow_book("Stay Hard")
        self.assertTrue(library.books[0]['borrowed'])

    def test_borrow_book_not_in_library(self):
        library = Library()
        library.add_book("Keyur")
        library.borrow_book("Nonexistent Book")
        self.assertFalse(any(book['borrowed'] for book in library.books))

    def test_return_book(self):
        library = Library()
        library.add_book("To Kill a Mockingbird")
        library.borrow_book("To Kill a Mockingbird")
        library.return_book("To Kill a Mockingbird")
        self.assertFalse(library.books[0]['borrowed'])

    def test_return_book_not_borrowed(self):
        library = Library()
        library.add_book("To Kill a Mockingbird")
        library.return_book("To Kill a Mockingbird")
        self.assertFalse(library.books[0]['borrowed'])

    def test_return_book_not_in_library(self):
        library = Library()
        library.return_book("Nonexistent Book")
        self.assertFalse(any(book['borrowed'] for book in library.books))

    def test_display_books(self):
        library = Library()
        library.add_book("Harry Potter")
        library.add_book("Discipline")
        library.borrow_book("Discipline")
        library.add_book("Keyur")
        
        available_books = [book["title"] for book in library.books if not book["borrowed"]]
        borrowed_books = [book["title"] for book in library.books if book["borrowed"]]

        self.assertIn("Harry Potter", available_books)
        self.assertIn("Keyur", available_books)
        self.assertIn("Discipline", borrowed_books)
       
if __name__ == "__main__":
    unittest.main()
