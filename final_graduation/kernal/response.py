import traceback
from typing import Dict, Any, Type

from . import AppException, UnknownError


def make_response(f):
    def inner(*args, **kwargs):
        response = Response()
        with response:
            response.result = f(*args, **kwargs)
        return response

    return inner


def make_response_all_verbs(cls: Type):
    verbs = [
        'post', 'get', 'put', 'patch', 'delete'
    ]

    for name in verbs:
        if name in cls.__dict__:
            setattr(cls, name, make_response(cls.__dict__[name]))
    return cls


class Response(dict):
    debug: bool = True
    _response: Dict

    def __init__(self):
        super().__init__()
        self['code'] = 0
        self['result'] = None
        self['msg'] = ''

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            if isinstance(exc_val, AppException):
                self.set_exception(exc_val)
            else:
                self.set_exception(UnknownError(exc_val))
            if self.debug:
                traceback.print_tb(exc_tb)
        return True

    @classmethod
    def set_debug(cls, debug: bool) -> None:
        cls.debug = debug

    @property
    def code(self) -> int:
        return self['code']

    @code.setter
    def code(self, code: str) -> None:
        self['code'] = code

    @property
    def result(self) -> Any:
        return self['result']

    @result.setter
    def result(self, result: Any) -> None:
        self['result'] = result

    @property
    def msg(self) -> str:
        return self['msg']

    @msg.setter
    def msg(self, msg: str) -> None:
        self['msg'] = msg

    def set_exception(self, exception: AppException) -> None:
        self.code = exception.code
        self.result = None
        self.msg = f'{type(exception).__name__}: {exception.msg}'
