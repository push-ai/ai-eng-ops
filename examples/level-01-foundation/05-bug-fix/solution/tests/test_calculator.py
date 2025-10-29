"""
Comprehensive tests for Calculator demonstrating TDD bug fixing approach.
Tests reproduce bugs, verify fixes, and cover edge cases.
"""

import pytest
from main import Calculator


class TestCalculateDiscount:
    """Tests for calculate_discount method."""
    
    def setup_method(self):
        """Set up test fixture."""
        self.calc = Calculator()
    
    def test_normal_discount(self):
        """Test normal discount calculation."""
        result = self.calc.calculate_discount(100, 10)
        assert result == 90.0
    
    def test_zero_discount(self):
        """Test 0% discount returns original price."""
        result = self.calc.calculate_discount(100, 0)
        assert result == 100.0
    
    def test_full_discount(self):
        """Test 100% discount returns zero."""
        result = self.calc.calculate_discount(100, 100)
        assert result == 0.0
    
    def test_fifty_percent_discount(self):
        """Test 50% discount."""
        result = self.calc.calculate_discount(100, 50)
        assert result == 50.0
    
    # BUG REPRODUCTION TESTS - These would fail with original code
    def test_negative_discount_raises_error(self):
        """Test that negative discount raises ValueError."""
        with pytest.raises(ValueError, match="cannot be negative"):
            self.calc.calculate_discount(100, -10)
    
    def test_discount_over_100_percent_raises_error(self):
        """Test that discount over 100% raises ValueError."""
        with pytest.raises(ValueError, match="cannot exceed 100%"):
            self.calc.calculate_discount(100, 150)
    
    def test_negative_price_raises_error(self):
        """Test that negative price raises ValueError."""
        with pytest.raises(ValueError, match="Price cannot be negative"):
            self.calc.calculate_discount(-100, 10)
    
    # EDGE CASE TESTS
    def test_zero_price_with_discount(self):
        """Test discount on zero price."""
        result = self.calc.calculate_discount(0, 50)
        assert result == 0.0
    
    def test_decimal_discount(self):
        """Test discount with decimal percentage."""
        result = self.calc.calculate_discount(100, 12.5)
        assert result == 87.5
    
    def test_result_never_negative(self):
        """Test that result is never negative (handles floating point edge cases)."""
        result = self.calc.calculate_discount(100, 100)
        assert result >= 0
    
    def test_exact_boundary_100_percent(self):
        """Test exact boundary at 100%."""
        result = self.calc.calculate_discount(100, 100)
        assert result == 0.0
    
    def test_exact_boundary_0_percent(self):
        """Test exact boundary at 0%."""
        result = self.calc.calculate_discount(100, 0)
        assert result == 100.0


class TestCalculateTotalWithTax:
    """Tests for calculate_total_with_tax method."""
    
    def setup_method(self):
        """Set up test fixture."""
        self.calc = Calculator()
    
    def test_normal_tax_calculation(self):
        """Test normal tax calculation."""
        result = self.calc.calculate_total_with_tax(100, 0.08)
        assert result == 108.0
    
    def test_zero_tax(self):
        """Test zero tax rate."""
        result = self.calc.calculate_total_with_tax(100, 0)
        assert result == 100.0
    
    def test_negative_subtotal_raises_error(self):
        """Test that negative subtotal raises ValueError."""
        with pytest.raises(ValueError, match="Subtotal cannot be negative"):
            self.calc.calculate_total_with_tax(-100, 0.08)
    
    def test_negative_tax_rate_raises_error(self):
        """Test that negative tax rate raises ValueError."""
        with pytest.raises(ValueError, match="Tax rate cannot be negative"):
            self.calc.calculate_total_with_tax(100, -0.08)
    
    def test_tax_rate_over_one_raises_error(self):
        """Test that tax rate over 1.0 raises ValueError."""
        with pytest.raises(ValueError, match="cannot exceed 1.0"):
            self.calc.calculate_total_with_tax(100, 1.5)


class TestBasicOperations:
    """Tests for basic calculator operations to ensure fixes don't break existing functionality."""
    
    def setup_method(self):
        """Set up test fixture."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition."""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(-5, 3) == -2
    
    def test_subtract(self):
        """Test subtraction."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(3, 5) == -2
    
    def test_multiply(self):
        """Test multiplication."""
        assert self.calc.multiply(5, 3) == 15
        assert self.calc.multiply(-5, 3) == -15
    
    def test_divide(self):
        """Test division."""
        assert self.calc.divide(10, 2) == 5.0
        assert self.calc.divide(7, 2) == 3.5
    
    def test_divide_by_zero_raises_error(self):
        """Test division by zero raises error."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)

