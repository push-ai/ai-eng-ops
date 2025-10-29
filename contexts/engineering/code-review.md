# Code Review Guidelines

## Overview

This document defines standards and best practices for code reviews, ensuring code quality and knowledge sharing.

## Review Principles

### 1. Code Review is a Learning Opportunity

- **Share knowledge**: Explain patterns and decisions
- **Teach**: Help reviewers learn
- **Learn**: Be open to feedback
- **Improve**: Use feedback to improve

### 2. Be Constructive

- **Respectful**: Criticize code, not people
- **Specific**: Provide specific, actionable feedback
- **Helpful**: Suggest improvements, not just problems
- **Positive**: Acknowledge good work

### 3. Focus on What Matters

- **Functionality**: Does it work correctly?
- **Design**: Is the design sound?
- **Standards**: Does it follow standards?
- **Tests**: Are tests adequate?

## Review Checklist

### Functionality

- [ ] Code solves the stated problem
- [ ] Edge cases handled
- [ ] Error handling implemented
- [ ] Performance acceptable

### Code Quality

- [ ] Follows style guide
- [ ] Uses type hints/interfaces
- [ ] Documented appropriately
- [ ] No obvious bugs

### Testing

- [ ] Tests added/updated
- [ ] Tests cover edge cases
- [ ] Tests are maintainable
- [ ] Coverage meets threshold

### Security

- [ ] No security vulnerabilities
- [ ] Input validation present
- [ ] Authentication/authorization correct
- [ ] Secrets not hardcoded

## Review Process

### For Authors

1. **Self-review**: Review your own code first
2. **Run tests**: Ensure all tests pass
3. **Update documentation**: Update docs if needed
4. **Request review**: Request review from appropriate reviewers
5. **Respond to feedback**: Address all comments
6. **Thank reviewers**: Acknowledge reviewers' time

### For Reviewers

1. **Review promptly**: Review within 24 hours
2. **Be thorough**: Check checklist items
3. **Provide feedback**: Specific, actionable feedback
4. **Approve when ready**: Don't block unnecessarily
5. **Learn**: Use reviews to learn codebase

## Review Comments

### Good Review Comments

```python
# ❌ Good: Specific, actionable
# This function could use input validation. The `amount` parameter 
# should be checked for negative values, as negative amounts don't 
# make sense for payments. Consider adding:
#   if amount < 0:
#       raise ValueError("Amount must be positive")

# ✅ Good: Acknowledges good work
# Great use of type hints here! The TypedDict makes the return 
# structure very clear.
```

### Bad Review Comments

```python
# ❌ Bad: Vague
# This doesn't look right

# ❌ Bad: Not constructive
# This is wrong

# ❌ Bad: Personal attack
# You should know better than this
```

## Common Review Patterns

### Request Changes When

- Code has bugs or won't work
- Security vulnerabilities present
- Standards not followed
- Tests missing or inadequate
- Performance issues

### Suggest Improvements When

- Code works but could be better
- Better patterns available
- Optimization opportunities
- Documentation could be clearer

### Approve When

- Code works correctly
- Standards followed
- Tests adequate
- Documentation updated
- No blocking issues

## Review Timing

### Response Times

- **P0/P1 issues**: Review within 2 hours
- **Normal PRs**: Review within 24 hours
- **Large PRs**: Review within 48 hours
- **Complex PRs**: Schedule review meeting if needed

### PR Size Guidelines

- **Small PRs**: < 200 lines, easy to review
- **Medium PRs**: 200-500 lines, manageable
- **Large PRs**: 500-1000 lines, consider splitting
- **Very Large PRs**: > 1000 lines, should be split

## Collaboration

### Discussion

- **Use comments**: Discuss in PR comments
- **Be respectful**: Maintain professional tone
- **Seek clarification**: Ask questions if unclear
- **Reach consensus**: Work together on solutions

### Conflict Resolution

- **Data-driven**: Use data/metrics to support points
- **Compromise**: Find middle ground when possible
- **Escalate**: Involve tech lead if needed
- **Learn**: Use conflicts as learning opportunities

## References

- Development Workflow: `contexts/engineering/development-workflow.md`
- Code Quality Standards: `contexts/standards/code-quality.md`

