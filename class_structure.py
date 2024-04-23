class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author}"

    def check_availability(self):
        return self.available

    def borrow_book(self):
        if self.available:
            self.available = False
            return True
        else:
            print("Sorry, this book is currently unavailable.")
            return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        else:
            print("This book is already available.")
            return False


class Patron:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class LibraryTransaction:
    def __init__(self, book, patron, transaction_type, date):
        self.book = book
        self.patron = patron
        self.transaction_type = transaction_type
        self.date = date

    def perform_transaction(self):
        if self.transaction_type == "borrow":
            if self.book.borrow_book():
                print(f"{self.patron.name} has borrowed {self.book.title} on {self.date}.")
        elif self.transaction_type == "return":
            if self.book.return_book():
                print(f"{self.patron.name} has returned {self.book.title} on {self.date}.")
        else:
            print("Invalid transaction type.")


book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780141182636")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
patron1 = Patron("Navaneedh")
patron2 = Patron("Gokul")

transaction1 = LibraryTransaction(book1, patron1, "borrow", "12/06/2021")
transaction1.perform_transaction()

transaction2 = LibraryTransaction(book1, patron1, "return", "19/06/2022")
transaction2.perform_transaction()

transaction3 = LibraryTransaction(book2, patron2, "borrow", "01/07/2022")
transaction3.perform_transaction()

transaction4 = LibraryTransaction(book1, patron1, "borrow", "05/07/2022")
transaction4.perform_transaction()
