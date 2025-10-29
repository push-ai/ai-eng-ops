"""
Comprehensive tests for calculate_discount function.
Demonstrates how tests enable safe iteration and verify correctness.
"""

import pytest
from main import calculate_discount


class TestCalculateDiscountHappyPath:
    """Tests for normal, expected behavior."""
    
    def test_normal_discount(self):
        """Test normal discount calculation."""
        result = calculate_discount(100, 10)
        assert result == 90.0
    
    def test_zero_discount(self):
        """Test 0% discount returns original price."""
        result = calculate_discount(100, 0)
        assert result == 100.0
    
    def test_full_discount(self):
        """Test 100% discount returns zero."""
        result = calculate_discount(100, 100)
        assert result == 0.0
    
    def test_partial_discount(self):
        """Test partial discount (25%)."""
        result = calculate_discount(100, 25)
        assert result == 75.0
    
    def test_decimal_price(self):
        """Test with decimal price."""
        result = calculate_discount(99.99, 10)
        assert abs(result - 89.991) < 0.01
    
    def test_decimal_discount(self):
        """Test with decimal discount percentage."""
        result = calculate_discount(100, 12.5)
        assert result == 87.5


class TestCalculateDiscountEdgeCases:
    """Tests for boundary conditions and edge cases."""
    
    def test_zero_price(self):
        """Test with zero price."""
        result = calculate_discount(0, 50)
        assert result == 0.0
    
    def test_exact_boundary_0_percent(self):
        """Test exact boundary at 0%."""
        result = calculate_discount(100, 0)
        assert result == 100.0
    
    def test_exact_boundary_100_percent(self):
        """Test exact boundary at 100%."""
        result = calculate_discount(100, 100)
        assert result == 0.0
    
    def test_small_price(self):
        """Test with very small price."""
        result = calculate_discount(0.01, 50)
        assert result == 0.005 or result == 0.0  # Handles floating point
    
    def test_large_price(self):
        """Test with large price."""
        result = calculate_discount(1000000, 10)
        assert result == 900000.0


class TestCalculateDiscountErrorCases:
    """Tests for error handling and input validation."""
    
    def test_negative_price_raises_error(self):
        """Test that negative price raises ValueError."""
        with pytest.raises(ValueError, match="cannot be negative"):
            calculate_discount(-100, 10)
    
    def test_negative_discount_raises_error(self):
        """Test that negative discount raises ValueError."""
        with pytest.raises(ValueError, match="cannot be negative"):
            calculate_discount(100, -10)
    
    def test_discount_over_100_raises_error(self):
        """Test that discount over 100% raises ValueError."""
        with pytest.raises(ValueError, match="cannot exceed 100%"):
            calculate_discount(100, 150)
    
    def test_none_price_raises_error(self):
        """Test that None price raises TypeError."""
        with pytest.raises(TypeError, match="must be numeric"):
            calculate_discount(None, 10)
    
    def test_none_discount_raises_error(self):
        """Test that None discount raises TypeError."""
        with pytest.raises(TypeError, match="must be numeric"):
            calculate_discount(100, None)
    
    def test_string_price_raises_error(self):
        """Test that string price raises TypeError."""
        with pytest.raises(TypeError, match="must be numeric"):
            calculate_discount("100", 10)
    
    def test_string_discount_raises_error(self):
        """Test that string discount raises TypeError."""
        with pytest.raises(TypeError, match="must be numeric"):
            calculate_discount(100, "10")


class TestCalculateDiscountResultProperties:
    """Tests to verify result properties."""
    
    def test_result_never_negative(self):
        """Test that result is never negative."""
        # Even with floating point precision issues
        result = calculate_discount(100, 100)
        assert result >= 0
    
    def test_result_never_exceeds_original_price(self):
        """Test that discounted price never exceeds original."""
        result = calculate_discount(100, 10)
        assert result <= 100
    
    def test_result_is_float(self):
        """Test that result is always a float."""
        result = calculate_discount(100, 10)
        assert isinstance(result, float)

