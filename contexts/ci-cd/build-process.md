# Build Process

## Overview

This document defines the build process for all services, including dependency management, build steps, and artifact creation.

## Build Tools

### Python Services

- **Package manager**: pip with requirements.txt or Poetry
- **Build tool**: setuptools or Poetry
- **Virtual environment**: venv or Poetry
- **Artifact**: Docker image or wheel package

### TypeScript/Node Services

- **Package manager**: npm or yarn
- **Build tool**: TypeScript compiler, webpack, or esbuild
- **Artifact**: Docker image or npm package

## Build Configuration

### Python Build

```dockerfile
# Dockerfile example
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Run application
CMD ["python", "main.py"]
```

### TypeScript Build

```dockerfile
# Dockerfile example
FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Build application
COPY . .
RUN npm run build

# Run application
CMD ["node", "dist/main.js"]
```

## Build Steps

### 1. Dependency Installation

```bash
# Python
pip install -r requirements.txt

# Node
npm ci
```

### 2. Code Quality Checks

```bash
# Linting
npm run lint
pylint src/

# Type checking
npm run type-check
mypy src/
```

### 3. Testing

```bash
# Run tests
npm test
pytest

# Coverage
npm run test:coverage
pytest --cov
```

### 4. Building

```bash
# Python (if building package)
python setup.py sdist bdist_wheel

# TypeScript
npm run build
```

### 5. Artifact Creation

```bash
# Docker image
docker build -t service-name:version .

# Package (if applicable)
npm pack
python setup.py sdist
```

## Build Optimization

### Caching

- **Dependencies**: Cache dependency installation
- **Build artifacts**: Cache build outputs
- **Docker layers**: Optimize Docker layer caching

### Parallelization

- **Test parallelization**: Run tests in parallel
- **Build parallelization**: Build modules in parallel
- **CI/CD parallelization**: Run checks in parallel

## Build Environment

### Required Tools

- **Docker**: For container builds
- **Language runtime**: Python 3.11+, Node 18+
- **Build tools**: pip, npm, etc.
- **CI/CD platform**: GitHub Actions, GitLab CI, etc.

### Environment Variables

- **Build-time**: Configure build behavior
- **Runtime**: Configure application (not in image)
- **Secrets**: Never in image, use secrets management

## Build Artifacts

### Docker Images

- **Tagging**: `service-name:version` and `service-name:latest`
- **Registry**: Push to container registry
- **Scanning**: Security scan before deployment

### Packages

- **Versioning**: Semantic versioning (semver)
- **Distribution**: Package registry (npm, PyPI)
- **Metadata**: Include version, dependencies, etc.

## Build Verification

### Pre-Build Checks

- [ ] Dependencies up to date
- [ ] Security vulnerabilities scanned
- [ ] Build configuration valid

### Post-Build Checks

- [ ] Artifact created successfully
- [ ] Artifact size reasonable
- [ ] Artifact security scanned
- [ ] Artifact tagged correctly

## Build Failures

### Common Issues

- **Dependency conflicts**: Resolve version conflicts
- **Build errors**: Fix compilation errors
- **Test failures**: Fix failing tests
- **Timeout**: Optimize build or increase timeout

### Debugging

- **Build logs**: Review build logs for errors
- **Local build**: Reproduce locally
- **Incremental build**: Build step by step
- **Cache clearing**: Clear caches if needed

## References

- Deployment Workflow: `contexts/ci-cd/deployment-workflow.md`
- Infrastructure: `contexts/infrastructure/containers.md`

