import typing


class DeserializerException(BaseException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Diagnostics:
    __errors: typing.List["DeserializerError"]
    __warnings: typing.List["DeserializerWarning"]

    def __init__(self) -> None:
        self.__errors = []
        self.__warnings = []

    def push_error(self, error: "DeserializerError") -> None:
        self.__errors.append(error)

    def push_warning(self, warning: "DeserializerWarning") -> None:
        self.__warnings.append(warning)

    def to_exception(self) -> None:
        """
        This method raises a DeserializerException if there are any errors in the diagnostics.
        """
        if len(self.__errors) > 0:
            raise DeserializerException(self.__errors)


class DeserializerError:
    def __init__(self, message: str):
        self.__message = message

    @staticmethod
    def create_error(message: str) -> "DeserializerError":
        return DeserializerError(message)

    def __str__(self) -> str:
        return f"Error: {self.__message}"


class DeserializerWarning:
    def __init__(self, message: str):
        self.__message = message

    @staticmethod
    def create_warning(message: str) -> "DeserializerWarning":
        return DeserializerWarning(message)

    def __str__(self) -> str:
        return f"Warning: {self.__message}"
