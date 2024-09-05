import json
from typing import Any, Dict, List, Optional

from fastapi import Query
from fastapi_pagination import Page, Params
from pydantic import BaseModel, Field
from starlette import status
from starlette.responses import JSONResponse, Response


class Pagination(BaseModel):
    """Pagination model"""

    total: int
    page: int
    size: int
    pages: int


class ResponseModel(BaseModel):
    """Base Response model"""

    status_code: int
    message: str
    data: Optional[Dict[str, Any]] | Optional[List[Any]] | Optional[str] = None
    pagination: Optional[Pagination] = Field(None, exclude=True)
    background_tasks: Optional[Any] = Field(None, exclude=True)


class ResponsePaginationModel(ResponseModel):
    """Override Response model for pagination to be included"""

    pagination: Optional[Pagination] = None


class CustomParams(Params):
    """Override Params for custom default size"""

    size: int = Query(10, ge=1, le=100, description='Page size')


def generate_json_response(response: ResponseModel) -> JSONResponse:
    """
    Generate a JSON response for FastAPI from a ResponseModel.

    :param response: ResponseModel to be converted
    :type response: ResponseModel
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    content = dict()
    content['status_code'] = response.status_code
    content['message'] = response.message
    background = None

    if response.data:
        if isinstance(response.data, dict):
            content['data'] = response.data
        else:
            content['data'] = json.loads(response.data)
    if response.pagination:
        content['pagination'] = response.pagination.model_dump()
    if response.background_tasks:
        background = response.background_tasks

    return JSONResponse(status_code=response.status_code, content=content, background=background)


def response_success(message: str = 'Resources was successfully retrieved', data: Optional[Any] = None, background_tasks: Optional[Any] = None) -> JSONResponse:
    """
    Use this response when a resource is successfully retrieved.

    :param message: Message to be returned
    :type message: str
    :param data: Any additional data to be returned
    :type data: Any
    :param background_tasks: Any background tasks to be run
    :type background_tasks: Any
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_200_OK, message=message, data=data, background_tasks=background_tasks))


def response_pagination(message: str = 'Resources was successfully retrieved', data: Optional[Any] = None, pagination: Optional[Page] = None) -> JSONResponse:
    """
    Use this response when a resource is successfully retrieved.

    :param message: Message to be returned
    :type message: str
    :param data: Any additional data to be returned
    :type data: Any
    :param pagination: Pagination data to be returned
    :type pagination: Page
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    page_info = None
    if pagination:
        page_info = Pagination(page=pagination.page, total=pagination.total, size=pagination.size, pages=pagination.pages)

    return generate_json_response(ResponsePaginationModel(status_code=status.HTTP_200_OK, message=message, data=data, pagination=page_info))


def response_created(message: str = 'Resource was successfully created', data: Optional[Any] = None) -> JSONResponse:
    """
    Use this response when a resource is successfully created.

    :param message: Message to be returned
    :type message: str
    :param data: Any additional data to be returned
    :type data: Any
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_201_CREATED, message=message, data=data))


def response_no_content() -> Response:
    """
    Use this response when a resource is successfully deleted.

    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def response_bad_request(message: str = 'Bad request', data: Optional[Any] = None) -> JSONResponse:
    """
    Use this response when a bad request is made.

    :param message: Message to be returned
    :type message: str
    :param data: Any additional data to be returned
    :type data: Any
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_400_BAD_REQUEST, message=message, data=data))


def response_unauthorized(message: str = 'Unauthorized') -> JSONResponse:
    """
    Use this response when a request is unauthorized.

    :param message: Message to be returned
    :type message: str
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_401_UNAUTHORIZED, message=message))


def response_forbidden(message: str = 'Forbidden') -> JSONResponse:
    """
    Use this response when a request is forbidden.

    :param message: Message to be returned
    :type message: str
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=403, message=message))


def response_not_found(message: str = 'Resource not found') -> JSONResponse:
    """
    Use this response when a resource is not found.

    :param message: Message to be returned
    :type message: str
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_404_NOT_FOUND, message=message))


def response_conflict(message: str = 'Resource already exists') -> JSONResponse:
    """
    Use this response when a resource already exists.

    :param message: Message to be returned
    :type message: str
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_409_CONFLICT, message=message))


def response_request_entity_too_large(message: str = 'Request entity too large') -> JSONResponse:
    """
    Use this response when a request is too large.

    :param message: Message to be returned
    :type message: str
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, message=message))


def response_unsupported_media_type(message: str = 'Unsupported media type') -> JSONResponse:
    """
    Use this response when a user has supplied invalid file input. For example, a file that is not a .png

    :param message: Message to be returned
    :type message: str
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, message=message))


def response_internal_server_error(message: str = 'Internal server error') -> JSONResponse:
    """
    Use this response when an internal server error occurs.

    :param message: Message to be returned
    :type message: str
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=message))


def response_service_unavailable(message: str = 'Service unavailable') -> JSONResponse:
    """
    Use this response when a service is unavailable.

    :param message: Message to be returned
    :type message: str
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, message=message))


def response_not_implemented(message: str = 'Not implemented') -> JSONResponse:
    """
    Use this response when a request is not implemented.

    :param message: Message to be returned
    :type message: str
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status.HTTP_501_NOT_IMPLEMENTED, message=message))


def response_custom(message: str = 'An unknown error has occurred', status_code: int = 500, data: Optional[Any] = None) -> JSONResponse:
    """
    Use this response when a response is needed with a custom message and status code.

    :param message: Message to be returned
    :type message: str
    :param status_code: Status code to be returned
    :type status_code: int
    :param data: Any additional data to be returned
    :type data: Any
    :return: Tuple of response and status code
    :rtype: Tuple[Dict[str, Any], int]
    """
    return generate_json_response(ResponseModel(status_code=status_code, message=message, data=data))
