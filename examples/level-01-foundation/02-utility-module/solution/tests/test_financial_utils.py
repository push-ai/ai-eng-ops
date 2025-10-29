"""
Comprehensive tests for financial utilities module.
Demonstrates how organized module structure enables systematic testing.
"""

import pytest
from main import (
    format_currency,
    calculate_tax,
    format_percentage,
    apply_discount,
    calculate_final_price
)


class TestFormatCurrency:
    """Tests for format_currency function."""
    
    def test_normal_amount(self):
        """Test normal currency formatting."""
        assert format_currency(100) == "$100.00"
        assert format_currency(99.99) == "$99.99"
    
    def test_zero_amount(self):
        """Test zero amount formatting."""
        assert format_currency(0) == "$0.00"
    
    def test_decimal_amount(self):
        """Test decimal amount formatting."""
        assert format_currency(123.456) == "$123.46"
    
    def test_negative_amount_raises_error(self):
        """Test that negative amount raises ValueError."""
        with pytest.raises(ValueError, match="cannot be negative"):
            format_currency(-100)
    
    def test_non_numeric_raises_error(self):
        """Test that non-numeric input raises TypeError."""
        with pytest.raises(TypeError, match="must be numeric"):
            format_currency("100")
        
        with pytest.raises(TypeError, match="must be numeric"):
            format_currency(None)


class TestCalculateTax:
    """Tests for calculate_tax function."""
    
    def test_normal_tax_calculation(self):
        """Test normal tax calculation."""
        assert calculate_tax(100, 0.08) == 8.0
        assert calculate_tax(50, 0.10) == 5.0
    
    def test_zero_tax_rate(self):
        """Test zero tax rate."""
        assert calculate_tax(100, 0) == 0.0
    
    def test_full_tax_rate(self):
        """Test 100% tax rate."""
        assert calculate_tax(100, 1.0) == 100.0
    
    def test_negative_amount_raises_error(self):
        """Test that negative amount raises ValueError."""
        with pytest.raises(ValueError, match="cannot be negative"):
            calculate_tax(-100, 0.08)
    
    def test_negative_rate_raises_error(self):
        """Test that negative rate raises ValueError."""
        with pytest.raises(ValueError, match="Tax rate cannot be negative"):
            calculate_tax(100, -0.08)
    
    def test_rate_over_one_raises_error(self):
        """Test that rate over 1.0 raises ValueError."""
        with pytest.raises(ValueError, match="cannot exceed 1.0"):
            calculate_tax(100, 1.5)
    
    def test_non_numeric_raises_error(self):
        """Test that non-numeric inputs raise TypeError."""
        with pytest.raises(TypeError):
            calculate_tax("100", 0.08)
        
        with pytest.raises(TypeError):
            calculate_tax(100, "0.08")


class TestFormatPercentage:
    """Tests for format_percentage function."""
    
    def test_normal_percentage(self):
        """Test normal percentage formatting."""
        assert format_percentage(0.08) == "8.0%"
        assert format_percentage(0.125) == "12.5%"
    
    def test_zero_percentage(self):
        """Test zero percentage."""
        assert format_percentage(0) == "0.0%"
    
    def test_full_percentage(self):
        """Test 100% percentage."""
        assert format_percentage(1.0) == "100.0%"
    
    def test_negative_value_raises_error(self):
        """Test that negative value raises ValueError."""
        with pytest.raises(ValueError, match="cannot be negative"):
            format_percentage(-0.10)
    
    def test_value_over_one_raises_error(self):
        """Test that value over 1.0 raises ValueError."""
        with pytest.raises(ValueError, match="cannot exceed 1.0"):
            format_percentage(1.5)
    
    def test_non_numeric_raises_error(self):
        """Test that non-numeric input raises TypeError."""
        with pytest.raises(TypeError):
            format_percentage("0.08")


