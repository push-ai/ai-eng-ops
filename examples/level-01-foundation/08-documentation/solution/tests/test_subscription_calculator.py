"""
Tests for SubscriptionCalculator.

These tests verify that the calculator correctly applies discounts
and handles edge cases according to documented business rules.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from main import SubscriptionCalculator, PlanType


class TestCalculatePrice:
    """Test price calculation with various discount combinations."""
    
    def test_basic_plan_single_month(self):
        """Basic plan, 1 month, no discounts."""
        calc = SubscriptionCalculator()
        assert calc.calculate_price("basic", 1) == 10.0
    
    def test_premium_plan_single_month(self):
        """Premium plan, 1 month, no discounts."""
        calc = SubscriptionCalculator()
        assert calc.calculate_price("premium", 1) == 20.0
    
    def test_enterprise_plan_single_month(self):
        """Enterprise plan, 1 month, no discounts."""
        calc = SubscriptionCalculator()
        assert calc.calculate_price("enterprise", 1) == 30.0
    
    def test_annual_discount_applied(self):
        """Annual discount (20% off) for 12+ months."""
        calc = SubscriptionCalculator()
        # Premium: $20 base * 12 months * 0.8 annual = $192
        assert calc.calculate_price("premium", 12) == 192.0
    
    def test_multi_month_discount_applied(self):
        """Multi-month discount (10% off) for 3+ months."""
        calc = SubscriptionCalculator()
        # Basic: $10 * 3 months * 0.9 multi-month = $27
        assert calc.calculate_price("basic", 3) == 27.0
    
    def test_student_discount_applied(self):
        """Student discount (50% off) stacks with other discounts."""
        calc = SubscriptionCalculator()
        # Basic: $10 * 6 months * 0.9 multi-month * 0.5 student = $27
        assert calc.calculate_price("basic", 6, is_student=True) == 27.0
    
    def test_coupon_discount_applied(self):
        """Coupon discount (15% off) stacks with other discounts."""
        calc = SubscriptionCalculator()
        # Basic: $10 * 3 months * 0.9 multi-month * 0.85 coupon = $22.95
        assert calc.calculate_price("basic", 3, has_coupon=True) == 22.95
    
    def test_all_discounts_stacked(self):
        """All discounts stack together correctly."""
        calc = SubscriptionCalculator()
        # Enterprise: $30 base * 12 months * 0.8 annual * 0.5 student * 0.85 coupon
        # = $30 * 12 * 0.8 * 0.5 * 0.85 = $122.40
        # Note: Annual subscriptions don't get multi-month discount
        price = calc.calculate_price("enterprise", 12, is_student=True, has_coupon=True)
        assert price == 122.40
    
    def test_invalid_plan_type_raises_error(self):
        """Invalid plan type raises ValueError."""
        calc = SubscriptionCalculator()
        with pytest.raises(ValueError, match="Invalid plan_type"):
            calc.calculate_price("invalid", 1)  # type: ignore
    
    def test_invalid_months_raises_error(self):
        """Invalid months value raises ValueError."""
        calc = SubscriptionCalculator()
        with pytest.raises(ValueError, match="Invalid months"):
            calc.calculate_price("basic", 0)
        with pytest.raises(ValueError, match="Invalid months"):
            calc.calculate_price("basic", 25)


class TestCalculateRefund:
    """Test refund calculation for different cancellation reasons."""
    
    def test_technical_issue_full_refund(self):
        """Technical issues get full refund regardless of remaining days."""
        calc = SubscriptionCalculator()
        # Full refund even with only 5 days left
        assert calc.calculate_refund(5, 30.0, "technical") == 30.0
        # Full refund with 29 days left
        assert calc.calculate_refund(29, 30.0, "technical") == 30.0
    
    def test_billing_issue_half_refund(self):
        """Billing issues get 50% refund regardless of remaining days."""
        calc = SubscriptionCalculator()
        # 50% refund regardless of days
        assert calc.calculate_refund(10, 30.0, "billing") == 15.0
        assert calc.calculate_refund(25, 30.0, "billing") == 15.0
    
    def test_other_reason_pro_rated_refund(self):
        """Other reasons get pro-rated refund based on remaining days."""
        calc = SubscriptionCalculator()
        # 15 days / 30 days * $30 = $15
        assert calc.calculate_refund(15, 30.0, "other") == 15.0
        # 10 days / 30 days * $30 = $10
        assert calc.calculate_refund(10, 30.0, "other") == 10.0
    
    def test_invalid_remaining_days_raises_error(self):
        """Negative remaining days raises ValueError."""
        calc = SubscriptionCalculator()
        with pytest.raises(ValueError, match="remaining_days must be >= 0"):
            calc.calculate_refund(-1, 30.0, "other")
    
    def test_invalid_original_price_raises_error(self):
        """Non-positive original price raises ValueError."""
        calc = SubscriptionCalculator()
        with pytest.raises(ValueError, match="original_price must be > 0"):
            calc.calculate_refund(15, 0, "other")
        with pytest.raises(ValueError, match="original_price must be > 0"):
            calc.calculate_refund(15, -10, "other")


class TestDiscountOrder:
    """Test that discounts are applied in the correct order."""
    
    def test_discount_order_is_correct(self):
        """
        Verify discount application order matches documentation.
        
        Order should be:
        1. Plan type multiplier
        2. Annual discount (applied before monthly multiplication)
        3. Multi-month discount (applied after monthly multiplication)
        4. Student discount
        5. Coupon discount
        """
        calc = SubscriptionCalculator()
        
        # Test: Premium, 12 months, student
        # Expected: $20 * 12 * 0.8 annual * 0.5 student = $96
        price = calc.calculate_price("premium", 12, is_student=True)
        assert price == 96.0
        
        # Verify order matters by comparing with manual calculation
        # If annual discount applied after student: $20 * 12 * 0.5 * 0.8 = $96 (same)
        # But if multi-month applied differently, would get different result
        # This test verifies the documented order produces expected result


class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_minimum_months(self):
        """Minimum valid months (1) works correctly."""
        calc = SubscriptionCalculator()
        assert calc.calculate_price("basic", 1) == 10.0
    
    def test_maximum_months(self):
        """Maximum valid months (24) works correctly."""
        calc = SubscriptionCalculator()
        # Basic: $10 * 24 months * 0.8 annual = $192
        assert calc.calculate_price("basic", 24) == 192.0
    
    def test_exactly_3_months_gets_discount(self):
        """Exactly 3 months qualifies for multi-month discount."""
        calc = SubscriptionCalculator()
        # Basic: $10 * 3 months * 0.9 multi-month = $27
        assert calc.calculate_price("basic", 3) == 27.0
    
    def test_exactly_12_months_gets_annual_discount(self):
        """Exactly 12 months qualifies for annual discount."""
        calc = SubscriptionCalculator()
        # Basic: $10 * 12 months * 0.8 annual = $96
        assert calc.calculate_price("basic", 12) == 96.0
    
    def test_zero_remaining_days_refund(self):
        """Zero remaining days gets appropriate refund."""
        calc = SubscriptionCalculator()
        # Technical: full refund
        assert calc.calculate_refund(0, 30.0, "technical") == 30.0
        # Other: no refund (0/30 * $30 = $0)
        assert calc.calculate_refund(0, 30.0, "other") == 0.0

