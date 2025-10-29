# Terraform Standards

## Overview

This document defines standards for Terraform infrastructure-as-code, ensuring consistency and maintainability.

## File Organization

### Directory Structure

```
infrastructure/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   └── production/
├── modules/
│   ├── ecs-service/
│   ├── rds-instance/
│   └── vpc/
└── shared/
    └── common-resources/
```

### Module Structure

```
module-name/
├── main.tf           # Main resources
├── variables.tf      # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider versions
└── README.md        # Module documentation
```

## Naming Conventions

### Resources

- **Format**: `{resource_type}_{environment}_{purpose}`
- **Lowercase**: Use lowercase and hyphens
- **Descriptive**: Clear purpose from name

```hcl
# Good
resource "aws_ecs_service" "production_api_service" {
  name = "api-service"
}

# Bad
resource "aws_ecs_service" "service1" {
  name = "s1"
}
```

### Variables

- **Descriptive names**: Clear purpose
- **Consistent format**: snake_case

```hcl
# Good
variable "database_instance_type" {
  description = "RDS instance type"
  type        = string
  default     = "db.t3.medium"
}

# Bad
variable "db_type" {
  type = string
}
```

## Module Design

### Module Principles

- **Single responsibility**: One module, one purpose
- **Reusable**: Parameterized for reuse
- **Documented**: Clear README with examples
- **Versioned**: Tag modules for versioning

### Module Example

```hcl
# modules/ecs-service/main.tf
resource "aws_ecs_service" "service" {
  name            = var.service_name
  cluster         = var.cluster_id
  task_definition = aws_ecs_task_definition.task.arn
  desired_count   = var.desired_count
  
  network_configuration {
    subnets         = var.subnet_ids
    security_groups = var.security_group_ids
  }
}

# modules/ecs-service/variables.tf
variable "service_name" {
  description = "Name of the ECS service"
  type        = string
}

variable "cluster_id" {
  description = "ECS cluster ID"
  type        = string
}

# modules/ecs-service/outputs.tf
output "service_id" {
  description = "ECS service ID"
  value       = aws_ecs_service.service.id
}
```

## State Management

### Remote State

- **Backend**: S3 with DynamoDB locking
- **State files**: Separate state per environment
- **Locking**: DynamoDB table for state locking
- **Encryption**: Encrypt state files

### State Configuration

```hcl
terraform {
  backend "s3" {
    bucket         = "terraform-state-bucket"
    key            = "environments/production/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}
```

## Best Practices

### Resource Organization

- **Group related resources**: Group by service/component
- **Use modules**: Reuse common patterns
- **Separate environments**: Different directories/files
- **Version providers**: Pin provider versions

### Variable Management

- **Use variables**: Parameterize all configurable values
- **Default values**: Provide sensible defaults
- **Validation**: Validate variable values
- **Descriptions**: Document all variables

### Output Management

- **Output values**: Output important resource attributes
- **Documentation**: Document all outputs
- **Sensitive data**: Mark sensitive outputs

## Security

### Secrets Management

- **Never commit secrets**: Use secrets management (AWS Secrets Manager, etc.)
- **Reference secrets**: Reference secrets in Terraform
- **Rotate secrets**: Regular secret rotation

### IAM Permissions

- **Least privilege**: Minimum required permissions
- **Use roles**: Assume roles, don't store credentials
- **Review permissions**: Review IAM policies regularly

## Testing

### Validation

- **terraform validate**: Run before apply
- **terraform plan**: Review plan before apply
- **terraform fmt**: Format code consistently

### CI/CD Integration

- **Validate on PR**: Run terraform validate
- **Plan on PR**: Generate plan for review
- **Apply on merge**: Auto-apply to dev environment
- **Manual approval**: Require approval for production

## References

- Cloud Patterns: `contexts/infrastructure/cloud-patterns.md`
- DevOps: `contexts/devops/infrastructure-patterns.md`

