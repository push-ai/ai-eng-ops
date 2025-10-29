# Infrastructure Patterns

## Overview

This document defines infrastructure patterns used across our systems, ensuring consistency and reliability.

## Cloud Architecture

### Multi-AZ Deployment

- **Availability Zones**: Deploy across at least 2 AZs
- **Load balancing**: Distribute traffic across AZs
- **Data replication**: Replicate data across AZs
- **Failover**: Automatic failover between AZs

### Auto-Scaling

- **Horizontal scaling**: Add/remove instances
- **Vertical scaling**: Resize instances (limited)
- **Scaling triggers**: CPU, memory, request rate
- **Scaling policies**: Target 70% CPU utilization

### Load Balancing

- **Application Load Balancer**: For HTTP/HTTPS traffic
- **Network Load Balancer**: For TCP/UDP traffic
- **Health checks**: Every 30 seconds
- **Sticky sessions**: Use only when necessary

## Container Patterns

### Container Best Practices

- **Base images**: Use official, minimal base images
- **Image size**: Keep images small (< 500MB when possible)
- **Layer caching**: Order Dockerfile for cache efficiency
- **Security**: Scan images for vulnerabilities

### Container Orchestration

- **Kubernetes**: Primary orchestration platform
- **Deployments**: Use Deployments for stateless services
- **StatefulSets**: Use StatefulSets for stateful services
- **Services**: Use Services for service discovery

## Database Patterns

### High Availability

- **Primary-replica**: Primary + at least 1 replica
- **Automatic failover**: Promote replica on primary failure
- **Connection pooling**: Use connection pools
- **Read replicas**: Use for read-heavy workloads

### Backup Strategy

- **Daily backups**: Full backup daily
- **Transaction logs**: Continuous transaction log backup
- **Retention**: 30 days for daily, 7 days for transaction logs
- **Testing**: Test restore monthly

## Monitoring and Logging

### Metrics Collection

- **Prometheus**: Metrics collection
- **Grafana**: Metrics visualization
- **Custom metrics**: Business metrics
- **Retention**: 90 days for metrics

### Log Aggregation

- **Centralized logging**: All logs to central system
- **Structured logs**: JSON format
- **Log levels**: DEBUG, INFO, WARN, ERROR
- **Retention**: 30 days for application logs

## Security Patterns

### Network Security

- **VPC**: Isolated network per environment
- **Security groups**: Least privilege access
- **WAF**: Web Application Firewall for public APIs
- **DDoS protection**: Cloud provider DDoS protection

### Access Control

- **IAM**: Role-based access control
- **Least privilege**: Minimum required permissions
- **Audit logging**: Log all access
- **Rotation**: Rotate credentials regularly

## Cost Optimization

### Resource Right-Sizing

- **Monitor usage**: Track resource utilization
- **Right-size**: Match resources to actual usage
- **Reserved instances**: Use for predictable workloads
- **Spot instances**: Use for fault-tolerant workloads

### Resource Cleanup

- **Automated cleanup**: Remove unused resources
- **Lifecycle policies**: Auto-delete old resources
- **Cost alerts**: Alert on cost anomalies
- **Cost review**: Monthly cost review

## Disaster Recovery

### Backup Strategy

- **RTO**: Recovery Time Objective: 4 hours
- **RPO**: Recovery Point Objective: 1 hour
- **Backup locations**: Multiple geographic regions
- **Testing**: Test DR procedures quarterly

### Failover Procedures

- **Automated failover**: Where possible
- **Manual failover**: Documented procedures
- **Failover testing**: Test quarterly
- **Communication**: Notify stakeholders during failover

## References

- Incident Response: `contexts/devops/incident-response.md`
- Infrastructure Standards: `contexts/infrastructure/cloud-patterns.md`

