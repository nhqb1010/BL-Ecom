import enum


class AppErrorCodes(enum.Enum):
    pass


class AuthErrorCodes(AppErrorCodes):
    """
    Enum class representing authentication errors.
    """

    INVALID_LOGIN_CREDENTIALS = "Invalid email or password."
    INVALID_TOKEN = "Access token is invalid or expired."
