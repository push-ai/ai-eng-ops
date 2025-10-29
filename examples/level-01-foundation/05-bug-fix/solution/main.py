"""
A calculator module with bugs fixed using test-driven development.
This improved version addresses edge cases identified through failing tests.
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
            price: Original price (must be >= 0)
            discount_percent: Discount percentage between 0 and 100 (e.g., 10 for 10%)
        
        Returns:
            Price after discount
        
        Raises:
            ValueError: If price is negative or discount_percent is outside [0, 100]
        """
        # Validate inputs
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        if discount_percent < 0:
            raise ValueError("Discount percentage cannot be negative")
        
        if discount_percent > 100:
            raise ValueError("Discount percentage cannot exceed 100%")
        
        # Calculate discount
        discount_amount = price * (discount_percent / 100)
        result = price - discount_amount
        
        # Ensure result is not negative (in case of floating point issues)
        return max(0, result)
    
    def calculate_total_with_tax(self, subtotal, tax_rate):
        """
        Calculate total price including tax.
        
        Args:
            subtotal: Price before tax (must be >= 0)
            tax_rate: Tax rate as decimal between 0 and 1 (e.g., 0.08 for 8%)
        
        Returns:
            Total price with tax
        
        Raises:
            ValueError: If subtotal is negative or tax_rate is outside [0, 1]
        """
        # Validate inputs
        if subtotal < 0:
            raise ValueError("Subtotal cannot be negative")
        
        if tax_rate < 0:
            raise ValueError("Tax rate cannot be negative")
        
        if tax_rate > 1:
            raise ValueError("Tax rate cannot exceed 1.0 (100%)")
        
        tax_amount = subtotal * tax_rate
        return subtotal + tax_amount


# Example usage
if __name__ == "__main__":
    calc = Calculator()
    
    # Normal case
    result = calc.calculate_discount(100, 10)
    print(f"$100 with 10% discount: ${result}")
    print(f"Expected: $90.0")
    print(f"Match Y: {result == 90.0}")
    
    # Edge case: 0% discount
    result = calc.calculate_discount(100, 0)
    print(f"\n$100 with 0% discount: ${result}")
    print(f"Expected: $100.0")
    print(f"Match: {result == 100.0}")
    
    # Edge case: 100% discount
    result = calc.calculate_discount(100, 100)
    print(f"\n$100 with 100% discount: ${result}")
    print(f"Expected: $0.0")
    print(f"Match: {result == 0.0}")
    
    # Invalid case: negative discount (should raise error)
    try:
        result = calc.calculate_discount(100, -10)
        print(f"\nBUG: Should have raised ValueError but got: ${result}")
    except ValueError as e:
        print(f"\nCorrectly raised ValueError: {e}")

