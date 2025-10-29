"""
Shopping cart data structure implementation.

This module provides a ShoppingCart class that maintains a collection of items
with prices and calculates totals.

Invariants:
- All items in cart have non-negative prices
- No duplicate items (by name)
- Cart total is always sum of item prices
"""


class ShoppingCart:
    """
    A shopping cart that maintains a collection of items with prices.
    
    The cart maintains the following invariants:
    - All items have non-negative prices
    - Each item name is unique (no duplicates)
    - Total is always sum of all item prices
    
    Attributes:
        items (list): List of dictionaries, each containing 'item' (str) and 'price' (float).
                     This is read-only from outside the class.
    
    Examples:
        >>> cart = ShoppingCart()
        >>> cart.add_item("Apple", 1.50)
        >>> cart.get_total()
        1.5
        >>> cart.remove_item("Apple")
        >>> cart.get_total()
        0.0
    """
    
    def __init__(self):
        """
        Initialize an empty shopping cart.
        
        The cart starts with no items and a total of 0.0.
        """
        self._items = []  # Protected internal state
    
    @property
    def items(self):
        """
        Get a read-only view of cart items.
        
        Returns:
            tuple: Tuple of item dictionaries. This prevents external modification.
        """
        return tuple(self._items)
    
    def add_item(self, item_name, price):
        """
        Add an item to the shopping cart.
        
        Args:
            item_name (str): Name of the item. Must be non-empty string.
            price (float): Price of the item. Must be >= 0.
        
        Raises:
            TypeError: If item_name is not a string or price is not numeric.
            ValueError: If item_name is empty or price is negative.
            ValueError: If item already exists in cart (duplicate prevention).
        
        Examples:
            >>> cart = ShoppingCart()
            >>> cart.add_item("Apple", 1.50)
            >>> cart.add_item("Banana", 0.75)
        """
        # Input validation
        if not isinstance(item_name, str):
            raise TypeError(f"Item name must be a string, got {type(item_name).__name__}")
        
        if not item_name.strip():
            raise ValueError("Item name cannot be empty")
        
        if not isinstance(price, (int, float)):
            raise TypeError(f"Price must be numeric, got {type(price).__name__}")
        
        if price < 0:
            raise ValueError(f"Price cannot be negative, got {price}")
        
        # Check for duplicates (maintain invariant: no duplicate items)
        if self._item_exists(item_name):
            raise ValueError(f"Item '{item_name}' already exists in cart. Use update_item() to change price.")
        
        # Add item (maintains invariants)
        self._items.append({
            "item": item_name.strip(),
            "price": float(price)
        })
    
    def remove_item(self, item_name):
        """
        Remove an item from the shopping cart.
        
        Args:
            item_name (str): Name of the item to remove.
        
        Returns:
            bool: True if item was removed, False if item was not found.
        
        Raises:
            TypeError: If item_name is not a string.
        
        Examples:
            >>> cart = ShoppingCart()
            >>> cart.add_item("Apple", 1.50)
            >>> cart.remove_item("Apple")
            True
            >>> cart.remove_item("Nonexistent")
            False
        """
        if not isinstance(item_name, str):
            raise TypeError(f"Item name must be a string, got {type(item_name).__name__}")
        
        item_name = item_name.strip()
        
        # Find and remove item
        for i, cart_item in enumerate(self._items):
            if cart_item["item"] == item_name:
                self._items.pop(i)
                return True
        
        return False
    
    def update_item_price(self, item_name, new_price):
        """
        Update the price of an existing item.
        
        Args:
            item_name (str): Name of the item to update.
            new_price (float): New price. Must be >= 0.
        
        Returns:
            bool: True if item was updated, False if item was not found.
        
        Raises:
            TypeError: If inputs are invalid types.
            ValueError: If new_price is negative.
        
        Examples:
            >>> cart = ShoppingCart()
            >>> cart.add_item("Apple", 1.50)
            >>> cart.update_item_price("Apple", 2.00)
            True
        """
        if not isinstance(item_name, str):
            raise TypeError(f"Item name must be a string, got {type(item_name).__name__}")
        
        if not isinstance(new_price, (int, float)):
            raise TypeError(f"Price must be numeric, got {type(new_price).__name__}")
        
        if new_price < 0:
            raise ValueError(f"Price cannot be negative, got {new_price}")
        
        item_name = item_name.strip()
        
        # Find and update item
        for cart_item in self._items:
            if cart_item["item"] == item_name:
                cart_item["price"] = float(new_price)
                return True
        
        return False
    
    def get_total(self):
        """
        Calculate the total price of all items in the cart.
        
        Returns:
            float: Sum of all item prices. Returns 0.0 for empty cart.
        
        Examples:
            >>> cart = ShoppingCart()
            >>> cart.get_total()
            0.0
            >>> cart.add_item("Apple", 1.50)
            >>> cart.get_total()
            1.5
        """
        total = sum(item["price"] for item in self._items)
        return float(total)
    
    def get_item_count(self):
        """
        Get the number of items in the cart.
        
        Returns:
            int: Number of items in cart.
        """
        return len(self._items)
    
    def is_empty(self):
        """
        Check if the cart is empty.
        
        Returns:
            bool: True if cart has no items, False otherwise.
        """
        return len(self._items) == 0
    
    def clear(self):
        """
        Remove all items from the cart.
        
        After calling this method, the cart will be empty and total will be 0.0.
        """
        self._items.clear()
    
    def _item_exists(self, item_name):
        """
        Check if an item exists in the cart (private helper method).
        
        Args:
            item_name (str): Name of the item to check.
        
        Returns:
            bool: True if item exists, False otherwise.
        """
        return any(item["item"] == item_name.strip() for item in self._items)
    
    def __repr__(self):
        """Return string representation of the cart."""
        return f"ShoppingCart(items={len(self._items)}, total=${self.get_total():.2f})"


# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    print("Adding items to cart:")
    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    cart.add_item("Orange", 2.00)
    
    print(f"Cart: {cart}")
    print(f"Total: ${cart.get_total():.2f}")
    print(f"Item count: {cart.get_item_count()}")
    
    print("\nRemoving Banana:")
    removed = cart.remove_item("Banana")
    print(f"Removed: {removed}")
    print(f"Total after removal: ${cart.get_total():.2f}")
    
    print("\nUpdating Apple price:")
    updated = cart.update_item_price("Apple", 2.00)
    print(f"Updated: {updated}")
    print(f"New total: ${cart.get_total():.2f}")
    
    print("\nClearing cart:")
    cart.clear()
    print(f"Cart empty: {cart.is_empty()}")
    print(f"Total: ${cart.get_total():.2f}")

