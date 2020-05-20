from final_graduation.kernal import get_codes


class AppException(Exception):
    _code: int
    _msg: str

    def __init__(self, msg: str = '', code: int = None):
        super().__init__(msg)

        self._code = code or get_codes(type(self).__name__)
        self._msg = msg

    @property
    def code(self) -> int:
        return self._code

    @property
    def msg(self) -> str:
        return self._msg


class UnknownError(AppException):
    def __init__(self, exception: Exception):
        super().__init__(f'{type(exception).__name__}: {exception}')
