# API Endpoint Example - Solution

This directory contains a well-structured REST API that demonstrates how to build APIs that AI can reliably understand and modify.

## What Changed

The solution adds comprehensive structure that enables AI to:

1. **Understand API contracts** through explicit request/response models
2. **Validate inputs correctly** using Pydantic models
3. **Handle errors consistently** with standard error responses
4. **Generate correct code** without guessing at requirements
5. **Maintain consistency** when adding new endpoints

## Running the API

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py

# Server runs on http://localhost:5000
```

## Testing the API

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=main --cov-report=term-missing

# Test endpoints manually
curl http://localhost:5000/api/users
curl -X POST http://localhost:5000/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com","age":25}'
curl http://localhost:5000/api/users/1
```

## Key Improvements

### 1. Request/Response Models
- **UserCreate**: Request model with validation
- **UserUpdate**: Partial update model
- **UserResponse**: Response model with all fields
- **ErrorResponse**: Standard error response

### 2. Input Validation
- Email format validation
- String length constraints
- Number range validation
- Required field checking

### 3. Consistent Error Handling
- Standard ErrorResponse model
- Consistent HTTP status codes
- Helpful error messages
- Proper exception handling

### 4. API Documentation
- Docstrings on all endpoints
- Request/response examples
- Error documentation
- Clear parameter descriptions

### 5. Comprehensive Tests
- Successful request tests
- Validation error tests
- Not found error tests
- Edge case tests

## Benefits for AI

With this structure, AI assistants can:

1. Understand the API contract through models
2. Add new endpoints following the same pattern
3. Modify existing endpoints without breaking contracts
4. Generate correct validation code
5. Write tests that verify behavior

The key is providing explicit structure at every level: models, validation, errors, and documentation.

