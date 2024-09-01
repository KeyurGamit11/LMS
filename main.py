class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append({"title": title, "borrowed": False})

    def show_info(self):
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
