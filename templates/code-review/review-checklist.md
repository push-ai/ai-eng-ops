# Code Review Checklist

Use this checklist to ensure thorough code reviews. Check each item systematically.

## Pre-Review

- [ ] Read PR description
- [ ] Understand context and requirements
- [ ] Check linked issues
- [ ] Review related code/files if needed

## Functionality

- [ ] Code solves the stated problem
- [ ] Edge cases are handled
- [ ] Error handling is implemented
- [ ] Input validation is present
- [ ] Performance is acceptable
- [ ] No obvious bugs

## Code Quality

### Style and Formatting
- [ ] Follows style guide
- [ ] Consistent formatting
- [ ] Proper indentation
- [ ] No commented-out code

### Type Safety
- [ ] Type hints/interfaces used (Python/TypeScript)
- [ ] Types are correct
- [ ] No `any` types (TypeScript)
- [ ] Proper type constraints

### Code Structure
- [ ] Functions are focused and single-purpose
- [ ] Code is well-organized
- [ ] No code duplication
- [ ] Appropriate abstractions

## Testing

- [ ] Tests added/updated
- [ ] Tests cover new functionality
- [ ] Tests cover edge cases
- [ ] Tests are maintainable
- [ ] Test coverage meets threshold
- [ ] Integration tests updated (if applicable)
- [ ] Manual testing completed (if applicable)

## Security

- [ ] No security vulnerabilities
- [ ] Input validation present
- [ ] Authentication/authorization correct
- [ ] Secrets not hardcoded
- [ ] SQL injection prevented
- [ ] XSS prevented
- [ ] CSRF protection (if applicable)
- [ ] Rate limiting (if applicable)

## Performance

- [ ] No performance regressions
- [ ] Database queries optimized
- [ ] No N+1 queries
- [ ] Caching used appropriately
- [ ] Async operations handled correctly

## Documentation

- [ ] Code comments/documentation added
- [ ] Docstrings complete (if applicable)
- [ ] README updated (if applicable)
- [ ] API documentation updated (if applicable)
- [ ] Architecture docs updated (if applicable)
- [ ] Changelog updated (if applicable)

## Architecture

- [ ] Design is sound
- [ ] Follows established patterns
- [ ] No anti-patterns
- [ ] Maintainable structure
- [ ] Scalable design

## Dependencies

- [ ] Dependencies are necessary
- [ ] Dependency versions are pinned
- [ ] No security vulnerabilities in dependencies
- [ ] Dependencies are up to date (or updates justified)

## Breaking Changes

- [ ] Breaking changes documented
- [ ] Migration guide provided (if needed)
- [ ] Version bumped appropriately
- [ ] Stakeholders notified (if needed)

## CI/CD

- [ ] All CI checks passing
- [ ] Build succeeds
- [ ] Tests pass
- [ ] Linting passes
- [ ] Security scans pass

## Accessibility (if applicable)

- [ ] Accessibility standards met
- [ ] Keyboard navigation works
- [ ] Screen reader compatible
- [ ] ARIA labels present

## Browser/Platform Compatibility (if applicable)

- [ ] Works on supported browsers
- [ ] Mobile responsive (if applicable)
- [ ] Cross-platform compatible (if applicable)

## Final Review

- [ ] All critical issues addressed
- [ ] Suggestions considered
- [ ] Code is ready to merge
- [ ] PR can be approved

---

**Reviewer Notes**: [Any additional notes or concerns]

