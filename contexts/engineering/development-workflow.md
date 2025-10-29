# Development Workflow

## Overview

This document defines the standard development workflow for feature development, bug fixes, and releases.

## Feature Development Process

### 1. Planning

- **Create issue**: Document feature requirements
- **Design review**: Review design if complex
- **Break down**: Break into smaller tasks
- **Estimate**: Estimate effort

### 2. Development

- **Create branch**: `feature/feature-name` or `feat/feature-name`
- **Implement**: Write code following standards
- **Test**: Write tests as you develop
- **Document**: Update documentation

### 3. Review

- **Self-review**: Review your own code
- **Request review**: Request review from teammates
- **Address feedback**: Respond to all comments
- **Iterate**: Make improvements based on feedback

### 4. Merge

- **All checks pass**: CI/CD checks passing
- **Approved**: At least one approval
- **Updated**: Code up to date with main
- **Merge**: Merge to main

### 5. Deploy

- **Automatic**: Deploy to staging automatically
- **Verify**: Verify in staging
- **Production**: Deploy to production after approval

## Bug Fix Process

### 1. Triage

- **Reproduce**: Reproduce the bug
- **Identify**: Identify root cause
- **Prioritize**: Assign priority (P0-P3)
- **Create issue**: Document bug

### 2. Fix

- **Create branch**: `bugfix/bug-description` or `fix/bug-description`
- **Write test**: Write failing test first (TDD)
- **Fix bug**: Implement fix
- **Verify**: Test passes, bug fixed

### 3. Review and Deploy

- **Review**: Same as feature development
- **Hotfix**: Expedited process for P0 bugs
- **Deploy**: Deploy fix quickly for critical bugs

## Branch Naming

### Conventions

- **Features**: `feature/feature-name` or `feat/feature-name`
- **Bug fixes**: `bugfix/bug-description` or `fix/bug-description`
- **Hotfixes**: `hotfix/description`
- **Chores**: `chore/description`

### Examples

```
feature/user-authentication
feat/add-payment-processing
bugfix/fix-login-error
fix/correct-calculation
hotfix/security-patch
chore/update-dependencies
```

## Commit Messages

### Format

```
type(scope): subject

body (optional)

footer (optional)
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation
- **style**: Formatting
- **refactor**: Code refactoring
- **test**: Tests
- **chore**: Maintenance

### Examples

```
feat(auth): add user authentication

Implements JWT-based authentication with refresh tokens.
Adds login, logout, and token refresh endpoints.

Closes #123
```

## Pull Request Process

### PR Requirements

- **Description**: Clear description of changes
- **Linked issue**: Reference related issue
- **Tests**: Tests added/updated
- **Documentation**: Documentation updated
- **Checklist**: PR checklist completed

### PR Template

```markdown
## Description
Brief description of changes

## Related Issue
Closes #123

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
- [ ] Tests added/updated
- [ ] Manual testing completed
- [ ] All tests passing

## Checklist
- [ ] Code follows standards
- [ ] Documentation updated
- [ ] No breaking changes
```

## Code Review Process

See `code-review.md` for detailed code review guidelines.

## Deployment Process

See `contexts/ci-cd/deployment-workflow.md` for deployment procedures.

## References

- Code Review: `contexts/engineering/code-review.md`
- CI/CD: `contexts/ci-cd/deployment-workflow.md`

