# Problem: Database Models Without Structure

This example demonstrates database model code that works but lacks the structure needed for AI to reliably understand and modify it.

## The Problem

Without proper structure, AI struggles with database models because:

1. **No field constraints**: Missing validation and constraints
2. **No relationships defined**: Relationships unclear
3. **No indexes**: Performance issues
4. **No documentation**: Models and fields undocumented
5. **No tests**: No way to verify model behavior

## Setup

```bash
# Install dependencies
pip install django

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Test models in shell
python manage.py shell
```

## Issues to Notice

- Missing field constraints (email validation, age ranges)
- No unique constraints on email
- No indexes for performance
- No model methods or properties
- No documentation
- No model tests

When AI tries to modify these models, it will guess at:
- What constraints exist
- What relationships mean
- What indexes are needed
- What the model contract is

