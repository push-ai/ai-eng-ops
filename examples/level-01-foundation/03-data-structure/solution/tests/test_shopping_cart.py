"""
Comprehensive tests for ShoppingCart data structure.
Demonstrates how tests verify invariants and behavior.
"""

import pytest
from main import ShoppingCart


class TestShoppingCartInitialization:
    """Tests for cart initialization."""
    
    def test_empty_cart_initialization(self):
        """Test that cart starts empty."""
        cart = ShoppingCart()
        assert cart.is_empty() is True
        assert cart.get_total() == 0.0
        assert cart.get_item_count() == 0
    
    def test_cart_items_property_is_readonly(self):
        """Test that items property returns read-only tuple."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        
        items = cart.items
        assert isinstance(items, tuple)
        
        # Should not be able to modify through property
        with pytest.raises(AttributeError):
            items.append({"item": "Banana", "price": 0.75})


class TestAddItem:
    """Tests for add_item method."""
    
    def test_add_item_success(self):
        """Test successful item addition."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        
        assert cart.get_item_count() == 1
        assert cart.get_total() == 1.50
        assert cart.is_empty() is False
    
    def test_add_multiple_items(self):
        """Test adding multiple items."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        cart.add_item("Orange", 2.00)
        
        assert cart.get_item_count() == 3
        assert cart.get_total() == 4.25
    
    def test_add_item_with_zero_price(self):
        """Test adding item with zero price."""
        cart = ShoppingCart()
        cart.add_item("Free Item", 0.0)
        
        assert cart.get_item_count() == 1
        assert cart.get_total() == 0.0
    
    def test_add_item_negative_price_raises_error(self):
        """Test that negative price raises ValueError."""
        cart = ShoppingCart()
        
        with pytest.raises(ValueError, match="cannot be negative"):
            cart.add_item("Apple", -1.50)
    
    def test_add_item_empty_name_raises_error(self):
        """Test that empty item name raises ValueError."""
        cart = ShoppingCart()
        
        with pytest.raises(ValueError, match="cannot be empty"):
            cart.add_item("", 1.50)
        
        with pytest.raises(ValueError, match="cannot be empty"):
            cart.add_item("   ", 1.50)
    
    def test_add_item_non_string_name_raises_error(self):
        """Test that non-string item name raises TypeError."""
        cart = ShoppingCart()
        
        with pytest.raises(TypeError, match="must be a string"):
            cart.add_item(123, 1.50)
        
        with pytest.raises(TypeError, match="must be a string"):
            cart.add_item(None, 1.50)
    
    def test_add_item_non_numeric_price_raises_error(self):
        """Test that non-numeric price raises TypeError."""
        cart = ShoppingCart()
        
        with pytest.raises(TypeError, match="must be numeric"):
            cart.add_item("Apple", "1.50")
    
    def test_add_duplicate_item_raises_error(self):
        """Test that adding duplicate item raises ValueError."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        
        with pytest.raises(ValueError, match="already exists"):
            cart.add_item("Apple", 2.00)
    
    def test_add_item_trims_whitespace(self):
        """Test that item names are trimmed."""
        cart = ShoppingCart()
        cart.add_item("  Apple  ", 1.50)
        
        # Should be able to remove using trimmed name
        assert cart.remove_item("Apple") is True


class TestRemoveItem:
    """Tests for remove_item method."""
    
    def test_remove_item_success(self):
        """Test successful item removal."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        
        result = cart.remove_item("Apple")
        
        assert result is True
        assert cart.get_item_count() == 1
        assert cart.get_total() == 0.75
    
    def test_remove_nonexistent_item_returns_false(self):
        """Test that removing nonexistent item returns False."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        
        result = cart.remove_item("Banana")
        
        assert result is False
        assert cart.get_item_count() == 1
    
    def test_remove_from_empty_cart(self):
        """Test removing from empty cart."""
        cart = ShoppingCart()
        
        result = cart.remove_item("Apple")
        
        assert result is False
    
    def test_remove_item_updates_total(self):
        """Test that removal updates total correctly."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        
        original_total = cart.get_total()
        cart.remove_item("Apple")
        
        assert cart.get_total() == original_total - 1.50
    
    def test_remove_non_string_raises_error(self):
        """Test that non-string item name raises TypeError."""
        cart = ShoppingCart()
        
        with pytest.raises(TypeError, match="must be a string"):
            cart.remove_item(123)


class TestUpdateItemPrice:
    """Tests for update_item_price method."""
    
    def test_update_item_price_success(self):
        """Test successful price update."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        
        result = cart.update_item_price("Apple", 2.00)
        
        assert result is True
        assert cart.get_total() == 2.00
    
    def test_update_nonexistent_item_returns_false(self):
        """Test that updating nonexistent item returns False."""
        cart = ShoppingCart()
        
        result = cart.update_item_price("Apple", 2.00)
        
        assert result is False
    
    def test_update_negative_price_raises_error(self):
        """Test that negative price raises ValueError."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        
        with pytest.raises(ValueError, match="cannot be negative"):
            cart.update_item_price("Apple", -1.00)
    
    def test_update_item_price_maintains_invariants(self):
        """Test that price update maintains cart invariants."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        
        cart.update_item_price("Apple", 2.00)
        
        # Total should be updated correctly
        assert cart.get_total() == 2.75
        # Item count should remain same
        assert cart.get_item_count() == 2


