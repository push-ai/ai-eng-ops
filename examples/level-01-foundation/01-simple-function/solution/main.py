"""
A well-structured simple function with comprehensive documentation and validation.
This demonstrates how proper structure enables safe AI iteration.
"""


def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount percentage.
    
    Args:
        price (float): Original price before discount. Must be >= 0.
        discount_percent (float): Discount percentage (0-100). Must be between 0 and 100.
    
    Returns:
        float: Price after discount is applied. Result is always >= 0.
    
    Raises:
        ValueError: If price is negative or discount_percent is outside [0, 100].
        TypeError: If inputs are not numeric.
    
    Examples:
        >>> calculate_discount(100, 10)
        90.0
        >>> calculate_discount(50, 0)
        50.0
        >>> calculate_discount(100, 100)
        0.0
    """
    # Input validation
    if not isinstance(price, (int, float)):
        raise TypeError(f"Price must be numeric, got {type(price).__name__}")
    
    if not isinstance(discount_percent, (int, float)):
        raise TypeError(f"Discount percent must be numeric, got {type(discount_percent).__name__}")
    
    if price < 0:
        raise ValueError(f"Price cannot be negative, got {price}")
    
    if discount_percent < 0:
        raise ValueError(f"Discount percentage cannot be negative, got {discount_percent}")
    
    if discount_percent > 100:
        raise ValueError(f"Discount percentage cannot exceed 100%, got {discount_percent}")
    
    # Calculate discount
    discount_amount = price * (discount_percent / 100)
    result = price - discount_amount
    
    # Ensure result is never negative (handles floating point edge cases)
    return max(0.0, result)


if __name__ == "__main__":
    # Example usage
    print("Testing calculate_discount function:")
    
    # Normal case
    result = calculate_discount(100, 10)
    print(f"$100 with 10% discount: ${result} (expected: $90.0)")
    
    # Edge case: 0% discount
    result = calculate_discount(100, 0)
    print(f"$100 with 0% discount: ${result} (expected: $100.0)")
    
    # Edge case: 100% discount
    result = calculate_discount(100, 100)
    print(f"$100 with 100% discount: ${result} (expected: $0.0)")
    
    # Error case: negative discount
    try:
        result = calculate_discount(100, -10)
    except ValueError as e:
        print(f"Correctly caught error: {e}")

