from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.config import settings
from app.core.helpers.auth import verify_access_token
from app.core.models import User
from app.core.models.enums import ErrorCode
from app.core.schemas import APIException
from app.db.database import get_db
from app.services.user import UserService

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl="/api/" + settings.API_VERSION + "/auth/login"
)


def check_user_token(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> User:
    """
    This function verifies the token by a function and gets the current user from service
    :param db: Related db
    :param token: Related token
    :return: User Object
    """
    token_data = verify_access_token(token)
    user = UserService(db).get_user_by_username(username=token_data["username"])
    return user


def get_current_active_user(current_user: User = Depends(check_user_token)) -> User:
    """
    This function checks the current_user is active or not
    :param current_user: User Object
    :return: Current user
    :raises APIException: It raises if current_user is not active
    """
    if not current_user.is_active:
        raise APIException(ErrorCode.inactive_user)
    return current_user
