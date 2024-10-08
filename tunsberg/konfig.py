import logging


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
