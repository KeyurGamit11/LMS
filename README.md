Library Management System:
Overview
This is a simple Python-based library management system. It allows users to add books to the library, borrow books, return books, and display the status of all books in the library. The system is designed with an easy-to-understand structure and includes a set of unit tests to verify its functionality.

Features
Add Book: Add new books to the library.
Borrow Book: Borrow a book from the library if it's available.
Return Book: Return a borrowed book to the library.
Display Books: Show the list of available and borrowed books in the library.
Class Structure
Library
Methods:
add_book(title): Adds a book to the library with the given title.
borrow_book(title): Allows a user to borrow a book if it is available.
return_book(title): Allows a user to return a borrowed book.
display_books(): Displays the list of available and borrowed books.
TestLibrary
Test Cases:
test_add_book(): Tests if a book is added correctly.
test_borrow_book(): Tests if a book can be borrowed.
test_borrow_book_already_borrowed(): Tests the scenario where a borrowed book is attempted to be borrowed again.
test_borrow_book_not_in_library(): Tests borrowing a book that does not exist in the library.
test_return_book(): Tests if a borrowed book can be returned.
test_return_book_not_borrowed(): Tests returning a book that was not borrowed.
test_return_book_not_in_library(): Tests returning a book that is not in the library.
test_display_books(): Tests the display of available and borrowed books.

![image](https://github.com/user-attachments/assets/dd9b0cb3-492b-49a6-a8f6-7f0d2becf08b)
