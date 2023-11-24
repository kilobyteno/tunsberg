""" Common utilities for the package """
import re


def format_version_tag(name: str) -> str:
    """
    Format version tag that is used by setuptools-git-versioning

    :param name:
    :type name: str
    :return: Correctly formatted tag name
    :rtype: str
    :raises ValueError: If tag name is not formatted correctly
    """
    pattern = re.compile(r'^\d+\.\d+\.\d+$')
    match = pattern.search(name)

    # Check if the tag name is formatted correctly
    if match:
        return name

    # If the tag name is not formatted correctly, raise an error
    raise ValueError(f'Wrong tag name: {name}')
