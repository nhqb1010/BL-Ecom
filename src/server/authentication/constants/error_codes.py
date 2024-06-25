from app.errors.error_codes import AppErrorCodes


class AuthErrorCodes(AppErrorCodes):
    """
    Enum class representing authentication errors.
    """

    INVALID_LOGIN_CREDENTIALS = "Invalid email or password."
    INVALID_TOKEN = "Access token is invalid or expired."
