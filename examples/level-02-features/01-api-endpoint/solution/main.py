"""
User Management API

A well-structured REST API demonstrating proper request/response models,
validation, error handling, and documentation for AI-friendly development.

This API manages users with proper validation, type safety, and consistent
error handling. Designed to be easily understood and modified by AI assistants.
"""

from flask import Flask, request, jsonify
from pydantic import BaseModel, EmailStr, Field, ValidationError
from typing import List, Optional
from enum import Enum

app = Flask(__name__)

# ============================================================================
# Request/Response Models
# ============================================================================

class UserCreate(BaseModel):
    """
    Request model for creating a new user.
    
    Attributes:
        name: User's full name (1-100 characters)
        email: Valid email address
        age: User's age (0-150, optional, defaults to 0)
    
    Examples:
        >>> UserCreate(name="Alice", email="alice@example.com", age=25)
        UserCreate(name='Alice', email='alice@example.com', age=25)
    """
    name: str = Field(..., min_length=1, max_length=100, description="User's full name")
    email: EmailStr = Field(..., description="Valid email address")
    age: int = Field(default=0, ge=0, le=150, description="User's age (0-150)")

    class Config:
        schema_extra = {
            "example": {
                "name": "Alice Smith",
                "email": "alice@example.com",
                "age": 25
            }
        }


class UserUpdate(BaseModel):
    """
    Request model for updating an existing user.
    
    All fields are optional - only provided fields will be updated.
    
    Attributes:
        name: User's full name (1-100 characters, optional)
        email: Valid email address (optional)
        age: User's age (0-150, optional)
    """
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, ge=0, le=150)

    class Config:
        schema_extra = {
            "example": {
                "name": "Alice Johnson",
                "email": "alice.johnson@example.com",
                "age": 26
            }
        }


class UserResponse(BaseModel):
    """
    Response model for user data.
    
    This model represents a user as returned by the API.
    All fields are guaranteed to be present and valid.
    
    Attributes:
        id: Unique user identifier
        name: User's full name
        email: User's email address
        age: User's age
    """
    id: int = Field(..., description="Unique user identifier")
    name: str = Field(..., description="User's full name")
    email: str = Field(..., description="User's email address")
    age: int = Field(..., description="User's age")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Alice Smith",
                "email": "alice@example.com",
                "age": 25
            }
        }


class ErrorResponse(BaseModel):
    """
    Standard error response model.
    
    All API errors return this consistent structure.
    
    Attributes:
        error: Error type/code (e.g., "ValidationError", "NotFound")
        message: Human-readable error message
        status_code: HTTP status code
    """
    error: str = Field(..., description="Error type or code")
    message: str = Field(..., description="Human-readable error message")
    status_code: int = Field(..., description="HTTP status code")

    class Config:
        schema_extra = {
            "example": {
                "error": "ValidationError",
                "message": "Invalid email format",
                "status_code": 400
            }
        }


# ============================================================================
# Data Storage (In-memory for example)
# ============================================================================

class UserStore:
    """
    In-memory user storage.
    
    In production, this would be replaced with a database.
    Using a class allows for better testing and future migration.
    """
    def __init__(self):
        self._users: List[UserResponse] = []
        self._next_id = 1
    
    def create(self, user_data: UserCreate) -> UserResponse:
        """Create a new user and return the created user."""
        user = UserResponse(
            id=self._next_id,
            name=user_data.name,
            email=str(user_data.email),  # EmailStr to str
            age=user_data.age
        )
        self._users.append(user)
        self._next_id += 1
        return user
    
    def get_all(self) -> List[UserResponse]:
        """Get all users."""
        return self._users.copy()
    
    def get_by_id(self, user_id: int) -> Optional[UserResponse]:
        """Get user by ID, returns None if not found."""
        for user in self._users:
            if user.id == user_id:
                return user
        return None
    
    def update(self, user_id: int, user_data: UserUpdate) -> Optional[UserResponse]:
        """Update user by ID, returns updated user or None if not found."""
        for user in self._users:
            if user.id == user_id:
                # Update only provided fields
                if user_data.name is not None:
                    user.name = user_data.name
                if user_data.email is not None:
                    user.email = str(user_data.email)
                if user_data.age is not None:
                    user.age = user_data.age
                return user
        return None
    
    def delete(self, user_id: int) -> bool:
        """Delete user by ID, returns True if deleted, False if not found."""
        initial_count = len(self._users)
        self._users = [u for u in self._users if u.id != user_id]
        return len(self._users) < initial_count


# Global store instance
user_store = UserStore()


# ============================================================================
# Error Handlers
# ============================================================================

def make_error_response(error_type: str, message: str, status_code: int) -> tuple:
    """
    Create a standardized error response.
    
    Args:
        error_type: Error type/code (e.g., "ValidationError")
        message: Human-readable error message
        status_code: HTTP status code
    
    Returns:
        Tuple of (json response, status code) for Flask
    """
    error = ErrorResponse(
        error=error_type,
        message=message,
        status_code=status_code
    )
    return jsonify(error.dict()), status_code


