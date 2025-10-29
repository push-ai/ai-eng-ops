"""
Generate TypeScript types from Pydantic models.

This script generates TypeScript type definitions from Python Pydantic models,
ensuring frontend and backend types always match.
"""

import json
from typing import get_type_hints
from types import UserCreate, UserResponse

def python_to_typescript_type(python_type):
    """Convert Python type to TypeScript type."""
    type_map = {
        int: 'number',
        str: 'string',
        bool: 'boolean',
        float: 'number',
        Optional: lambda t: f'{python_to_typescript_type(t)} | null',
    }
    return type_map.get(python_type, 'any')

def generate_typescript_interface(model_class, class_name):
    """Generate TypeScript interface from Pydantic model."""
    fields = []
    for field_name, field_info in model_class.__fields__.items():
        ts_type = python_to_typescript_type(field_info.type_)
        optional = '?' if field_info.required else ''
        fields.append(f"  {field_name}{optional}: {ts_type};")
    
    return f"export interface {class_name} {{\n" + "\n".join(fields) + "\n}"

# Generate TypeScript types
typescript_types = f"""// Auto-generated from shared/types.py
// DO NOT EDIT MANUALLY - This file is generated from Python types

{generate_typescript_interface(UserCreate, 'UserCreate')}

{generate_typescript_interface(UserResponse, 'UserResponse')}
"""

# Write to file
with open('../frontend/src/shared/types.ts', 'w') as f:
    f.write(typescript_types)

print("TypeScript types generated successfully!")

