from starlette import status

from tunsberg.responses import (
    response_success,
)


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
