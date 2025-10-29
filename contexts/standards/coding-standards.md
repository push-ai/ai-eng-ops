# Coding Standards

This document defines the coding standards and best practices for our engineering team. These standards ensure consistency, maintainability, and quality across our codebase.

## Language & Framework Preferences

### Primary Languages
- **TypeScript**: Preferred for new projects and components
- **JavaScript**: Acceptable for legacy code or simple scripts
- **Python**: Used for data processing, automation, and ML workflows
- **Go**: Used for high-performance services and CLI tools

### Framework Choices
- **Frontend**: React with TypeScript, Next.js for full-stack applications
- **Backend**: Node.js with Express/Fastify, Python with FastAPI
- **Testing**: Jest for JavaScript/TypeScript, pytest for Python
- **Documentation**: JSDoc/TSDoc for code documentation

## Code Style

### Naming Conventions

#### Variables and Functions
- Use `camelCase` for variables and functions
- Use descriptive names that explain purpose
- Prefix boolean variables with `is`, `has`, `should`, etc.
- Use verbs for functions: `getUser()`, `calculateTotal()`, `validateInput()`

#### Classes and Components
- Use `PascalCase` for classes and React components
- Use nouns: `UserService`, `PaymentProcessor`, `Dashboard`

#### Constants
- Use `UPPER_SNAKE_CASE` for constants
- Group related constants: `API_ENDPOINTS`, `ERROR_CODES`

#### Files and Directories
- Use `kebab-case` for file and directory names
- React components: `user-profile.tsx`
- Utilities: `format-date.ts`
- Tests: `user-profile.test.ts`

### Code Organization

#### File Structure
- One class/component per file
- Co-locate related files (component + styles + tests)
- Use index files for clean imports
- Separate concerns (UI, business logic, data access)

#### Function Length
- Maximum function length: **50 lines**
- Maximum file length: **300 lines**
- Extract complex logic into helper functions
- Break large functions into smaller, focused functions

#### Comment Guidelines
- Write self-documenting code (prefer clear code">comments)
- Use comments to explain "why", not "what"
- Document complex algorithms and business logic
- Remove commented-out code before committing
- Use JSDoc/TSDoc for public APIs

## Design Patterns & Principles

### SOLID Principles
- **Single Responsibility**: Each class/function should have one reason to change
- **Open/Closed**: Open for extension, closed for modification
- **Liskov Substitution**: Subtypes must be substitutable for their base types
- **Interface Segregation**: Clients shouldn't depend on interfaces they don't use
- **Dependency Inversion**: Depend on abstractions, not concretions

### Design Patterns to Prefer
- **Factory Pattern**: For object creation complexity
- **Strategy Pattern**: For interchangeable algorithms
- **Observer Pattern**: For event-driven architectures
- **Repository Pattern**: For data access abstraction
- **Dependency Injection**: For testability and flexibility

### Anti-Patterns to Avoid
- ❌ God Objects (classes that do too much)
- ❌ Spaghetti Code (unstructured, difficult to follow)
- ❌ Magic Numbers (use named constants)
- ❌ Copy-Paste Programming (extract common code)
- ❌ Premature Optimization (optimize only when needed)

## Error Handling

### Error Handling Patterns
- Use try-catch blocks for error handling
- Throw meaningful error messages
- Use custom error types when appropriate
- Log errors with context
- Never swallow errors silently

### Example
```typescript
try {
  const user = await userService.getUser(userId);
  if (!user) {
    throw new NotFoundError(`User ${userId} not found`);
  }
  return user;
} catch (error) {
  logger.error('Failed to get user', { userId, error });
  throw error;
}
```

## Code Quality Rules

### Complexity
- Maximum cyclomatic complexity: **10** per function
- Avoid deeply nested conditionals (max 3 levels)
- Use early returns to reduce nesting
- Extract complex conditions into named functions

### Duplication
- Follow DRY (Don't Repeat Yourself) principle
- Extract common patterns into utilities
- Create reusable components
- Use configuration for repeated values

### Performance
- Avoid premature optimization
- Profile before optimizing
- Use appropriate data structures
- Consider algorithmic complexity
- Cache expensive computations when appropriate

## Testing Standards

### Test Coverage Requirements
- Minimum **80% code coverage** for new code
- **100% coverage** for critical business logic
- Test edge cases and error scenarios
- Use descriptive test names

### Test Organization
- One test file per source file
- Group related tests with `describe` blocks
- Use `beforeEach`/`afterEach` for setup/teardown
- Keep tests independent and isolated

## Security Guidelines

### Input Validation
- Always validate and sanitize user inputs
- Use parameterized queries to prevent SQL injection
- Escape output to prevent XSS attacks
- Validate file uploads (type, size, content)

### Authentication & Authorization
- Never trust client-side validation alone
- Verify permissions server-side
- Use secure password hashing (bcrypt, Argon2)
- Implement proper session management

### Secrets Management
- Never commit secrets to version control
- Use environment variables or secrets management
- Rotate secrets regularly
- Audit secret usage

## Documentation Standards

### Code Documentation
- Document public APIs with JSDoc/TSDoc
- Explain complex algorithms and business logic
- Include examples for public functions
- Document parameters and return values

### README Files
- Include setup instructions
- Document environment variables
- Provide usage examples
- Include contribution guidelines

## Code Review Checklist

Before submitting code for review, ensure:
- [ ] Code follows style guide
- [ ] Tests are written and passing
- [ ] Documentation is updated
- [ ] No console.logs or debug code
- [ ] No commented-out code
- [ ] Error handling is appropriate
- [ ] Performance considerations addressed
- [ ] Security best practices followed

## Tools & Linting

### Linting Tools
- **ESLint**: JavaScript/TypeScript linting
- **Prettier**: Code formatting
- **TypeScript**: Type checking
- **ESLint plugins**: React, security, accessibility

### Pre-commit Hooks
- Run linters before commit
- Format code automatically
- Run tests before commit (optional)
- Prevent committing secrets

## Version Control

### Commit Messages
- Use descriptive commit messages
- Reference issue numbers when applicable
- Follow conventional commits format:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation
  - `refactor:` for code refactoring
  - `test:` for tests
  - `chore:` for maintenance

### Branch Naming
- `feature/` for new features
- `fix/` for bug fixes
- `hotfix/` for urgent production fixes
- `refactor/` for refactoring

## Continuous Improvement

These standards evolve based on:
- Team feedback and discussions
- Industry best practices
- Tooling improvements
- Project-specific needs

Regular review and updates ensure standards remain relevant and useful.

---

*Last Updated: [Current Date]*
*Next Review: [Quarterly]*

