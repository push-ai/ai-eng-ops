"""
Tests for UserManager.

These tests verify that refactored code maintains all legacy functionality
while adding new capabilities.
"""

import pytest
from main import UserManager, User


class TestUserManager:
    """Test UserManager functionality."""
    
    def test_add_user_success(self):
        """Test successful user creation."""
        manager = UserManager()
        user = manager.add_user('Alice', 'alice@example.com', 25)
        
        assert user['id'] == 1
        assert user['name'] == 'Alice'
        assert user['email'] == 'alice@example.com'
        assert user['age'] == 25
    
    def test_add_user_validation(self):
        """Test input validation."""
        manager = UserManager()
        
        # Invalid email
        with pytest.raises(ValueError):
            manager.add_user('Alice', 'invalid-email', 25)
        
        # Invalid age
        with pytest.raises(ValueError):
            manager.add_user('Alice', 'alice@example.com', 200)
    
    def test_get_user_found(self):
        """Test getting existing user."""
        manager = UserManager()
        created = manager.add_user('Alice', 'alice@example.com', 25)
        user = manager.get_user(created['id'])
        
        assert user == created
    
    def test_get_user_not_found(self):
        """Test getting non-existent user."""
        manager = UserManager()
        user = manager.get_user(999)
        
        assert user is None
    
    def test_update_user_success(self):
        """Test successful user update."""
        manager = UserManager()
        created = manager.add_user('Alice', 'alice@example.com', 25)
        updated = manager.update_user(created['id'], age=26)
        
        assert updated['age'] == 26
        assert updated['name'] == 'Alice'  # Unchanged
    
    def test_update_user_not_found(self):
        """Test updating non-existent user."""
        manager = UserManager()
        result = manager.update_user(999, age=26)
        
        assert result is None
    
    def test_delete_user_success(self):
        """Test successful user deletion."""
        manager = UserManager()
        created = manager.add_user('Alice', 'alice@example.com', 25)
        deleted = manager.delete_user(created['id'])
        
        assert deleted is True
        assert manager.get_user(created['id']) is None
    
    def test_delete_user_not_found(self):
        """Test deleting non-existent user."""
        manager = UserManager()
        deleted = manager.delete_user(999)
        
        assert deleted is False

