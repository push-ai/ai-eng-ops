"""
A simple function example without proper testing or documentation.
This demonstrates code that works but lacks structure for AI iteration.
"""


def calculate_discount(price, discount_percent):
    """Calculate price after discount."""
    discount = price * discount_percent / 100
    return price - discount


if __name__ == "__main__":
    # Some basic usage
    result = calculate_discount(100, 10)
    print(f"Price $100 with 10% discount: ${result}")
    
    # But what about edge cases?
    # What if discount is 0? Negative? Over 100%?
    # What if price is negative?
    # No tests to verify behavior!

