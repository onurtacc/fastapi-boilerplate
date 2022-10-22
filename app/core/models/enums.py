from enum import Enum, IntEnum


class ErrorCode(IntEnum):
    def __new__(cls, code, message, status_code=404):
        obj = int.__new__(cls, code)
        obj._value_ = code

        obj.code = code
        obj.message = message
        obj.status_code = status_code
        return obj

    # Access and Permission Errors
    invalid_access_token = 10001, "Invalid Access Token", 403
    invalid_permission = 10002, "Invalid Permission.", 403

    # Auth Errors
    unauthorized = 10100, "User not authorized.", 401

    # User Errors
    user_not_found = 10200, "User not found.", 404
    user_already_exist = 10201, "User already exist.", 400
    inactive_user = 10201, "User is not active.", 400
    username_or_password_not_correct = 10203, "Username or password not correct.", 404


class UserRole(str, Enum):
    admin = "admin"
    customer = "customer"