@app.errorhandler(ValidationError)
def handle_validation_error(e: ValidationError):
    """Handle Pydantic validation errors."""
    errors = []
    for error in e.errors():
        field = ".".join(str(loc) for loc in error["loc"])
        message = error["msg"]
        errors.append(f"{field}: {message}")
    
    return make_error_response(
        error_type="ValidationError",
        message="Invalid input: " + "; ".join(errors),
        status_code=400
    )


@app.errorhandler(404)
def handle_not_found(e):
    """Handle 404 errors."""
    return make_error_response(
        error_type="NotFound",
        message="Resource not found",
        status_code=404
    )


@app.errorhandler(500)
def handle_internal_error(e):
    """Handle 500 errors."""
    return make_error_response(
        error_type="InternalError",
        message="An internal error occurred",
        status_code=500
    )


# ============================================================================
# API Endpoints
# ============================================================================

@app.route('/api/users', methods=['GET'])
def get_users():
    """
    Get all users.
    
    Returns a list of all users in the system.
    
    Returns:
        JSON array of UserResponse objects
        Status code: 200
    
    Example Response:
        [
            {
                "id": 1,
                "name": "Alice Smith",
                "email": "alice@example.com",
                "age": 25
            }
        ]
    """
    users = user_store.get_all()
    return jsonify([user.dict() for user in users]), 200


@app.route('/api/users', methods=['POST'])
def create_user():
    """
    Create a new user.
    
    Validates input and creates a new user.
    
    Request Body:
        {
            "name": "Alice Smith",        # Required, 1-100 chars
            "email": "alice@example.com", # Required, valid email
            "age": 25                      # Optional, 0-150, defaults to 0
        }
    
    Returns:
        UserResponse object
        Status code: 201 (Created)
    
    Errors:
        400: Validation error (invalid input)
        500: Internal server error
    
    Example Request:
        POST /api/users
        {
            "name": "Alice Smith",
            "email": "alice@example.com",
            "age": 25
        }
    
    Example Response:
        {
            "id": 1,
            "name": "Alice Smith",
            "email": "alice@example.com",
            "age": 25
        }
    """
    try:
        # Validate request body
        if not request.is_json:
            return make_error_response(
                error_type="ValidationError",
                message="Request must be JSON",
                status_code=400
            )
        
        user_data = UserCreate(**request.json)
        
        # Check for duplicate email (simple validation)
        existing_users = user_store.get_all()
        if any(u.email == str(user_data.email) for u in existing_users):
            return make_error_response(
                error_type="ValidationError",
                message=f"User with email {user_data.email} already exists",
                status_code=400
            )
        
        # Create user
        user = user_store.create(user_data)
        return jsonify(user.dict()), 201
    
    except ValidationError as e:
        return handle_validation_error(e)
    except Exception as e:
        return make_error_response(
            error_type="InternalError",
            message=f"Failed to create user: {str(e)}",
            status_code=500
        )


@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id: int):
    """
    Get a user by ID.
    
    Args:
        user_id: User ID to retrieve
    
    Returns:
        UserResponse object
        Status code: 200
    
    Errors:
        404: User not found
    
    Example Response:
        {
            "id": 1,
            "name": "Alice Smith",
            "email": "alice@example.com",
            "age": 25
        }
    """
    user = user_store.get_by_id(user_id)
    if user is None:
        return make_error_response(
            error_type="NotFound",
            message=f"User with ID {user_id} not found",
            status_code=404
        )
    
    return jsonify(user.dict()), 200


@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
    """
    Update a user by ID.
    
    Updates only the fields provided in the request body.
    
    Args:
        user_id: User ID to update
    
    Request Body:
        {
            "name": "Alice Johnson",       # Optional
            "email": "alice@example.com",  # Optional
            "age": 26                      # Optional
        }
    
    Returns:
        Updated UserResponse object
        Status code: 200
    
    Errors:
        400: Validation error
        404: User not found
        500: Internal server error
    
    Example Request:
        PUT /api/users/1
        {
            "name": "Alice Johnson",
            "age": 26
        }
    """
    try:
        # Validate request body
        if not request.is_json:
            return make_error_response(
                error_type="ValidationError",
                message="Request must be JSON",
                status_code=400
            )
        
        user_data = UserUpdate(**request.json)
        
        # Update user
        user = user_store.update(user_id, user_data)
        if user is None:
            return make_error_response(
                error_type="NotFound",
                message=f"User with ID {user_id} not found",
                status_code=404
            )
        
        return jsonify(user.dict()), 200
    
    except ValidationError as e:
        return handle_validation_error(e)
    except Exception as e:
        return make_error_response(
            error_type="InternalError",
            message=f"Failed to update user: {str(e)}",
            status_code=500
        )


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
    """
    Delete a user by ID.
    
    Args:
        user_id: User ID to delete
    
    Returns:
        Success message
        Status code: 200
    
    Errors:
        404: User not found
    
    Example Response:
        {
            "message": "User deleted successfully"
        }
    """
    deleted = user_store.delete(user_id)
    if not deleted:
        return make_error_response(
            error_type="NotFound",
            message=f"User with ID {user_id} not found",
            status_code=404
        )
    
    return jsonify({"message": "User deleted successfully"}), 200


# ============================================================================
# Health Check
# ============================================================================

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

