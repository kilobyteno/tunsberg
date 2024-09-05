from tunsberg.responses import (
    response_bad_request,
    response_conflict,
    response_content_too_large,
    response_created,
    response_forbidden,
    response_no_content,
    response_not_found,
    response_service_unavailable,
    response_success,
    response_unauthorized,
    response_unsupported_media_type,
)


class TestResponseSuccess:
    def test_success_default(self):
        expected_response = ({'status': 'Success', 'message': 'Resource(s) were successfully retrieved', 'data': None}, 200)
        response = response_success()
        assert response == expected_response

    def test_success_custom_message(self):
        expected_response = ({'status': 'Success', 'message': 'Custom success message', 'data': None}, 200)
        response = response_success(message='Custom success message')
        assert response == expected_response

    def test_success_custom_data(self):
        expected_response = ({'status': 'Success', 'message': 'Resource(s) were successfully retrieved', 'data': {'key': 'value'}}, 200)
        response = response_success(data={'key': 'value'})
        assert response == expected_response


class TestResponseCreated:
    def test_created_custom_message(self):
        expected_response = ({'status': 'Created', 'message': 'Custom created message', 'data': None}, 201)
        response = response_created(message='Custom created message')
        assert response == expected_response

    def test_created_custom_data(self):
        expected_response = ({'status': 'Created', 'message': 'Resource created successfully', 'data': {'key': 'value'}}, 201)
        response = response_created(data={'key': 'value'})
        assert response == expected_response


class TestResponseNoContent:
    def test_no_content_default(self):
        expected_response = ({'status': 'No Content', 'message': 'Resource was successfully deleted', 'data': None}, 204)
        response = response_no_content()
        assert response == expected_response


class TestResponseBadRequest:
    def test_bad_request_default(self):
        expected_response = ({'status': 'Bad Request', 'message': 'Input validation failed', 'data': None}, 400)
        response = response_bad_request()
        assert response == expected_response

    def test_bad_request_custom_message(self):
        expected_response = ({'status': 'Bad Request', 'message': 'Custom bad request message', 'data': None}, 400)
        response = response_bad_request(message='Custom bad request message')
        assert response == expected_response

    def test_bad_request_custom_data(self):
        expected_response = ({'status': 'Bad Request', 'message': 'Input validation failed', 'data': {'key': 'value'}}, 400)
        response = response_bad_request(data={'key': 'value'})
        assert response == expected_response


class TestResponseUnauthorized:
    def test_unauthorized_default(self):
        expected_response = ({'status': 'Unauthorized', 'message': 'Missing or invalid credentials', 'data': None}, 401)
        response = response_unauthorized()
        assert response == expected_response

    def test_unauthorized_custom_message(self):
        expected_response = ({'status': 'Unauthorized', 'message': 'Custom unauthorized message', 'data': None}, 401)
        response = response_unauthorized(message='Custom unauthorized message')
        assert response == expected_response

    def test_unauthorized_custom_data(self):
        expected_response = ({'status': 'Unauthorized', 'message': 'Missing or invalid credentials', 'data': {'key': 'value'}}, 401)
        response = response_unauthorized(data={'key': 'value'})
        assert response == expected_response


class TestResponseForbidden:
    def test_forbidden_default(self):
        expected_response = ({'status': 'Forbidden', 'message': 'User is not authorized to perform this action', 'data': None}, 403)
        response = response_forbidden()
        assert response == expected_response

    def test_forbidden_custom_message(self):
        expected_response = ({'status': 'Forbidden', 'message': 'Custom forbidden message', 'data': None}, 403)
        response = response_forbidden(message='Custom forbidden message')
        assert response == expected_response

    def test_forbidden_custom_data(self):
        expected_response = ({'status': 'Forbidden', 'message': 'User is not authorized to perform this action', 'data': {'key': 'value'}}, 403)
        response = response_forbidden(data={'key': 'value'})
        assert response == expected_response


class TestResponseNotFound:
    def test_not_found_default(self):
        expected_response = ({'status': 'Not Found', 'message': 'Requested resource not found', 'data': None}, 404)
        response = response_not_found()
        assert response == expected_response

    def test_not_found_custom_message(self):
        expected_response = ({'status': 'Not Found', 'message': 'Custom not found message', 'data': None}, 404)
        response = response_not_found(message='Custom not found message')
        assert response == expected_response

    def test_not_found_custom_data(self):
        expected_response = ({'status': 'Not Found', 'message': 'Requested resource not found', 'data': {'key': 'value'}}, 404)
        response = response_not_found(data={'key': 'value'})
        assert response == expected_response


class TestResponseConflict:
    def test_conflict_default(self):
        expected_response = ({'status': 'Conflict', 'message': 'Conflict with the current state of the target resource', 'data': None}, 409)
        response = response_conflict()
        assert response == expected_response

    def test_conflict_custom_message(self):
        expected_response = ({'status': 'Conflict', 'message': 'Custom conflict message', 'data': None}, 409)
        response = response_conflict(message='Custom conflict message')
        assert response == expected_response

    def test_conflict_custom_data(self):
        expected_response = ({'status': 'Conflict', 'message': 'Conflict with the current state of the target resource', 'data': {'key': 'value'}}, 409)
        response = response_conflict(data={'key': 'value'})
        assert response == expected_response


class TestResponsePayloadTooLarge:
    def test_payload_too_large_default(self):
        expected_response = ({'status': 'Payload Too Large', 'message': 'Payload exceeds the allowed limit', 'data': None}, 413)
        response = response_content_too_large()
        assert response == expected_response

    def test_payload_too_large_custom_message(self):
        expected_response = ({'status': 'Payload Too Large', 'message': 'Custom payload too large message', 'data': None}, 413)
        response = response_content_too_large(message='Custom payload too large message')
        assert response == expected_response

    def test_payload_too_large_custom_data(self):
        expected_response = ({'status': 'Payload Too Large', 'message': 'Payload exceeds the allowed limit', 'data': {'key': 'value'}}, 413)
        response = response_content_too_large(data={'key': 'value'})
        assert response == expected_response


class TestResponseUnsupportedMediaType:
    def test_unsupported_media_type_default(self):
        expected_response = ({'status': 'Unsupported Media Type', 'message': 'Unsupported media type', 'data': None}, 415)
        response = response_unsupported_media_type()
        assert response == expected_response

    def test_unsupported_media_type_custom_message(self):
        expected_response = ({'status': 'Unsupported Media Type', 'message': 'Custom message', 'data': None}, 415)
        response = response_unsupported_media_type(message='Custom message')
        assert response == expected_response

    def test_unsupported_media_type_custom_data(self):
        expected_response = ({'status': 'Unsupported Media Type', 'message': 'Unsupported media type', 'data': {'key': 'value'}}, 415)
        response = response_unsupported_media_type(data={'key': 'value'})
        assert response == expected_response


class TestResponseServiceUnavailable:
    def test_service_unavailable_default(self):
        expected_response = ({'status': 'Service Unavailable', 'message': 'Service temporarily unavailable', 'data': None}, 503)
        response = response_service_unavailable()
        assert response == expected_response

    def test_service_unavailable_custom_message(self):
        expected_response = ({'status': 'Service Unavailable', 'message': 'Custom unavailable message', 'data': None}, 503)
        response = response_service_unavailable(message='Custom unavailable message')
        assert response == expected_response
