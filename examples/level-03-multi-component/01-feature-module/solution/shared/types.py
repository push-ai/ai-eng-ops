"""
Shared type definitions for User feature module.

This is the single source of truth for User types across frontend and backend.
Types are defined here once and generated/imported by both sides.
"""

from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    """Request model for creating a user."""
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(default=0, ge=0, le=150)


class UserResponse(BaseModel):
    """Response model for user data."""
    id: int
    name: str
    email: str
    age: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Alice Smith",
                "email": "alice@example.com",
                "age": 25
            }
        }

