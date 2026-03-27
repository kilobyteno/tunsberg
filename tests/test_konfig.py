import json
import logging
import os
import sys

import pytest

from tunsberg.konfig import JsonFormatter, check_required_env_vars, log_config, uvicorn_log_config


class TestLogConfig:
    def test_default_config(self):
        log_lvl = logging.NOTSET
        config = log_config(log_level=log_lvl)
        assert config['version'] == 1
        assert not config['disable_existing_loggers']
        assert config['formatters']['default']['format'] == '%(asctime)s - [%(levelname)s] %(name)s: %(message)s'
        assert config['handlers']['file']['class'] == 'logging.FileHandler'
        assert config['handlers']['file']['filename'] == 'fastapi.log'
        assert config['handlers']['file']['formatter'] == 'default'
        assert config['handlers']['console']['class'] == 'logging.StreamHandler'
        assert config['handlers']['console']['formatter'] == 'default'
        assert config['loggers']['uvicorn']['handlers'] == ['time_rotating_file', 'console']
        assert config['loggers']['uvicorn']['level'] == logging.getLevelName(log_lvl)
        assert not config['loggers']['uvicorn']['propagate']
        assert config['loggers']['uvicorn.error']['handlers'] == ['time_rotating_file', 'console']
        assert config['loggers']['uvicorn.error']['level'] == logging.getLevelName(log_lvl)
        assert not config['loggers']['uvicorn.error']['propagate']
        assert config['loggers']['uvicorn.access']['handlers'] == ['time_rotating_file', 'console']
        assert config['loggers']['uvicorn.access']['level'] == logging.getLevelName(log_lvl)
        assert not config['loggers']['uvicorn.access']['propagate']

    def test_invalid_log_level(self):
        with pytest.raises(ValueError):
            log_config(log_level=999)

    def test_empty_log_format(self):
        with pytest.raises(ValueError):
            log_config(log_level=logging.NOTSET, log_format='')

    def test_empty_log_file_path(self):
        with pytest.raises(ValueError):
            log_config(log_level=logging.NOTSET, log_file_path='')

    def test_custom_log_format(self):
        log_format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(filename)s - %(lineno)s'
        config = log_config(log_level=logging.NOTSET, log_format=log_format)
        assert config['formatters']['default']['format'] == log_format

    def test_custom_log_file_path(self):
        log_file_path = 'custom.log'
        config = log_config(log_level=logging.NOTSET, log_file_path=log_file_path)
        assert config['handlers']['file']['filename'] == log_file_path

    def test_custom_log_level(self):
        log_lvl = logging.INFO
        config = log_config(log_level=log_lvl)
        assert config['loggers']['uvicorn']['level'] == logging.getLevelName(log_lvl)
        assert config['loggers']['uvicorn.error']['level'] == logging.getLevelName(log_lvl)
        assert config['loggers']['uvicorn.access']['level'] == logging.getLevelName(log_lvl)


class TestJsonFormatter:
    def test_format_emits_json_with_expected_keys(self):
        formatter = JsonFormatter()
        record = logging.LogRecord(
            name='test.logger',
            level=logging.INFO,
            pathname='x.py',
            lineno=10,
            msg='hello',
            args=(),
            exc_info=None,
        )
        payload = json.loads(formatter.format(record))
        assert payload['message'] == 'hello'
        assert payload['level'] == 'INFO'
        assert payload['logger'] == 'test.logger'
        assert 'timestamp' in payload

    def test_format_includes_exception_when_exc_info_set(self):
        formatter = JsonFormatter()
        try:
            raise ValueError('boom')
        except ValueError:
            record = logging.LogRecord(
                name='test',
                level=logging.ERROR,
                pathname='x.py',
                lineno=1,
                msg='failed',
                args=(),
                exc_info=sys.exc_info(),
            )
        payload = json.loads(formatter.format(record))
        assert 'exception' in payload
        assert 'ValueError' in payload['exception']


class TestUvicornLogConfig:
    def test_deprecated_success_returns_config(self):
        with pytest.warns(DeprecationWarning, match='uvicorn_log_config'):
            config = uvicorn_log_config()
        assert config['version'] == 1
        assert not config['disable_existing_loggers']
        assert config['handlers']['file']['filename'] == 'uvicorn.log'

    def test_invalid_log_level(self):
        with pytest.warns(DeprecationWarning), pytest.raises(ValueError, match='Invalid log level'):
            uvicorn_log_config(log_level=999)

    def test_empty_log_format(self):
        with pytest.warns(DeprecationWarning), pytest.raises(ValueError, match='Log format cannot be empty'):
            uvicorn_log_config(log_format='')

    def test_empty_log_file_path(self):
        with pytest.warns(DeprecationWarning), pytest.raises(ValueError, match='Log file path cannot be empty'):
            uvicorn_log_config(log_file_path='')


class TestCheckRequiredEnvVars:
    # Set the environment variable for testing
    os.environ['RANDOM_ENV_VAR'] = 'random_value'

    def test_validate_if_true_in_local_development_env(self):
        req_envs = {'RANDOM_ENV_VAR': {'runtime': True, 'build': True}}
        check = check_required_env_vars(required_env_vars=req_envs, env='local')
        assert check

    def test_validate_if_true_in_staging_env(self):
        req_envs = {'RANDOM_ENV_VAR': {'runtime': True, 'build': True}}
        check = check_required_env_vars(required_env_vars=req_envs, env='staging', live_envs=['staging'])
        assert check

    def test_validate_if_true_in_prod_env(self):
        req_envs = {'RANDOM_ENV_VAR': {'runtime': True, 'build': True}}
        check = check_required_env_vars(required_env_vars=req_envs, env='prod', live_envs=['prod'])
        assert check

    def test_validate_that_it_fails_if_env_var_is_not_set(self):
        req_envs = {'SOME_OTHER_RANDOM_ENV_VAR': {'runtime': True, 'build': True}}
        with pytest.raises(ValueError):
            check_required_env_vars(required_env_vars=req_envs, env='production', live_envs=['production'])

    def test_validate_that_it_fails_for_code_build_if_env_var_is_not_set(self):
        req_envs = {'SOME_OTHER_RANDOM_ENV_VAR': {'runtime': False, 'build': True}}
        with pytest.raises(ValueError):
            check_required_env_vars(required_env_vars=req_envs, env='production', live_envs=['production'], code_build=True)

    def test_validate_that_it_fails_for_runtime_if_env_var_is_not_set(self):
        req_envs = {'SOME_OTHER_RANDOM_ENV_VAR': {'runtime': True, 'build': False}}
        with pytest.raises(ValueError):
            check_required_env_vars(required_env_vars=req_envs, env='production', live_envs=['production'])
