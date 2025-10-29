"""
A calculator module with a bug that needs to be fixed.
This example demonstrates how to reproduce a bug locally and fix it using TDD.
"""


class Calculator:
    """Simple calculator with basic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def calculate_discount(self, price, discount_percent):
        """
        Calculate price after discount.
        
        Args:
            price: Original price
            discount_percent: Discount percentage (e.g., 10 for 10%)
        
        Returns:
            Price after discount
        """
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    
    def calculate_total_with_tax(self, subtotal, tax_rate):
        """
        Calculate total price including tax.
        
        Args:
            subtotal: Price before tax
            tax_rate: Tax rate as decimal (e.g., 0.08 for 8%)
        
        Returns:
            Total price with tax
        """
        tax_amount = subtotal * tax_rate
        return subtotal + tax_amount


# Example usage demonstrating the bug
if __name__ == "__main__":
    calc = Calculator()
    
    # This should work fine
    result = calc.calculate_discount(100, 10)
    print(f"$100 with 10% discount: ${result}")
    print(f"Expected: $90.0")
    print(f"Match: {result == 90.0}")
    
    # This reveals a potential bug - what about edge cases?
    result = calc.calculate_discount(100, 0)
    print(f"\n$100 with 0% discount: ${result}")
    print(f"Expected: $100.0")
    print(f"Match: {result == 100.0}")
    
    # What about negative discounts? (should this be allowed?)
    result = calc.calculate_discount(100, -10)
    print(f"\n$100 with -10% discount: ${result}")
    print(f"This might be a bug - negative discount gives ${result}")

