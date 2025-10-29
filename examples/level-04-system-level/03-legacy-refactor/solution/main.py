"""
Refactored UserManager with modern structure.

This demonstrates incremental refactoring: tests added first, then type hints,
then validation, then refactoring - all while maintaining functionality.
"""

from typing import Dict, Optional, TypedDict
from pydantic import BaseModel, EmailStr, Field, ValidationError


# Step 1: Define explicit data structures
class User(TypedDict):
    """User data structure."""
    id: int
    name: str
    email: str
    age: int


class UserCreate(BaseModel):
    """Request model for creating a user."""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(ge=0, le=150)


class UserUpdate(BaseModel):
    """Request model for updating a user."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=0, le=150)


class UserManager:
    """
    Manages user data with proper validation and error handling.
    
    Refactored from legacy code while maintaining all functionality.
    """
    
    def __init__(self) -> None:
        """Initialize UserManager with empty user store."""
        self.users: Dict[int, User] = {}
        self.id_counter: int = 0
    
    def add_user(self, name: str, email: str, age: int) -> User:
        """
        Add a new user.
        
        Args:
            name: User's name (1-100 characters)
            email: Valid email address
            age: User's age (0-150)
        
        Returns:
            Created user dictionary
        
        Raises:
            ValidationError: If input validation fails
        """
        # Validate input using Pydantic
        try:
            user_data = UserCreate(name=name, email=email, age=age)
        except ValidationError as e:
            raise ValueError(f"Invalid user data: {e}")
        
        # Create user
        self.id_counter += 1
        user: User = {
            'id': self.id_counter,
            'name': user_data.name,
            'email': str(user_data.email),
            'age': user_data.age
        }
        self.users[self.id_counter] = user
        return user
    
    def get_user(self, user_id: int) -> Optional[User]:
        """
        Get user by ID.
        
        Args:
            user_id: User ID to retrieve
        
        Returns:
            User dictionary if found, None otherwise
        """
        return self.users.get(user_id)
    
    def update_user(
        self,
        user_id: int,
        name: Optional[str] = None,
        email: Optional[str] = None,
        age: Optional[int] = None
    ) -> Optional[User]:
        """
        Update user by ID.
        
        Args:
            user_id: User ID to update
            name: New name (optional)
            email: New email (optional)
            age: New age (optional)
        
        Returns:
            Updated user dictionary if found, None otherwise
        
        Raises:
            ValidationError: If input validation fails
        """
        if user_id not in self.users:
            return None
        
        # Validate updates
        try:
            update_data = UserUpdate(name=name, email=email, age=age)
        except ValidationError as e:
            raise ValueError(f"Invalid update data: {e}")
        
        # Update user
        user = self.users[user_id]
        if update_data.name is not None:
            user['name'] = update_data.name
        if update_data.email is not None:
            user['email'] = str(update_data.email)
        if update_data.age is not None:
            user['age'] = update_data.age
        
        return user
    
    def delete_user(self, user_id: int) -> bool:
        """
        Delete user by ID.
        
        Args:
            user_id: User ID to delete
        
        Returns:
            True if user was deleted, False if not found
        """
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
    
    def get_all_users(self) -> Dict[int, User]:
        """
        Get all users.
        
        Returns:
            Dictionary of all users (ID -> User)
        """
        return self.users.copy()


# Usage (maintains backward compatibility)
if __name__ == '__main__':
    manager = UserManager()
    user = manager.add_user('Alice', 'alice@example.com', 25)
    print(user)
    updated = manager.update_user(user['id'], age=26)
    print(updated)

