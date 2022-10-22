from datetime import datetime, timedelta
from typing import Optional

from fastapi.encoders import jsonable_encoder
from jwt import encode

from app.config import settings
from app.core.helpers.hash import HashHelper
from app.core.models import User
from app.core.models.enums import ErrorCode
from app.core.schemas import APIException


class UserService:
    """
    This service performs the necessary operations regarding the user.
    """

    def __init__(self, db):
        self.db = db
        self.hash_helper = HashHelper()

    def login_user(self, username: str, password: str) -> dict:
        """
        This function performs login with given credentials and returns some information along with access_token
        :param username: Related username
        :param password: Related password
        :return: dict
        :raises APIException: It raises if given username and password don't match
        """
        user = self.get_user_by_username(username=username)

        if not user or not self.hash_helper.verify_password(
            user.hashed_password, password
        ):
            raise APIException(ErrorCode.username_or_password_not_correct)

        access_token = self.create_access_token({"username": user.username})

        self.db.add(user)
        self.db.commit()

        return {
            "access_token": access_token,
            "token_type": "bearer",
            "username": user.username,
            "email": user.email,
        }

    def create_user(
        self, username: str, name: str, surname: str, email: str, password: str
    ) -> dict:
        """
        This function creates a user by given data
        :param username: User's username
        :param name: User's first name
        :param surname: User's last name
        :param email: User's e-mail
        :param password: User's password
        :return: User Object
        """
        user = self.get_user_by_email(email, show_error=False)

        if user:
            raise APIException(ErrorCode.user_already_exist)

        user = User()
        user.username = username
        user.name = name
        user.surname = surname
        user.email = email
        user.hashed_password = self.hash_helper.get_password_hash(password)

        self.db.add(user)
        self.db.commit()

        return {"message": "Registration successful."}

    def get_user_by_email(self, email: str, show_error: bool = True) -> User:
        """
        This function checks for the existence of a user with the given email address
        :param email: E-mail address to check
        :param show_error: Specifies whether to give an error when the user is not found. If given false, the empty object is returned
        :return: User Object
        """
        user = self.db.query(User).filter(User.email == email).first()
        if not user and show_error:
            raise APIException(ErrorCode.user_not_found)
        return user

    def get_user_by_username(self, username: str) -> User:
        """
        This function checks for the existence and status of a user with the given username and returns User
        :param username: Username to check
        :return: User Object
        :raises APIException: It raises if given username does not exist or status is False
        """
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            raise APIException(ErrorCode.user_not_found)
        return user

    def get_user_by_id(self, user_id: int) -> User:
        """
        This function checks for the existence and status of a user with the given user_id and returns User
        :param user_id: User ID to check
        :return: User Object
        :raises APIException: It raises if given user_id does not exist or status is False
        """
        user = self.db.query(User).filter(User.id == user_id).first()
        if not user:
            raise APIException(ErrorCode.user_not_found)
        return user

    @staticmethod
    def encode_user_detail(user: User):
        """
        This function takes a user instance and returns given user by dict
        :param user: User instance
        :return: User Dict
        """
        return jsonable_encoder(user)

    @staticmethod
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        """
        This function create an access token by given data
        :param data: Any dict
        :param expires_delta: Optional timedelta
        :return: Encoded JWT
        """
        to_jwt_encode = data.copy()

        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=settings.JWT_EXPIRES_TIME)

        to_jwt_encode.update({"exp": expire})
        encoded_jwt = encode(
            to_jwt_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM
        )

        return encoded_jwt
