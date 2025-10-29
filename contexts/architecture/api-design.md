# API Design Standards

## Overview

This document defines standards for designing RESTful APIs in our systems. All APIs must follow these patterns to ensure consistency, reliability, and ease of use.

## Design Principles

### 1. RESTful Design

- **Resources as nouns**: `/users`, `/orders`, `/products`
- **HTTP methods**: GET (read), POST (create), PUT (update), DELETE (remove)
- **Idempotent operations**: PUT and DELETE should be idempotent
- **Stateless**: Each request contains all information needed

### 2. Resource Naming

- **Plural nouns**: Use plural for resource names
- **Lowercase with hyphens**: `user-preferences` not `userPreferences`
- **Nested resources**: `/users/{id}/orders` for nested resources
- **Avoid verbs**: Use HTTP methods, not verbs in URLs

```python
# Good
GET    /api/users
POST   /api/users
GET    /api/users/{id}
PUT    /api/users/{id}
DELETE /api/users/{id}
GET    /api/users/{id}/orders

# Bad
GET    /api/getUsers
POST   /api/createUser
GET    /api/user/{id}/getOrders
```

### 3. Request/Response Models

- **Pydantic models** for Python APIs
- **TypeScript interfaces** for TypeScript APIs
- **Shared types** when frontend/backend share codebase
- **Versioning** for API evolution

```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int
```

### 4. HTTP Status Codes

- **200 OK**: Successful GET, PUT, DELETE
- **201 Created**: Successful POST
- **400 Bad Request**: Invalid input/validation error
- **401 Unauthorized**: Authentication required
- **403 Forbidden**: Insufficient permissions
- **404 Not Found**: Resource doesn't exist
- **500 Internal Server Error**: Server error

### 5. Error Responses

- **Consistent structure**: All errors use same format
- **Error codes**: Machine-readable error codes
- **Messages**: Human-readable error messages
- **Context**: Include relevant context (field errors, etc.)

```python
class ErrorResponse(BaseModel):
    error: str           # Error code (e.g., "VALIDATION_ERROR")
    message: str         # Human-readable message
    status_code: int     # HTTP status code
    details: Optional[Dict[str, Any]] = None  # Additional context
```

### 6. Pagination

- **Offset-based** or **cursor-based** pagination
- **Consistent parameters**: `page`, `limit` or `offset`, `limit`
- **Metadata**: Include total count, next/prev links

```python
class PaginatedResponse(BaseModel):
    items: List[T]
    total: int
    page: int
    limit: int
    has_next: bool
    has_prev: bool
```

### 7. Filtering and Sorting

- **Query parameters**: Use query params for filtering
- **Consistent syntax**: `?status=active&sort=created_at&order=desc`
- **Documented**: Document all supported filters/sorts

### 8. Versioning

- **URL versioning**: `/api/v1/users`, `/api/v2/users`
- **Header versioning**: `Accept: application/vnd.api+json;version=1`
- **Backward compatibility**: Maintain old versions during transition

## Security

### Authentication

- **Bearer tokens**: Use `Authorization: Bearer <token>` header
- **API keys**: For service-to-service communication
- **OAuth 2.0**: For user authentication

### Authorization

- **Role-based**: Check user roles/permissions
- **Resource-based**: Verify user owns/accesses resource
- **Always verify**: Never trust client-provided IDs

### Input Validation

- **Validate all inputs**: Never trust client data
- **Sanitize data**: Prevent injection attacks
- **Rate limiting**: Prevent abuse
- **CORS**: Configure appropriately

## Performance

### Caching

- **HTTP caching**: Use ETags, Last-Modified headers
- **Response caching**: Cache frequently accessed data
- **Cache invalidation**: Clear cache on updates

### Response Optimization

- **Field selection**: Allow clients to request specific fields
- **Compression**: Use gzip/brotli compression
- **Pagination**: Always paginate large datasets

## Documentation

### OpenAPI/Swagger

- **All endpoints**: Documented in OpenAPI spec
- **Request/response**: Document all models
- **Examples**: Include request/response examples
- **Errors**: Document all possible errors

### API Documentation Site

- **Interactive docs**: Swagger UI or similar
- **Authentication**: Show how to authenticate
- **Examples**: Include code examples
- **Changelog**: Document API changes

## Examples

### Good API Design

```python
@router.post("/api/v1/users", response_model=UserResponse, status_code=201)
async def create_user(user_data: UserCreate) -> UserResponse:
    """
    Create a new user.
    
    - **name**: User's full name (required, 1-100 chars)
    - **email**: Valid email address (required, unique)
    - **age**: User's age (optional, 0-150)
    
    Returns created user with generated ID.
    """
    # Implementation
    pass

@router.get("/api/v1/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int) -> UserResponse:
    """
    Get user by ID.
    
    - **user_id**: User ID to retrieve
    
    Returns user if found, 404 if not found.
    """
    # Implementation
    pass
```

### Bad API Design

```python
@router.post("/api/createUser")
async def create_user(data: dict):
    # No validation, no types, no documentation
    pass
```

## References

- Service Boundaries: `contexts/architecture/service-boundaries.md`
- Security Standards: `contexts/security/api-security.md`

