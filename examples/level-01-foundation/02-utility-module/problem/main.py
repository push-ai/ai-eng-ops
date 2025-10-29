"""
A utility module with multiple related functions.
This demonstrates code that works but lacks organization for reuse and testing.
"""


def format_currency(amount):
    """Format amount as currency."""
    return f"${amount:.2f}"


def calculate_tax(amount, rate):
    """Calculate tax."""
    return amount * rate


def format_percentage(value):
    """Format as percentage."""
    return f"{value * 100}%"


def apply_discount(price, discount):
    """Apply discount."""
    return price * (1 - discount)


# Example usage
if __name__ == "__main__":
    price = 100
    tax_rate = 0.08
    discount = 0.10
    
    # Calculate final price
    discounted = apply_discount(price, discount)
    tax = calculate_tax(discounted, tax_rate)
    final = discounted + tax
    
    print(f"Price: {format_currency(price)}")
    print(f"After {format_percentage(discount)} discount: {format_currency(discounted)}")
    print(f"Tax ({format_percentage(tax_rate)}): {format_currency(tax)}")
    print(f"Final: {format_currency(final)}")
    
    # But what if inputs are invalid?
    # No validation, no tests, no module structure!

