import json
import logging
import warnings
from datetime import datetime, timezone
from os import getenv


class JsonFormatter(logging.Formatter):
    """Custom JSON log formatter"""

    def format(self, record):
        """Format log record as JSON"""
        log_record = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'module': record.module,
            'line': record.lineno,
            'message': record.getMessage(),
        }

        # Add exception info if available
        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)

        return json.dumps(log_record)


def log_config(  # noqa: PLR0913
    log_level: int = logging.DEBUG,
    log_file_path: str = 'fastapi.log',
    log_format: str = '%(asctime)s - [%(levelname)s] %(name)s: %(message)s',
    log_handlers=None,
    log_formatter: str = 'default',
    date_format: str = '%Y-%m-%d %H:%M:%S',
) -> dict:
    """
    Generate a configuration dictionary for logging in FastAPI with Uvicorn.

    :param log_level: Log level integer, defaults to logging.DEBUG
    :type log_level: int
    :param log_file_path: Path to the log file, defaults to 'fastapi.log'
    :type log_file_path: str
    :param log_format: Log format string, defaults to '%(asctime)s - [%(levelname)s] %(name)s: %(message)s'
    :type log_format: str
    :param log_handlers: List of log handlers, defaults to ['time_rotating_file', 'console']
    :type log_handlers: list
    :param log_formatter: Log formatter name, defaults to 'default'
    :type log_formatter: str
    :param date_format: Date format string, defaults to '%Y-%m-%d %H:%M:%S'
    :type date_format: str
    :return: Configuration dictionary
    :rtype: dict
    """
    # Default to both time_rotating_file and console handlers if none are provided
    if log_handlers is None:
        log_handlers = ['time_rotating_file', 'console']

    # Make sure the log level is valid
    if logging.getLevelName(log_level) is None or logging.getLevelName(log_level).__contains__('Level'):
        raise ValueError('Invalid log level')

    # Make sure log format is not empty
    if not log_format:
        raise ValueError('Log format cannot be empty')

    # Make sure log file path is not empty
    if not log_file_path:
        raise ValueError('Log file path cannot be empty')

    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': log_format,
                'datefmt': date_format,
            },
            'json': {
                '()': JsonFormatter,
            },
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'filename': log_file_path,
                'formatter': log_formatter,
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': log_formatter,
            },
            'rotating_file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': log_formatter,
                'filename': log_file_path,
                'maxBytes': 10485760,  # 10 MB
                'backupCount': 5,
            },
            'time_rotating_file': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': log_formatter,
                'filename': log_file_path,
                'when': 'midnight',
                'interval': 1,
                'backupCount': 7,
            },
        },
        'loggers': {
            'uvicorn': {
                'handlers': log_handlers,
                'level': logging.getLevelName(log_level),
                'propagate': False,
            },
            'uvicorn.error': {
                'handlers': log_handlers,
                'level': logging.getLevelName(log_level),
                'propagate': False,
            },
            'uvicorn.access': {
                'handlers': log_handlers,
                'level': logging.getLevelName(log_level),
                'propagate': False,
            },
        },
        'root': {'handlers': ['console'], 'level': 'DEBUG'},
    }


def uvicorn_log_config(
    log_level: int = logging.DEBUG, log_file_path: str = 'uvicorn.log', log_format: str = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
) -> dict:
    """
    Generate a configuration dictionary for Uvicorn logging.

    DEPRECATED: Use log_config() instead.

    :param log_level: Log level integer
    :type log_level: int
    :param log_file_path: Path to the log file
    :type log_file_path: str
    :param log_format: Log format string
    :type log_format: str
    :return: Configuration dictionary
    :rtype: dict
    """
    warnings.deprecated('uvicorn_log_config is deprecated, use log_config instead', DeprecationWarning, stacklevel=2)

    # Make sure the log level is valid
    if logging.getLevelName(log_level) is None or logging.getLevelName(log_level).__contains__('Level'):
        raise ValueError('Invalid log level')

    # Make sure log format is not empty
    if not log_format:
        raise ValueError('Log format cannot be empty')

    # Make sure log file path is not empty
    if not log_file_path:
        raise ValueError('Log file path cannot be empty')

    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': log_format,
            },
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'filename': log_file_path,
                'formatter': 'default',
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
            },
        },
        'loggers': {
            'uvicorn': {
                'handlers': ['file', 'console'],
                'level': logging.getLevelName(log_level),
                'propagate': False,
            },
            'uvicorn.error': {
                'handlers': ['file', 'console'],
                'level': logging.getLevelName(log_level),
                'propagate': False,
            },
            'uvicorn.access': {
                'handlers': ['file', 'console'],
                'level': logging.getLevelName(log_level),
                'propagate': False,
            },
        },
    }


def check_required_env_vars(required_env_vars: dict, env: str, live_envs: [] or None = None, code_build: bool = False) -> bool or None:
    """
    Check if all required environment variables are set based on the current environment and if the code is being built.

    Example for required_env_vars:
        {'ENV': {'runtime': True, 'build': True},'JWT_PUBLIC_KEY': {'runtime': True, 'build': False}}

    Example for env:
        'production'

    Example for live_envs:
        ['production', 'prod', 'staging']

    :param required_env_vars: Required environment variables
    :type required_env_vars: dict
    :param env: Current environment
    :type env: str
    :param live_envs: List of live environments
    :type live_envs: [] or None
    :param code_build: Whether the code is being built
    :type code_build: bool
    :return: True if all required environment variables are set
    :rtype: bool or None
    :raises ValueError: If any required environment variable is not set
    """
    if live_envs is None:
        live_envs = ['production', 'prod']

    is_runtime = env in live_envs and not code_build
    is_code_build = code_build

    # Select environment variables based on current environment (production or build)
    req_env_vars = [
        env_var for env_var, conditions in required_env_vars.items() if (conditions['runtime'] and is_runtime) or (conditions['build'] and is_code_build)
    ]

    # Validate if all required environment variables are set
    missing_vars = [env_var for env_var in req_env_vars if getenv(env_var) is None]

    if missing_vars:
        missing_vars_str = ', '.join(missing_vars)
        raise ValueError(f'Environment Config Error: The following variables are not set: {missing_vars_str}')

    return True
