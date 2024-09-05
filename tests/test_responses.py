from fastapi_pagination import Page
from starlette import status

from tunsberg.responses import (
    ResponseModel,
    generate_json_response,
    response_bad_request,
    response_conflict,
    response_created,
    response_custom,
    response_forbidden,
    response_internal_server_error,
    response_no_content,
    response_not_found,
    response_not_implemented,
    response_pagination,
    response_request_entity_too_large,
    response_service_unavailable,
    response_success,
    response_unauthorized,
    response_unsupported_media_type,
)


class TestGenerateJsonResponse:
    # Generates JSON response with status code and message
    def test_generates_json_response_with_status_code_and_message(self):
        response_model = ResponseModel(status_code=status.HTTP_200_OK, message='Success')
        response = generate_json_response(response_model)
        assert response.status_code == status.HTTP_200_OK
        assert response.body == b'{"status_code":200,"message":"Success"}'

    # Handles None data gracefully
    def test_handles_none_data_gracefully(self):
        response_model = ResponseModel(status_code=status.HTTP_200_OK, message='Success', data=None)
        response = generate_json_response(response_model)
        assert response.status_code == status.HTTP_200_OK
        assert response.body == b'{"status_code":200,"message":"Success"}'

    # Handles empty dictionary data
    def test_handles_empty_dictionary_data(self):
        response_model = ResponseModel(status_code=status.HTTP_200_OK, message='Success', data={})
        response = generate_json_response(response_model)
        assert response.status_code == status.HTTP_200_OK
        assert response.body == b'{"status_code":200,"message":"Success"}'