class TestGetTotal:
    """Tests for get_total method."""
    
    def test_get_total_empty_cart(self):
        """Test total for empty cart."""
        cart = ShoppingCart()
        assert cart.get_total() == 0.0
    
    def test_get_total_single_item(self):
        """Test total for single item."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        assert cart.get_total() == 1.50
    
    def test_get_total_multiple_items(self):
        """Test total for multiple items."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        cart.add_item("Orange", 2.00)
        assert cart.get_total() == 4.25
    
    def test_get_total_after_removal(self):
        """Test total after item removal."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        cart.remove_item("Apple")
        assert cart.get_total() == 0.75
    
    def test_get_total_is_always_sum(self):
        """Test that total always equals sum of prices (invariant)."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        
        assert cart.get_total() == sum(item["price"] for item in cart.items)
        
        cart.update_item_price("Apple", 2.00)
        assert cart.get_total() == sum(item["price"] for item in cart.items)


class TestCartInvariants:
    """Tests that verify cart invariants are maintained."""
    
    def test_invariant_no_negative_prices(self):
        """Test that cart cannot have negative prices."""
        cart = ShoppingCart()
        
        # Should not be able to add negative price
        with pytest.raises(ValueError):
            cart.add_item("Apple", -1.50)
        
        # Should not be able to update to negative price
        cart.add_item("Apple", 1.50)
        with pytest.raises(ValueError):
            cart.update_item_price("Apple", -1.00)
    
    def test_invariant_no_duplicate_items(self):
        """Test that cart cannot have duplicate items."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        
        # Should not be able to add duplicate
        with pytest.raises(ValueError, match="already exists"):
            cart.add_item("Apple", 2.00)
    
    def test_invariant_total_is_sum(self):
        """Test that total always equals sum of prices."""
        cart = ShoppingCart()
        
        # Empty cart
        assert cart.get_total() == sum(item["price"] for item in cart.items)
        
        # After adding items
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        assert cart.get_total() == sum(item["price"] for item in cart.items)
        
        # After removal
        cart.remove_item("Apple")
        assert cart.get_total() == sum(item["price"] for item in cart.items)
        
        # After update
        cart.update_item_price("Banana", 1.00)
        assert cart.get_total() == sum(item["price"] for item in cart.items)


class TestClearCart:
    """Tests for clear method."""
    
    def test_clear_empty_cart(self):
        """Test clearing empty cart."""
        cart = ShoppingCart()
        cart.clear()
        
        assert cart.is_empty() is True
        assert cart.get_total() == 0.0
    
    def test_clear_cart_with_items(self):
        """Test clearing cart with items."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        
        cart.clear()
        
        assert cart.is_empty() is True
        assert cart.get_total() == 0.0
        assert cart.get_item_count() == 0
    
    def test_can_add_after_clear(self):
        """Test that items can be added after clearing."""
        cart = ShoppingCart()
        cart.add_item("Apple", 1.50)
        cart.clear()
        cart.add_item("Banana", 0.75)
        
        assert cart.get_item_count() == 1
        assert cart.get_total() == 0.75


class TestCartStateTransitions:
    """Tests for state transitions and operations."""
    
    def test_complete_workflow(self):
        """Test complete shopping workflow."""
        cart = ShoppingCart()
        
        # Start empty
        assert cart.is_empty() is True
        
        # Add items
        cart.add_item("Apple", 1.50)
        cart.add_item("Banana", 0.75)
        assert cart.get_item_count() == 2
        assert cart.get_total() == 2.25
        
        # Update price
        cart.update_item_price("Apple", 2.00)
        assert cart.get_total() == 2.75
        
        # Remove item
        cart.remove_item("Banana")
        assert cart.get_item_count() == 1
        assert cart.get_total() == 2.00
        
        # Clear
        cart.clear()
        assert cart.is_empty() is True
        assert cart.get_total() == 0.0

