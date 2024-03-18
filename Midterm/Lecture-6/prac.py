def add_book(inventory, title, author, quantity, price):
    book = {
        "title": title,
        "author": author,
        "quantity": quantity,
        "price": price
    }
    if title in inventory:
        print(f"Book '{title}' already exists in the inventory. Please use 'update_quantity' to update its quantity.")
    else:
        inventory[title] = book


def update_quantity(inventory, title, new_quantity):
    if title in inventory:
        inventory[title]["quantity"] = new_quantity
        print(f"Quantity of book '{title}' updated to {new_quantity}.")
    else:
        print(f"Book '{title}' not found in the inventory.")


def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for title, book in inventory.items():
        print(f"Title: {book['title']}, Author: {book['author']}, Quantity: {book['quantity']}, Price: ${book['price']}")


# Example usage:
book_inventory = {}
add_book(book_inventory, "The Great Gatsby", "F. Scott Fitzgerald", 20, 10.99)
add_book(book_inventory, "To Kill a Mockingbird", "Harper Lee", 15, 12.50)
update_quantity(book_inventory, "The Great Gatsby", 25)
update_quantity(book_inventory, "1984", 30)
display_inventory(book_inventory)