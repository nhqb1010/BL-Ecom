from http import HTTPStatus

from .error_codes import AuthErrorCodes


class AppException(Exception):
    """Base class for exceptions in the application.

    Attributes:

        message (str): The error message.
        code (str | int): The error code.
        status_code (int): The HTTP status code.
    """
    
    def __init__(self, message: str, code: str | int, status_code: int):
        self.code = code
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        """
        Converts the exception to a dictionary representation.

        Returns:
            dict: A dictionary containing the error code and error message.
        """
        return {
            'error_code': self.code,
            'error_message': self.message,
        }
    

class AppAuthException(AppException):
    """Exception raised for authentication errors in the application.

    Attributes:
        error (AuthErrorCodes): The error code associated with the exception.
    """

    status_code = HTTPStatus.UNAUTHORIZED

    def __init__(self, error: AuthErrorCodes):
        super().__init__(error.value, error.name, self.status_code)
