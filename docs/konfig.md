# Konfig

Helpers for logging configuration and required environment variable checks.

## Logging

Use `log_config` to build a `logging.config.dictConfig`-compatible dictionary for Uvicorn/FastAPI:

```python
import logging
from logging.config import dictConfig

from tunsberg.konfig import log_config

dictConfig(
    log_config(
        log_level=logging.INFO,
        log_file_path='app.log',
        log_formatter='json',  # or "default"
        log_handlers=['time_rotating_file', 'console'],
    )
)
```

Available handlers: `file`, `console`, `rotating_file`, `time_rotating_file`.

`uvicorn_log_config` is deprecated; use `log_config` instead.

## Required environment variables

```python
from tunsberg.konfig import check_required_env_vars

check_required_env_vars(
    required_env_vars={
        'ENV': {'runtime': True, 'build': True},
        'JWT_PUBLIC_KEY': {'runtime': True, 'build': False},
    },
    env='production',
    live_envs=['production', 'prod', 'staging'],
)
```

Raises `ValueError` when a required variable is missing for the current runtime or build context.
