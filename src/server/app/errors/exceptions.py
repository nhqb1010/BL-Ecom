from app.errors.error_codes import AppErrorCodes


class AppException(Exception):
    """Base class for exceptions in the application.

    Attributes:

        message (str): The error message.
        code (str | int): The error code.
        status_code (int): The HTTP status code.
    """

    def __init__(self, error_code: AppErrorCodes, status_code: int):
        self.code = error_code.name
        self.message = error_code.value
        self.status_code = status_code

    def to_dict(self):
        """
        Converts the exception to a dictionary representation.

        Returns:
            dict: A dictionary containing the error code and error message.
        """
        return {
            "error_code": self.code,
            "error_message": self.message,
        }
