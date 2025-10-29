"""
Comprehensive tests for UserAuthenticator demonstrating effective testing
principles that help AI identify edge cases and iterate through improvements.
"""

import pytest
from main import UserAuthenticator


class TestUserRegistration:
    """Tests for user registration functionality."""
    
    def test_register_user_success(self):
        """Test successful user registration."""
        auth = UserAuthenticator()
        success, message = auth.register_user("alice", "password123", "alice@example.com")
        assert success is True
        assert message == "User registered successfully"
        assert "alice" in auth.users
    
    def test_register_user_duplicate_username(self):
        """Test registration with duplicate username fails."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        success, message = auth.register_user("alice", "different123", "different@example.com")
        assert success is False
        assert "already exists" in message.lower()
    
    def test_register_user_password_too_short(self):
        """Test registration with password below minimum length."""
        auth = UserAuthenticator()
        success, message = auth.register_user("alice", "short", "alice@example.com")
        assert success is False
        assert "too short" in message.lower()
    
    def test_register_user_password_exactly_minimum_length(self):
        """Test registration with password at exact minimum length."""
        auth = UserAuthenticator()
        success, message = auth.register_user("alice", "123456", "alice@example.com")
        assert success is True
    
    def test_register_user_password_one_below_minimum(self):
        """Test registration with password one character below minimum."""
        auth = UserAuthenticator()
        success, message = auth.register_user("alice", "12345", "alice@example.com")
        assert success is False
        assert "too short" in message.lower()
    
    def test_register_user_empty_username(self):
        """Test registration with empty username."""
        auth = UserAuthenticator()
        success, message = auth.register_user("", "password123", "alice@example.com")
        assert success is False
        assert "cannot be empty" in message.lower() or "required" in message.lower()
    
    def test_register_user_whitespace_only_username(self):
        """Test registration with whitespace-only username."""
        auth = UserAuthenticator()
        success, message = auth.register_user("   ", "password123", "alice@example.com")
        assert success is False
    
    def test_register_user_none_username(self):
        """Test registration with None username."""
        auth = UserAuthenticator()
        success, message = auth.register_user(None, "password123", "alice@example.com")
        assert success is False
        assert "required" in message.lower()
    
    def test_register_user_empty_password(self):
        """Test registration with empty password."""
        auth = UserAuthenticator()
        success, message = auth.register_user("alice", "", "alice@example.com")
        assert success is False
        assert "required" in message.lower() or "too short" in message.lower()
    
    def test_register_user_none_password(self):
        """Test registration with None password."""
        auth = UserAuthenticator()
        success, message = auth.register_user("alice", None, "alice@example.com")
        assert success is False
        assert "required" in message.lower()
    
    def test_register_user_invalid_email(self):
        """Test registration with invalid email format."""
        auth = UserAuthenticator()
        success, message = auth.register_user("alice", "password123", "notanemail")
        assert success is False
        assert "email" in message.lower()
    
    def test_register_user_empty_email(self):
        """Test registration with empty email."""
        auth = UserAuthenticator()
        success, message = auth.register_user("alice", "password123", "")
        assert success is False


class TestUserAuthentication:
    """Tests for user authentication functionality."""
    
    def test_authenticate_success(self):
        """Test successful authentication."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        success, message = auth.authenticate("alice", "password123")
        assert success is True
        assert "successful" in message.lower()
    
    def test_authenticate_wrong_password(self):
        """Test authentication with wrong password."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        success, message = auth.authenticate("alice", "wrongpassword")
        assert success is False
        assert "invalid password" in message.lower()
    
    def test_authenticate_nonexistent_user(self):
        """Test authentication for user that doesn't exist."""
        auth = UserAuthenticator()
        success, message = auth.authenticate("nonexistent", "password123")
        assert success is False
        assert "not found" in message.lower()
    
    def test_authenticate_inactive_user(self):
        """Test authentication for inactive user."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        auth.deactivate_user("alice")
        success, message = auth.authenticate("alice", "password123")
        assert success is False
        assert "inactive" in message.lower()
    
    def test_authenticate_empty_username(self):
        """Test authentication with empty username."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        success, message = auth.authenticate("", "password123")
        assert success is False
    
    def test_authenticate_none_username(self):
        """Test authentication with None username."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        success, message = auth.authenticate(None, "password123")
        assert success is False
        assert "required" in message.lower()
    
    def test_authenticate_empty_password(self):
        """Test authentication with empty password."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        success, message = auth.authenticate("alice", "")
        assert success is False
    
    def test_authenticate_whitespace_password(self):
        """Test authentication with whitespace-only password."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        success, message = auth.authenticate("alice", "   ")
        assert success is False


class TestUserDeactivation:
    """Tests for user deactivation functionality."""
    
    def test_deactivate_user_success(self):
        """Test successful user deactivation."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        result = auth.deactivate_user("alice")
        assert result is True
        assert auth.users["alice"]["active"] is False
    
    def test_deactivate_nonexistent_user(self):
        """Test deactivation of non-existent user."""
        auth = UserAuthenticator()
        result = auth.deactivate_user("nonexistent")
        assert result is False
    
    def test_deactivate_then_authenticate_fails(self):
        """Test that deactivated user cannot authenticate."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        auth.deactivate_user("alice")
        success, message = auth.authenticate("alice", "password123")
        assert success is False
        assert "inactive" in message.lower()
    
    def test_deactivate_empty_username(self):
        """Test deactivation with empty username."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        result = auth.deactivate_user("")
        assert result is False


class TestUserActivation:
    """Tests for user activation functionality."""
    
    def test_activate_user_success(self):
        """Test successful user activation."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        auth.deactivate_user("alice")
        result = auth.activate_user("alice")
        assert result is True
        assert auth.users["alice"]["active"] is True
    
    def test_activate_nonexistent_user(self):
        """Test activation of non-existent user."""
        auth = UserAuthenticator()
        result = auth.activate_user("nonexistent")
        assert result is False
    
    def test_activate_then_authenticate_succeeds(self):
        """Test that reactivated user can authenticate."""
        auth = UserAuthenticator()
        auth.register_user("alice", "password123", "alice@example.com")
        auth.deactivate_user("alice")
        auth.activate_user("alice")
        success, message = auth.authenticate("alice", "password123")
        assert success is True

