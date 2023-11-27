import re

from flask import request


def get_api_version(folder_name: str, pattern: str = r'v\d+(_\d+)?', default: str = '') -> str:
    r"""
    Get API version from folder name.

    :param folder_name: Folder name
    :type folder_name: str
    :param pattern: Regular expression pattern to match version. Default is 'v\\d+(_\\d+)?',
                    which matches 'v<number>' or 'v<number>_<number>'.
    :type pattern: str
    :param default: Default return value if no version is found. Defaults to ''.
    :type default: str
    :return: API version as string, or the default value if no version is found
    :rtype: str
    """
    if folder_name == 'app.api':
        return default

    version_parts = folder_name.split('.')
    version_regex = re.compile(pattern)

    for part in version_parts:
        if version_regex.match(part):
            return part

    return default


def get_api_version_from_flask_url(pattern: str = r'v\d+(_\d+)?', default: str = '') -> str:
    r"""
    Get the API version from a Flask URL.

    :param pattern: Regular expression pattern to match version. Default is 'v\\d+(_\\d+)?',
                    which matches 'v<number>' or 'v<number>_<number>'.
    :type pattern: str
    :param default: Default return value if no version is found. Defaults to ''.
    :type default: str
    :return: API version as string, or the default value if no version is found
    :rtype: str
    """
    url_list = request.url.split('/')
    version_regex = re.compile(pattern)

    for item in url_list:
        if version_regex.match(item):
            return item

    return default
