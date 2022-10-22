from fastapi.security import OAuth2PasswordBearer
from jwt import decode

from app.config import settings
from app.core.models.enums import ErrorCode
from app.core.schemas import APIException

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/api/" + settings.API_VERSION + "/auth/login"
)


def verify_access_token(token: str):
    """
    This function verifies the given token with SECRET_KEY and JWT_ALGORITHM
    :param token:
    :raises APIException: It raises if data couldn't decode or something else
    """
    try:
        data = decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        if data is None:
            raise APIException(ErrorCode.unauthorized)
        return data
    except Exception:
        raise APIException(ErrorCode.unauthorized)
