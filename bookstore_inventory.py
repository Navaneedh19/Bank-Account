class Bookstore:
    def __init__(self):
        self.inventory = {}  

    def add_book(self, title, author, quantity):
        # Add a book to the inventory
        if title in self.inventory:
            self.inventory[title]['quantity'] += quantity
            
        else:
            self.inventory[title] = {'author': author, 'quantity': quantity}

    def remove_book(self, title, quantity):
       
        if title in self.inventory:
            self.inventory[title]['quantity'] -= quantity
            if self.inventory[title]['quantity'] <= 0:
                del self.inventory[title]
        else:
            print("Book not found in inventory.")

    def search_book(self, title):
      
        if title in self.inventory:
            print(f"Searched:-\nTitle: {title}, Author: {self.inventory[title]['author']}, Quantity: {self.inventory[title]['quantity']}")
        else:
            print("Book not found in inventory.")

    def display_inventory(self):
       
        print("Book Inventory:")
        for title, info in self.inventory.items():
            print(f"Title: {title}, Author: {info['author']}, Quantity: {info['quantity']}")


bookstore = Bookstore()

bookstore.add_book("The Little Princes", "Antoine de Saint-Exupery", 20)
bookstore.add_book("The Da Vinci Code", "Dan Brown", 15)
bookstore.add_book("Lolita", "Vladimir Nabokov", 35)
bookstore.add_book("The Catcher in the Rye", "J.D. Salinger", 24)
bookstore.add_book("Dream of the Red Chamber", "Cao Xueqin", 13)


bookstore.display_inventory()

bookstore.search_book("Lolita")

bookstore.remove_book("Dream of the Red Chamber", 5)

bookstore.display_inventory()

                                                       