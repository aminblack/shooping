from .messages import (
    PASSWORD_LENGTH_ERROR,
    PASSWORD_TYPE_ERROR
)


class WrongUserNameException(ValueError):
    pass
class TypeUserNameException(TypeError):
    pass


class WrongPassWordException(ValueError):
    def __str__(self):
        return PASSWORD_LENGTH_ERROR

class TypePassWordException(TypeError):
    def __str__(self):
        return PASSWORD_TYPE_ERROR
