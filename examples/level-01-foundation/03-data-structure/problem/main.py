"""
A simple data structure implementation.
This demonstrates a class that works but lacks proper structure for testing and extension.
"""


class ShoppingCart:
    """A simple shopping cart."""
    
    def __init__(self):
        self.items = []
    
    def add_item(self, item, price):
        """Add item to cart."""
        self.items.append({"item": item, "price": price})
    
    def get_total(self):
        """Get total price."""
        total = 0
        for item in self.items:
            total += item["price"]
        return total
    
    def remove_item(self, item):
        """Remove item from cart."""
        for i, cart_item in enumerate(self.items):
            if cart_item["item"] == item:
                self.items.pop(i)
                break


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    cart.add_item("Orange", 2.00)
    
    print(f"Total: ${cart.get_total()}")
    
    cart.remove_item("Banana")
    print(f"Total after removal: ${cart.get_total()}")
    
    # But what about edge cases?
    # What if we remove item that doesn't exist?
    # What if price is negative?
    # What if item is None?
    # No validation, no tests!

