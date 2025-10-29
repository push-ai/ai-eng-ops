# Problem: API Endpoint Without Structure

This example demonstrates API code that works but lacks the structure needed for AI to reliably understand and modify it.

## The Problem

Without proper structure, AI struggles with APIs because:

1. **No type safety**: Request/response structures aren't defined
2. **No validation**: Input validation is missing or inconsistent
3. **No error handling**: Errors aren't handled consistently
4. **No documentation**: API contract isn't clearly defined
5. **No tests**: No way to verify API behavior

## Run the Code

```bash
# Install dependencies
pip install flask

# Run the server
python main.py

# Test endpoints (in another terminal)
curl http://localhost:5000/api/users
curl -X POST http://localhost:5000/api/users -H "Content-Type: application/json" -d '{"name":"Alice","email":"alice@example.com"}'
curl http://localhost:5000/api/users/1
```

## Issues to Notice

- No request/response models defined
- No input validation
- Inconsistent error responses
- No type hints
- No API documentation
- No tests

When AI tries to modify this API, it will guess at:
- What fields are required
- What validation rules exist
- What error responses should look like
- What the API contract is

