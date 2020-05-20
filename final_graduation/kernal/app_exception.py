from typing import Dict
from . import config as cfg


class AppException(Exception):
    _code: int
    _msg: str
    _codes: Dict[str, int]

    def __init__(self, msg: str = '', code: int = None):
        super().__init__(msg)
        self._load_codes()

        self._code = code or self._codes[type(self).__name__]
        self._msg = msg

    @property
    def code(self) -> int:
        return self._code

    @property
    def msg(self) -> str:
        return self._msg

    @classmethod
    def _load_codes(cls):
        from final_graduation.kernal.bootstrap import Bootstrap
        config = Bootstrap.configs['exception']
        assert isinstance(config, ExceptionConfig)
        cls._codes = config.codes


class ExceptionConfig(cfg.BaseConfig):
    codes: Dict[str, int] = cfg.Option(
        required=True, default={},
        preprocess=lambda x, _: {name: int(code) for name, code in x.items()}  # convert all code to integer
    )


class UnknownError(AppException):
    def __init__(self, exception: Exception):
        super().__init__(f'{type(exception).__name__}: {exception}')
