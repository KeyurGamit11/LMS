class Library:
    def __init__(self):
        self.noBooks = 0
        self.books =[]

    
    def addBooks(self,books):
        self.books.append(books)
        self.noBooks = len(self.books)

    def showinfo(self):
        print(f"The Library has {self.noBooks} books , the books are")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBooks("keyur Gamit")
l1.addBooks("hello world")
l1.addBooks("Descipline....")
l1.showinfo()