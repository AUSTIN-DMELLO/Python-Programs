class Node:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.next = None

class ShoppingCart:
    def __init__(self):
        self.head = None

    def add_item(self, item_name, quantity, price):
        new_item = Node(item_name, quantity, price)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_item

    def remove_item(self, item_name):
        current = self.head
        prev = None
        while current:
            if current.item_name == item_name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                break
            prev = current
            current = current.next

    def display_items(self):
        current = self.head
        while current:
            print(f"Item: {current.item_name}, Quantity: {current.quantity}, Price: {current.price}")
            current = current.next

    def calculate_total(self):
        total = 0
        current = self.head
        while current:
            total += current.quantity * current.price
            current = current.next
        return total

cart = ShoppingCart()
num_items = int(input("Enter the number of items to add to the cart: "))
for _ in range(num_items):
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    cart.add_item(item_name, quantity, price)

cart.display_items()
print("Total Amount:", cart.calculate_total())

remove_item_name = input("Enter item name to remove from the cart: ")
cart.remove_item(remove_item_name)

print("After removing item:")
cart.display_items()
print("Total Amount:", cart.calculate_total())
