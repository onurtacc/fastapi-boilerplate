from sqlalchemy import Boolean, Enum, String
from sqlalchemy.sql.schema import Column

from app.core.models.base import BaseModel

from .enums import UserRole


class User(BaseModel):
    __tablename__ = "user"

    username = Column(String)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserRole), default=UserRole.customer)
    hashed_password = Column(String)

    def __repr__(self):
        return "User:" + self.username + " ({})".format(self.role)
