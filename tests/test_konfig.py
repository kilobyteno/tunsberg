import logging

import pytest

from tunsberg.konfig import uvicorn_config


class TestUvicornConfig:
    def test_default_config(self):
        log_lvl = logging.NOTSET
        config = uvicorn_config(log_level=log_lvl)
        assert config['version'] == 1
        assert not config['disable_existing_loggers']
        assert config['formatters']['default']['format'] == '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        assert config['handlers']['file']['class'] == 'logging.FileHandler'
        assert config['handlers']['file']['filename'] == 'uvicorn.log'
        assert config['handlers']['file']['formatter'] == 'default'
        assert config['handlers']['console']['class'] == 'logging.StreamHandler'
        assert config['handlers']['console']['formatter'] == 'default'
        assert config['loggers']['uvicorn']['handlers'] == ['file', 'console']
        assert config['loggers']['uvicorn']['level'] == logging.getLevelName(log_lvl)
        assert not config['loggers']['uvicorn']['propagate']
        assert config['loggers']['uvicorn.error']['handlers'] == ['file', 'console']
        assert config['loggers']['uvicorn.error']['level'] == logging.getLevelName(log_lvl)
        assert not config['loggers']['uvicorn.error']['propagate']
        assert config['loggers']['uvicorn.access']['handlers'] == ['file', 'console']
        assert config['loggers']['uvicorn.access']['level'] == logging.getLevelName(log_lvl)
        assert not config['loggers']['uvicorn.access']['propagate']

    def test_invalid_log_level(self):
        with pytest.raises(ValueError):
            uvicorn_config(log_level=999)

    def test_empty_log_format(self):
        with pytest.raises(ValueError):
            uvicorn_config(log_level=logging.NOTSET, log_format='')

    def test_empty_log_file_path(self):
        with pytest.raises(ValueError):
            uvicorn_config(log_level=logging.NOTSET, log_file_path='')
