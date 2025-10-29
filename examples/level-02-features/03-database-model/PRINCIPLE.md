# Database Model Principle: Structure Enables Reliable Database Design

## The Principle

**Well-structured database models with explicit field definitions, clear relationships, proper constraints, indexes, and comprehensive documentation enable AI to design and modify database schemas reliably.** When models have clear contracts, AI can understand and maintain them without guessing at requirements.

## Why This Matters for AI Engineering

### The Problem: AI Guesses at Database Structure

When AI encounters unstructured database models, it makes assumptions:

```python
# AI sees this:
email = models.CharField(max_length=255)

# AI guesses:
# - Is email unique? (no constraint shown)
# - Is email required? (no null=False shown)
# - Is email validated? (no validation shown)
# - Should there be an index? (no index shown)
```

Without structure, AI will:
- **Guess at constraints** and miss important validations
- **Miss relationships** between models
- **Forget indexes** causing performance issues
- **Create inconsistent models** because it doesn't know patterns
- **Break data integrity** when modifying schemas

### The Solution: Explicit Model Contracts

Structured models provide AI with clear contracts:

```python
class User(models.Model):
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True,
        help_text="User's email address"
    )
```

Now AI understands:
- **What constraints exist** (unique, required, etc.)
- **What relationships mean** (ForeignKey, ManyToMany, etc.)
- **What indexes are needed** (db_index=True)
- **What the model contract is** (explicit field definitions)

## Key Elements of Structured Database Models

### 1. **Explicit Field Definitions**

**Purpose**: Define all field attributes clearly.

**Why It Helps AI**:
- AI knows field types and constraints
- AI understands required vs optional fields
- AI can generate correct migrations
- AI can maintain field consistency

**Example**:
```python
age = models.IntegerField(
    null=False,
    blank=False,
    validators=[MinValueValidator(0), MaxValueValidator(150)],
    help_text="User's age (0-150)"
)
```

### 2. **Clear Relationships**

**Purpose**: Explicitly define relationships between models.

**Why It Helps AI**:
- AI knows how models relate
- AI understands cascade behaviors
- AI can generate correct queries
- AI can maintain referential integrity

**Example**:
```python
author = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='posts',
    help_text="Post author"
)
```

### 3. **Proper Constraints**

**Purpose**: Enforce data integrity at the database level.

**Why It Helps AI**:
- AI knows validation rules
- AI understands unique constraints
- AI can generate correct validators
- AI can maintain data integrity

**Example**:
```python
email = models.EmailField(unique=True, db_index=True)
```

### 4. **Indexes for Performance**

**Purpose**: Add indexes for frequently queried fields.

**Why It Helps AI**:
- AI knows which fields are indexed
- AI can add indexes when needed
- AI understands performance implications
- AI can maintain query performance

**Example**:
```python
email = models.EmailField(db_index=True)
created_at = models.DateTimeField(db_index=True)
```

### 5. **Model Methods and Properties**

**Purpose**: Add business logic to models.

**Why It Helps AI**:
- AI knows model capabilities
- AI understands business rules
- AI can generate correct code
- AI can maintain business logic

**Example**:
```python
@property
def full_name(self):
    return f"{self.first_name} {self.last_name}"

def is_adult(self):
    return self.age >= 18
```

### 6. **Model Documentation**

**Purpose**: Document models and fields.

**Why It Helps AI**:
- AI understands model purpose
- AI knows field meanings
- AI can generate correct queries
- AI can maintain documentation

**Example**:
```python
class User(models.Model):
    """
    User model representing a user in the system.
    
    Attributes:
        email: Unique email address (primary identifier)
        name: User's full name
        age: User's age (0-150)
    """
```

### 7. **Comprehensive Tests**

**Purpose**: Verify model behavior matches the contract.

**Why It Helps AI**:
- Tests define expected behavior
- AI can verify changes don't break contracts
- AI can iterate through test failures
- AI understands model behavior

## The Prompt

Copy this prompt and use it with your AI coding assistant:

```
I need you to refactor these database models to make them more reliable and easier for AI to understand and modify.

Please add:

1. **Explicit Field Definitions**:
   - Add null/blank constraints where appropriate
   - Add validators for fields (email, age ranges, etc.)
   - Add unique constraints where needed
   - Add db_index=True for frequently queried fields
   - Add help_text for all fields

2. **Clear Relationships**:
   - Add related_name to ForeignKey fields
   - Document cascade behaviors (on_delete)
   - Add help_text explaining relationships
   - Consider ManyToMany if needed

3. **Model Documentation**:
   - Add docstrings to all models
   - Document model purpose and attributes
   - Add field help_text
   - Include usage examples

4. **Model Methods**:
   - Add __str__ methods for better representation
   - Add useful properties
   - Add validation methods if needed
   - Add business logic methods

5. **Comprehensive Tests**:
   - Test model creation
   - Test field validation
   - Test relationships
   - Test constraints (unique, etc.)
   - Test model methods

Focus especially on:
- Making the model contract explicit through field definitions
- Ensuring data integrity through constraints
- Providing clear documentation
- Making models maintainable and testable

The goal is to create models that AI can reliably understand, modify, and extend without guessing at constraints, relationships, or validation rules.
```

## Expected Outcome

After restructuring the models, AI assistants will:

1. **Understand model contracts** through explicit field definitions
2. **Generate correct migrations** using defined constraints
3. **Maintain relationships** correctly through explicit definitions
4. **Add indexes** appropriately for performance
5. **Write tests** that verify model behavior
6. **Modify models safely** without breaking contracts

## Best Practices

### Field Definitions
- Always specify null/blank for all fields
- Add validators for data validation
- Use appropriate field types (EmailField, etc.)
- Add help_text for documentation

### Relationships
- Always add related_name to ForeignKey
- Document on_delete behavior
- Consider related_name conflicts
- Add help_text explaining relationships

### Constraints
- Add unique constraints where needed
- Add db_index for frequently queried fields
- Use database-level constraints when possible
- Document constraint rationale

### Documentation
- Add docstrings to all models
- Document all fields with help_text
- Include usage examples
- Explain business rules

### Testing
- Test model creation
- Test field validation
- Test relationships
- Test constraints
- Test model methods

Structured database models transform code from "works but unclear" to "explicit, reliable, and AI-friendly."