class TestApplyDiscount:
    """Tests for apply_discount function."""
    
    def test_normal_discount(self):
        """Test normal discount application."""
        assert apply_discount(100, 0.10) == 90.0
        assert apply_discount(50, 0.25) == 37.5
    
    def test_zero_discount(self):
        """Test zero discount."""
        assert apply_discount(100, 0) == 100.0
    
    def test_full_discount(self):
        """Test 100% discount."""
        assert apply_discount(100, 1.0) == 0.0
    
    def test_negative_price_raises_error(self):
        """Test that negative price raises ValueError."""
        with pytest.raises(ValueError, match="Price cannot be negative"):
            apply_discount(-100, 0.10)
    
    def test_negative_discount_raises_error(self):
        """Test that negative discount raises ValueError."""
        with pytest.raises(ValueError, match="Discount rate cannot be negative"):
            apply_discount(100, -0.10)
    
    def test_discount_over_one_raises_error(self):
        """Test that discount over 1.0 raises ValueError."""
        with pytest.raises(ValueError, match="cannot exceed 1.0"):
            apply_discount(100, 1.5)
    
    def test_result_never_negative(self):
        """Test that result is never negative."""
        result = apply_discount(100, 1.0)
        assert result >= 0


class TestCalculateFinalPrice:
    """Tests for calculate_final_price convenience function."""
    
    def test_normal_calculation(self):
        """Test normal final price calculation."""
        # Price 100, 10% discount = 90, 8% tax = 7.2, total = 97.2
        result = calculate_final_price(100, 0.10, 0.08)
        assert abs(result - 97.2) < 0.01
    
    def test_zero_discount(self):
        """Test with zero discount."""
        result = calculate_final_price(100, 0, 0.08)
        assert result == 108.0
    
    def test_zero_tax(self):
        """Test with zero tax."""
        result = calculate_final_price(100, 0.10, 0)
        assert result == 90.0
    
    def test_both_zero(self):
        """Test with both discount and tax zero."""
        result = calculate_final_price(100, 0, 0)
        assert result == 100.0
    
    def test_uses_discount_then_tax(self):
        """Test that discount is applied before tax."""
        # If tax applied first: 100 + 8 = 108, then 10% discount = 97.2
        # If discount applied first: 100 - 10 = 90, then 8% tax = 7.2, total = 97.2
        # The correct order should be discount first, then tax
        result = calculate_final_price(100, 0.10, 0.08)
        discounted = apply_discount(100, 0.10)
        tax = calculate_tax(discounted, 0.08)
        expected = discounted + tax
        assert abs(result - expected) < 0.01
    
    def test_invalid_inputs_propagate_errors(self):
        """Test that invalid inputs raise appropriate errors."""
        with pytest.raises(ValueError):
            calculate_final_price(-100, 0.10, 0.08)
        
        with pytest.raises(ValueError):
            calculate_final_price(100, 1.5, 0.08)
        
        with pytest.raises(ValueError):
            calculate_final_price(100, 0.10, 1.5)


class TestFunctionIntegration:
    """Tests for function combinations and integration."""
    
    def test_complete_workflow(self):
        """Test complete workflow using all functions."""
        price = 100
        discount_rate = 0.10
        tax_rate = 0.08
        
        discounted = apply_discount(price, discount_rate)
        tax = calculate_tax(discounted, tax_rate)
        final = discounted + tax
        
        formatted_price = format_currency(price)
        formatted_discount = format_percentage(discount_rate)
        formatted_tax = format_percentage(tax_rate)
        formatted_final = format_currency(final)
        
        assert formatted_price == "$100.00"
        assert formatted_discount == "10.0%"
        assert formatted_tax == "8.0%"
        assert formatted_final == "$97.20"
    
    def test_functions_are_pure(self):
        """Test that functions don't have side effects."""
        original_price = 100
        
        # Call function multiple times
        result1 = apply_discount(original_price, 0.10)
        result2 = apply_discount(original_price, 0.10)
        
        # Results should be identical
        assert result1 == result2
        assert original_price == 100  # Original unchanged

