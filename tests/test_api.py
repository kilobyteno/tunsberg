from flask import Flask

from tunsberg.api import get_api_version, get_api_version_from_flask_url


app = Flask(__name__)


def test_get_api_version_from_flask_url_default():
    """ Test that the default pattern matches """
    with app.test_request_context('/api/v1/resource'):
        assert get_api_version_from_flask_url() == 'v1'


def test_get_api_version_from_flask_url_custom_pattern():
    """ Test that the custom pattern matches """
    with app.test_request_context('/api/v2_1/resource'):
        assert get_api_version_from_flask_url(pattern=r'v\d+_\d+') == 'v2_1'


def test_get_api_version_from_flask_url_no_version():
    """ Test that the default return value is empty string """
    with app.test_request_context('/api/resource'):
        assert get_api_version_from_flask_url() == ''


def test_get_api_version_from_flask_url_default_return():
    """ Test that the default return value is 'v0' """
    with app.test_request_context('/api/resource'):
        assert get_api_version_from_flask_url(default='v0') == 'v0'


def test_get_api_version_from_flask_url_no_default_return():
    """ Test that the default return value is empty string """
    with app.test_request_context('/api/resource'):
        assert get_api_version_from_flask_url(default='') == ''


def test_get_api_version_standard():
    """ Test that the standard pattern matches """
    assert get_api_version('app.api.v1') == 'v1'
    assert get_api_version('module.v2.submodule') == 'v2'
    assert get_api_version('service.v3_1.beta') == 'v3_1'


def test_get_api_version_no_version():
    """ Test that the default return value is empty string """
    assert get_api_version('app.api') == ''
    assert get_api_version('module.submodule') == ''


def test_get_api_version_custom_pattern():
    """ Test that the custom pattern matches """
    assert get_api_version('app.api.v2021_04', pattern=r'v\d{4}_\d{2}') == 'v2021_04'
    assert get_api_version('service.v2021.beta', pattern=r'v\d{4}') == 'v2021'


def test_get_api_version_custom_default():
    """ Test that the custom default value is returned """
    assert get_api_version('app.api', default='no_version') == 'no_version'
    assert get_api_version('module.submodule', default='undefined') == 'undefined'
