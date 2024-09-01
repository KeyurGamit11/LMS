class Library:
    def __init__(self):
        
        self.books =[]

    
    def add_books(self, book):
        self.books.append({"title": book, "borrowed": False})

    def show_info(self):
        if not self.books:
            print("The library has no books.")
            return
        
        available_books = [book["title"] for book in self.books if not book["borrowed"]]
        borrowed_books = [book["title"] for book in self.books if book["borrowed"]]

        print(f"The Library has {len(self.books)} books in total.")
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- {book}")
        else:
            print("No books are currently available.")

        if borrowed_books:
            print("Borrowed books:")
            for book in borrowed_books:
                print(f"- {book}")
        else:
            print("No books are currently borrowed.")

    def return_book(self, book_title):
        for book in self.books:
            if book["title"] == book_title:
                if book["borrowed"]:
                    book["borrowed"] = False
                    print(f"Thank you for returning '{book_title}'.")
                    return
                else:
                    print(f"'{book_title}' was not borrowed.")
                    return
        print(f"'{book_title}' is not in the library.")

    def borrow_book(self, book_title):
        for book in self.books:
            if book["title"] == book_title:
                if not book["borrowed"]:
                    book["borrowed"] = True
                    print(f"You have borrowed '{book_title}'.")
                    return
                else:
                    print(f"Sorry, '{book_title}' is already borrowed.")
                    return
        print(f"Sorry, '{book_title}' is not available in the library.")