class TestResponseSuccess:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 200 when called with default parameters"""
        response = response_success()
        assert response.status_code == status.HTTP_200_OK
        assert response.body == b'{"status_code":200,"message":"Resources was successfully retrieved"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_success('Custom message')
        assert response.status_code == status.HTTP_200_OK
        assert response.body == b'{"status_code":200,"message":"Custom message"}'

    def test_custom_data(self):
        """Returns a JSONResponse with custom data when called with custom data"""
        response = response_success(data={'key': 'value'})
        assert response.status_code == status.HTTP_200_OK
        assert response.body == b'{"status_code":200,"message":"Resources was successfully retrieved","data":{"key":"value"}}'


class TestResponsePagination:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 200 when called with default parameters"""
        response = response_pagination()
        assert response.status_code == status.HTTP_200_OK
        assert response.body == b'{"status_code":200,"message":"Resources was successfully retrieved"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_pagination('Custom message')
        assert response.status_code == status.HTTP_200_OK
        assert response.body == b'{"status_code":200,"message":"Custom message"}'

    def test_custom_data(self):
        """Returns a JSONResponse with custom data when called with custom data"""
        response = response_pagination(data={'key': 'value'})
        assert response.status_code == status.HTTP_200_OK
        assert response.body == b'{"status_code":200,"message":"Resources was successfully retrieved","data":{"key":"value"}}'

    def test_response_with_pagination_data(self):
        """Generates a JSON response with a 200 status code when pagination data is provided"""
        pagination = Page(page=1, total=11, size=10, pages=2, items=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        response = response_pagination(message='Test message', data={'key': 'value'}, pagination=pagination)

        assert response.status_code == status.HTTP_200_OK
        assert response.body == b'{"status_code":200,"message":"Test message","data":{"key":"value"},"pagination":{"total":11,"page":1,"size":10,"pages":2}}'


class TestResponseCreated:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 201 when called with default parameters"""
        response = response_created()
        assert response.status_code == status.HTTP_201_CREATED
        assert response.body == b'{"status_code":201,"message":"Resource was successfully created"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_created('Custom message')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.body == b'{"status_code":201,"message":"Custom message"}'

    def test_custom_data(self):
        """Returns a JSONResponse with custom data when called with custom data"""
        response = response_created(data={'key': 'value'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.body == b'{"status_code":201,"message":"Resource was successfully created","data":{"key":"value"}}'


class TestResponseNoContent:
    def test_default_parameters(self):
        """Returns a Response with status code 204 when called with default parameters"""
        response = response_no_content()
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.body == b''


class TestResponseBadRequest:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 400 when called with default parameters"""
        response = response_bad_request()
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.body == b'{"status_code":400,"message":"Bad request"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_bad_request('Custom message')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.body == b'{"status_code":400,"message":"Custom message"}'

    def test_custom_data(self):
        """Returns a JSONResponse with custom data when called with custom data"""
        response = response_bad_request(data={'key': 'value'})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.body == b'{"status_code":400,"message":"Bad request","data":{"key":"value"}}'


class TestResponseUnauthorized:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 401 when called with default parameters"""
        response = response_unauthorized()
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.body == b'{"status_code":401,"message":"Unauthorized"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_unauthorized('Custom message')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert response.body == b'{"status_code":401,"message":"Custom message"}'


class TestResponseForbidden:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 403 when called with default parameters"""
        response = response_forbidden()
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.body == b'{"status_code":403,"message":"Forbidden"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_forbidden('Custom message')
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert response.body == b'{"status_code":403,"message":"Custom message"}'


class TestResponseNotFound:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 404 when called with default parameters"""
        response = response_not_found()
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.body == b'{"status_code":404,"message":"Resource not found"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_not_found('Custom message')
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.body == b'{"status_code":404,"message":"Custom message"}'


class TestResponseConflict:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 409 when called with default parameters"""
        response = response_conflict()
        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.body == b'{"status_code":409,"message":"Resource already exists"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_conflict('Custom message')
        assert response.status_code == status.HTTP_409_CONFLICT
        assert response.body == b'{"status_code":409,"message":"Custom message"}'


class TestResponseContentTooLarge:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 413 when called with default parameters"""
        response = response_request_entity_too_large()
        assert response.status_code == status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
        assert response.body == b'{"status_code":413,"message":"Request entity too large"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_request_entity_too_large('Custom message')
        assert response.status_code == status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
        assert response.body == b'{"status_code":413,"message":"Custom message"}'


class TestResponseUnsupportedMediaType:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 415 when called with default parameters"""
        response = response_unsupported_media_type()
        assert response.status_code == status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        assert response.body == b'{"status_code":415,"message":"Unsupported media type"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_unsupported_media_type('Custom message')
        assert response.status_code == status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        assert response.body == b'{"status_code":415,"message":"Custom message"}'


class TestResponseInternalServerError:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 500 when called with default parameters"""
        response = response_internal_server_error()
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.body == b'{"status_code":500,"message":"Internal server error"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_internal_server_error('Custom message')
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.body == b'{"status_code":500,"message":"Custom message"}'


class TestResponseServiceUnavailable:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 503 when called with default parameters"""
        response = response_service_unavailable()
        assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert response.body == b'{"status_code":503,"message":"Service unavailable"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_service_unavailable('Custom message')
        assert response.status_code == status.HTTP_503_SERVICE_UNAVAILABLE
        assert response.body == b'{"status_code":503,"message":"Custom message"}'


class TestResponseNotImplemented:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 501 when called with default parameters"""
        response = response_not_implemented()
        assert response.status_code == status.HTTP_501_NOT_IMPLEMENTED
        assert response.body == b'{"status_code":501,"message":"Not implemented"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_not_implemented('Custom message')
        assert response.status_code == status.HTTP_501_NOT_IMPLEMENTED
        assert response.body == b'{"status_code":501,"message":"Custom message"}'


class TestResponseCustom:
    def test_default_parameters(self):
        """Returns a JSONResponse with status code 500 when called with default parameters"""
        response = response_custom()
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.body == b'{"status_code":500,"message":"An unknown error has occurred"}'

    def test_custom_message(self):
        """Returns a JSONResponse with a custom message when called with custom message"""
        response = response_custom('Custom message')
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.body == b'{"status_code":500,"message":"Custom message"}'

    def test_custom_status_code(self):
        """Returns a JSONResponse with a custom status code when called with custom status code"""
        response = response_custom(status_code=404)
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.body == b'{"status_code":404,"message":"An unknown error has occurred"}'

    def test_custom_data(self):
        """Returns a JSONResponse with custom data when called with custom data"""
        response = response_custom(data={'key': 'value'})
        assert response.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
        assert response.body == b'{"status_code":500,"message":"An unknown error has occurred","data":{"key":"value"}}'
