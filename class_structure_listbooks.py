class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author}"

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
    def __init__(self, library_books):
        self.library_books = library_books

    def perform_transaction(self, book_title, patron, transaction_type, date):
        found_book = None
        for book in self.library_books:
            if book.title == book_title:
                found_book = book
                break
        
        if found_book:
            if transaction_type == "borrow":
                if found_book.available:
                    if found_book.borrow_book():
                        print(f"{patron.name} has borrowed {found_book.title} on {date}.")
                    else:
                        print(f"{found_book.title} is not available for borrowing.")
                else:
                    print(f"{found_book.title} is not available for borrowing.")
            elif transaction_type == "return":
                if not found_book.available:
                    if found_book.return_book():
                        print(f"{patron.name} has returned {found_book.title} on {date}.")
                    else:
                        print(f"{found_book.title} was not borrowed.")
                else:
                    print(f"{found_book.title} is already available.")
            else:
                print("Invalid transaction type.")
        else:
            print("Book not found in the library.")

library_books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", "9780141182636"),
    Book("To Kill a Mockingbird", "Harper Lee", "9780061120084"),
    Book("A Tale of Two Cities", "Charles Dickens", "9780061120065"),
    Book("The Little Prince", "Antoine de Saint-Exupéry", "9780061120024"),
    Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", "9780061120096"),
    Book("And Then There Were None", "Agatha Christie", "9780061120075"),
    Book("Dream of the Red Chamber", "Cao Xueqin", "9780061120063"),
    Book("The Hobbit", "J. R. R. Tolkien", "9780061120088"),
    Book("The Da Vinci Code", "Dan Brown", "9780061120045"),
    Book("The Catcher in the Rye", "J. D. Salinger", "97800611200869"),
    Book("Lolita", "Vladimir Nabokov", "9780061120067"),
]

patron1 = Patron("Navaneedh")
patron2 = Patron("Gokul")
patron3 = Patron("Keshav")
patron4 = Patron("Sanjay")
patron5 = Patron("Balaji")

library_transaction = LibraryTransaction(library_books)

library_transaction.perform_transaction("The Great Gatsby", patron4, "borrow", "06/04/2022")
library_transaction.perform_transaction("The Great Gatsby", patron2, "borrow", "06/04/2022")
library_transaction.perform_transaction("The Great Gatsby", patron4, "return", "06/05/2022")
library_transaction.perform_transaction("The Great Gatsby", patron5, "borrow", "07/05/2022")



