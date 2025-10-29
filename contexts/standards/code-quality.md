# Code Quality Standards

## Overview

This document defines code quality standards for our engineering team. All code must meet these standards before being merged.

## Quality Metrics

### Test Coverage

- **Minimum coverage**: 80% for new code
- **Maintain or improve**: Existing code coverage should not decrease
- **Critical paths**: 100% coverage for authentication, payment, and data access
- **Unit tests**: Required for all public APIs and business logic
- **Integration tests**: Required for API endpoints and database operations

### Code Complexity

- **Cyclomatic complexity**: Maximum 10 per function/method
- **Function length**: Maximum 50 lines
- **Class size**: Maximum 500 lines
- **File size**: Maximum 1000 lines

### Performance Standards

- **API response time**: P95 < 200ms for standard endpoints
- **Database queries**: Maximum 100ms for standard queries
- **Page load time**: P95 < 2s for web pages
- **Memory usage**: Monitor and alert on memory leaks

### Documentation Requirements

- **Public APIs**: All endpoints must have OpenAPI/Swagger documentation
- **Complex functions**: Docstrings with parameters, returns, and examples
- **Architecture decisions**: Documented in ADRs (Architecture Decision Records)
- **Business logic**: Inline comments explaining "why" not "what"

## Code Review Checklist

All code reviews must verify:

- [ ] Code meets minimum test coverage
- [ ] Code complexity within limits
- [ ] Performance benchmarks met
- [ ] Documentation updated
- [ ] Follows style guide
- [ ] No security vulnerabilities
- [ ] Error handling implemented
- [ ] Logging added where appropriate

## Quality Gates

### Pre-Merge Requirements

1. **Tests passing**: All tests must pass
2. **Coverage met**: Minimum coverage thresholds met
3. **Linting passed**: All linting rules pass
4. **Security scan**: No high/critical vulnerabilities
5. **Performance tests**: Performance benchmarks met

### CI/CD Integration

- Automated quality checks run on every PR
- PRs cannot be merged until quality gates pass
- Quality metrics reported in PR comments
- Coverage reports generated automatically

## Enforcement

### Automated Checks

- **Linters**: ESLint, Pylint, etc. configured in CI/CD
- **Formatters**: Prettier, Black, etc. auto-format on commit
- **Tests**: Automated test suite runs on every commit
- **Security**: Automated security scanning (Snyk, Dependabot)

### Manual Review

- **Code review**: Human review focuses on logic, architecture, and patterns
- **Quality review**: Dedicated quality review for large changes
- **Performance review**: Performance testing for critical paths

## Examples

### Good: Meets Quality Standards

```python
def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate price after discount.
    
    Args:
        price: Original price (must be >= 0)
        discount_percent: Discount percentage (0-100)
    
    Returns:
        Final price after discount
    
    Raises:
        ValueError: If price < 0 or discount_percent not in [0, 100]
    
    Example:
        >>> calculate_discount(100.0, 10.0)
        90.0
    """
    if price < 0:
        raise ValueError("Price must be >= 0")
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be between 0 and 100")
    
    return price * (1 - discount_percent / 100)
```

**Quality**: ✅ Documented, validated, typed, simple

### Bad: Fails Quality Standards

```python
def calc(p, d):
    return p - (p * d / 100)
```

**Issues**: ❌ No documentation, no validation, no types, unclear naming

## Tools and Configuration

### Linting

- **Python**: pylint, mypy configured in `.pylintrc` and `pyproject.toml`
- **TypeScript**: ESLint configured in `.eslintrc.json`
- **Git hooks**: Pre-commit hooks run linters before commit

### Testing

- **Framework**: pytest for Python, Jest for TypeScript
- **Coverage**: pytest-cov, jest-coverage configured
- **Reports**: Coverage reports published to CI/CD

### Security

- **Dependency scanning**: Dependabot, Snyk
- **SAST**: CodeQL, Semgrep
- **Secret scanning**: GitHub secret scanning, git-secrets

## Exceptions

Exceptions to quality standards require:

- **Justification**: Clear reason why exception is needed
- **Approval**: Team lead or tech lead approval
- **Documentation**: Exception documented in code comments
- **Plan**: Plan to address exception in future

## References

- Style Guide: `contexts/standards/style-guide.md`
- Testing Standards: `contexts/engineering/testing.md`
- Security Requirements: `contexts/security/coding-practices.md`

