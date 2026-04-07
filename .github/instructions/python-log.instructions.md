---
applyTo: '**/*.py'
---

# Logging Standards

When generating or modifying Python code, always include appropriate logging:

## Python Code
- Import logging at the top: `import logging`
- Add logger instance: `logger = logging.getLogger(__name__)`
- Add log statements:
  - `logger.info()` for successful operations and business events
  - `logger.debug()` for detailed debugging information
  - `logger.warning()` for recoverable issues
  - `logger.error()` for errors with `exc_info=True`
- Log statements:
  - Use structured logging where possible (e.g., `logger.info("User created", extra={"user_id": user.id})`)
  - Avoid logging sensitive information (e.g., passwords, personal data)
  - Use lazy formatting (e.g., `logger.info("Processing account %s", account_id)`) to avoid unnecessary string interpolation when the log level is not enabled.

## Function/Method Logging Pattern
```python
def function_name(params):
    logger.info("Operation started: %s", description)
    try:
        # operation logic
        logger.debug("Details: %s", relevant_data)
        logger.info("Operation completed successfully")
        return result
    except Exception as e:
        logger.error("Operation failed: %s", e, exc_info=True)
        raise
```

## Service Layer
- Log entry points with parameters (excluding sensitive data)
- Log successful completion
- Log errors with context

## Repository Layer
- Use DEBUG level for database operations
- Log query parameters (sanitized)

## API Routes
- INFO level for endpoint access
- Include relevant identifiers (account_id, etc.)