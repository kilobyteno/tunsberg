import logging
from os import getenv


def uvicorn_log_config(
    log_level: int = logging.DEBUG, log_file_path: str = 'uvicorn.log', log_format: str = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
) -> dict:
    """
    Generate a configuration dictionary for Uvicorn logging.

    :param log_level: Log level integer
    :type log_level: int
    :param log_file_path: Path to the log file
    :type log_file_path: str
    :param log_format: Log format string
    :type log_format: str
    :return: Configuration dictionary
    :rtype: dict
    """
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
    :raises Exception: If any required environment variable is not set
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
