"""
Financial calculation utilities module.

This module provides functions for common financial calculations including
currency formatting, tax calculations, percentage formatting, and discount applications.

All functions validate inputs and raise appropriate exceptions for invalid data.
"""


def format_currency(amount):
    """
    Format a numeric amount as currency string.
    
    Args:
        amount (float): The amount to format. Must be >= 0.
    
    Returns:
        str: Formatted currency string (e.g., "$100.00").
    
    Raises:
        TypeError: If amount is not numeric.
        ValueError: If amount is negative.
    
    Examples:
        >>> format_currency(100)
        '$100.00'
        >>> format_currency(99.99)
        '$99.99'
    """
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Amount must be numeric, got {type(amount).__name__}")
    
    if amount < 0:
        raise ValueError(f"Amount cannot be negative, got {amount}")
    
    return f"${amount:.2f}"


def calculate_tax(amount, rate):
    """
    Calculate tax amount for a given base amount and tax rate.
    
    Args:
        amount (float): Base amount before tax. Must be >= 0.
        rate (float): Tax rate as decimal (e.g., 0.08 for 8%). Must be between 0 and 1.
    
    Returns:
        float: Tax amount. Result is always >= 0.
    
    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If amount is negative or rate is outside [0, 1].
    
    Examples:
        >>> calculate_tax(100, 0.08)
        8.0
        >>> calculate_tax(50, 0.10)
        5.0
    """
    if not isinstance(amount, (int, float)):
        raise TypeError(f"Amount must be numeric, got {type(amount).__name__}")
    
    if not isinstance(rate, (int, float)):
        raise TypeError(f"Rate must be numeric, got {type(rate).__name__}")
    
    if amount < 0:
        raise ValueError(f"Amount cannot be negative, got {amount}")
    
    if rate < 0:
        raise ValueError(f"Tax rate cannot be negative, got {rate}")
    
    if rate > 1:
        raise ValueError(f"Tax rate cannot exceed 1.0 (100%), got {rate}")
    
    return amount * rate


def format_percentage(value):
    """
    Format a decimal value as a percentage string.
    
    Args:
        value (float): Decimal value to format (e.g., 0.08 for 8%). Should be between 0 and 1.
    
    Returns:
        str: Formatted percentage string (e.g., "8.0%").
    
    Raises:
        TypeError: If value is not numeric.
        ValueError: If value is negative or exceeds 1.
    
    Examples:
        >>> format_percentage(0.08)
        '8.0%'
        >>> format_percentage(0.125)
        '12.5%'
    """
    if not isinstance(value, (int, float)):
        raise TypeError(f"Value must be numeric, got {type(value).__name__}")
    
    if value < 0:
        raise ValueError(f"Percentage value cannot be negative, got {value}")
    
    if value > 1:
        raise ValueError(f"Percentage value cannot exceed 1.0 (100%), got {value}")
    
    return f"{value * 100}%"


def apply_discount(price, discount_rate):
    """
    Apply a discount rate to a price.
    
    Args:
        price (float): Original price. Must be >= 0.
        discount_rate (float): Discount rate as decimal (e.g., 0.10 for 10%). Must be between 0 and 1.
    
    Returns:
        float: Price after discount. Result is always >= 0.
    
    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If price is negative or discount_rate is outside [0, 1].
    
    Examples:
        >>> apply_discount(100, 0.10)
        90.0
        >>> apply_discount(50, 0.25)
        37.5
    """
    if not isinstance(price, (int, float)):
        raise TypeError(f"Price must be numeric, got {type(price).__name__}")
    
    if not isinstance(discount_rate, (int, float)):
        raise TypeError(f"Discount rate must be numeric, got {type(discount_rate).__name__}")
    
    if price < 0:
        raise ValueError(f"Price cannot be negative, got {price}")
    
    if discount_rate < 0:
        raise ValueError(f"Discount rate cannot be negative, got {discount_rate}")
    
    if discount_rate > 1:
        raise ValueError(f"Discount rate cannot exceed 1.0 (100%), got {discount_rate}")
    
    result = price * (1 - discount_rate)
    return max(0.0, result)  # Ensure never negative


def calculate_final_price(price, discount_rate, tax_rate):
    """
    Calculate final price after discount and tax.
    
    This is a convenience function that combines apply_discount and calculate_tax.
    
    Args:
        price (float): Original price. Must be >= 0.
        discount_rate (float): Discount rate as decimal (0-1). Must be between 0 and 1.
        tax_rate (float): Tax rate as decimal (0-1). Must be between 0 and 1.
    
    Returns:
        float: Final price after discount and tax. Result is always >= 0.
    
    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any input is invalid (see apply_discount and calculate_tax).
    
    Examples:
        >>> calculate_final_price(100, 0.10, 0.08)
        97.2
    """
    discounted_price = apply_discount(price, discount_rate)
    tax_amount = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax_amount


# Example usage
if __name__ == "__main__":
    price = 100
    tax_rate = 0.08
    discount_rate = 0.10
    
    # Calculate final price
    final = calculate_final_price(price, discount_rate, tax_rate)
    
    print(f"Price: {format_currency(price)}")
    print(f"After {format_percentage(discount_rate)} discount: {format_currency(apply_discount(price, discount_rate))}")
    print(f"Tax ({format_percentage(tax_rate)}): {format_currency(calculate_tax(apply_discount(price, discount_rate), tax_rate))}")
    print(f"Final: {format_currency(final)}")

