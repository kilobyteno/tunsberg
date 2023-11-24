from typing import Union


def response_success(message: str = 'Resource(s) were successfully retrieved', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a resource is successfully retrieved.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Success',
        'message': message,
        'data': data
    }, 200


def response_created(message: str = 'Resource created successfully', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a resource is successfully created.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Created',
        'message': message,
        'data': data,
    }, 201


def response_no_content(message: str = 'Resource was successfully deleted') -> tuple:
    """
    Use this response when a resource is successfully deleted.

    :param message: Message to be returned.
    :type message: str
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'No Content',
        'message': message,
        'data': None,
    }, 204


def response_bad_request(message: str = 'Input validation failed', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a user has supplied invalid input.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Bad Request',
        'message': message,
        'data': data
    }, 400


def response_unauthorized(message: str = 'Missing or invalid credentials', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a user is not authorized to access a resource.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Unauthorized',
        'message': message,
        'data': data
    }, 401


def response_forbidden(message: str = 'User is not authorized to perform this action', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a user is not authorized to access a resource.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Forbidden',
        'message': message,
        'data': data
    }, 403


def response_not_found(message: str = 'Requested resource not found', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a requested resource is not found.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Not Found',
        'message': message,
        'data': data,
    }, 404


def response_method_not_allowed(message: str = 'This method is not allowed', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a user has supplied an invalid HTTP method for a resource.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Method Not Allowed',
        'message': message,
        'data': data
    }, 405


def response_conflict(message: str = 'Conflict with the current state of the target resource', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when there is a conflict with the current state of the target resource.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Conflict',
        'message': message,
        'data': data,
    }, 409


def response_gone(message: str = 'Resource no longer available', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a resource does not exist, i.e., no results found.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Gone',
        'message': message,
        'data': data
    }, 410


def response_payload_too_large(message: str = 'Payload exceeds the allowed limit', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a user has supplied too large of a payload, e.g., a file that is too large.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Payload Too Large',
        'message': message,
        'data': data
    }, 413


def response_unsupported_media_type(message: str = 'Unsupported media type', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a user has supplied invalid file input, e.g., a file that is not a .png.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Unsupported Media Type',
        'message': message,
        'data': data
    }, 415


def response_too_many_requests(message: str = 'Client has sent too many requests in a given amount of time', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a client has sent too many requests in a given amount of time.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Too Many Requests',
        'message': message,
        'data': data,
    }, 429


def response_error(message: str = 'An error occurred', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when an unexpected error occurs on the server.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :type data: dict or None
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Internal Server Error',
        'message': message,
        'data': data,
    }, 500


def response_service_unavailable(message: str = 'Service temporarily unavailable', data: Union[dict, None] = None) -> tuple:
    """
    Use this response when a service is unavailable, e.g., a service that is down for maintenance.

    :param message: Message to be returned.
    :type message: str
    :param data: Any additional data to be returned.
    :return: Tuple of response and status code.
    :rtype: tuple
    """
    return {
        'status': 'Service Unavailable',
        'message': message,
        'data': data,
    }, 503
