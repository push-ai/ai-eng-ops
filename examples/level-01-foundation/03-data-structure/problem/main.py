"""
A simple data structure implementation WITHOUT strong typing.
This demonstrates how lack of type annotations causes AI to guess and spiral.

CRITICAL ISSUE: Without type hints, AI doesn't know:
- What type should 'item' be? (str? dict? object?)
- What type should 'price' be? (int? float? Decimal?)
- What does get_total() return? (int? float?)
- What structure do items have? (what keys?)
"""


class ShoppingCart:
    """A simple shopping cart."""
    
    def __init__(self):
        self.items = []  # What type? List of what?
    
    def add_item(self, item, price):
        """Add item to cart. What types? AI guesses..."""
        self.items.append({"item": item, "price": price})
    
    def get_total(self):
        """Get total price. Returns what type? AI assumes..."""
        total = 0
        for item in self.items:
            total += item["price"]
        return total
    
    def remove_item(self, item):
        """Remove item from cart. What type is item? AI guesses..."""
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

