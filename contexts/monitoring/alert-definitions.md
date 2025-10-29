# Alert Definitions

## Overview

This document defines alert definitions, thresholds, and routing for production monitoring.

## Alert Severity

### Critical

- **Impact**: Service down, data loss, security breach
- **Response**: Immediate, 24/7
- **Notification**: All stakeholders, on-call engineer
- **Auto-remediation**: Attempt automatic recovery

### High

- **Impact**: Major degradation, significant errors
- **Response**: Within 15 minutes
- **Notification**: On-call engineer, team lead
- **Investigation**: Required within SLA

### Medium

- **Impact**: Minor issues, performance degradation
- **Response**: Within 1 hour
- **Notification**: On-call engineer
- **Investigation**: Next business day

### Low

- **Impact**: Informational, minor issues
- **Response**: Next business day
- **Notification**: Ticket system
- **Investigation**: As time permits

## Alert Categories

### Availability Alerts

#### Service Down

- **Metric**: Health check failures
- **Threshold**: 3 consecutive failures
- **Severity**: Critical
- **Action**: Auto-scale, failover, page on-call

#### High Error Rate

- **Metric**: Error rate percentage
- **Threshold**: > 5% errors for 5 minutes
- **Severity**: High
- **Action**: Investigate errors, check recent deployments

### Performance Alerts

#### High Latency

- **Metric**: P95 response time
- **Threshold**: > 2x baseline for 5 minutes
- **Severity**: High
- **Action**: Investigate performance, check resources

#### Resource Exhaustion

- **Metric**: CPU/Memory usage
- **Threshold**: > 90% for 5 minutes
- **Severity**: High
- **Action**: Scale up, investigate resource usage

### Error Alerts

#### Exception Rate

- **Metric**: Exception count
- **Threshold**: > 10 exceptions/minute
- **Severity**: Medium
- **Action**: Review error logs, identify root cause

#### Database Errors

- **Metric**: Database error rate
- **Threshold**: > 1% database errors
- **Severity**: High
- **Action**: Check database health, connection pool

## Alert Routing

### On-Call Rotation

- **Primary**: On-call engineer
- **Secondary**: Backup on-call engineer
- **Escalation**: Team lead if no response
- **Rotation**: Weekly rotation

### Notification Channels

- **Critical**: Phone call + SMS + Slack + Email
- **High**: SMS + Slack + Email
- **Medium**: Slack + Email
- **Low**: Email only

## Alert Examples

### Service Health Check Failure

```yaml
alert: ServiceHealthCheckFailure
condition: health_check_failures > 3
severity: Critical
notification:
  - oncall_engineer
  - team_lead
  - status_page
action:
  - auto_scale_up
  - failover_if_available
```

### High Error Rate

```yaml
alert: HighErrorRate
condition: error_rate > 5% for 5 minutes
severity: High
notification:
  - oncall_engineer
action:
  - check_recent_deployments
  - review_error_logs
```

### High Latency

```yaml
alert: HighLatency
condition: p95_latency > 2x_baseline for 5 minutes
severity: High
notification:
  - oncall_engineer
action:
  - check_resource_usage
  - review_slow_queries
```

## Alert Tuning

### Reducing Noise

- **Threshold adjustment**: Increase thresholds to reduce false positives
- **Grouping**: Group related alerts
- **Suppression**: Suppress expected alerts (maintenance windows)
- **Filtering**: Filter out known issues

### Increasing Sensitivity

- **Lower thresholds**: For critical services
- **Faster detection**: Reduce time windows
- **More channels**: Additional notification channels

## References

- Logging Standards: `contexts/monitoring/logging-standards.md`
- Incident Response: `contexts/devops/incident-response.md`

