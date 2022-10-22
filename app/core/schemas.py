from typing import Generic, Optional, TypeVar

from pydantic import BaseModel as BModel
from pydantic.generics import GenericModel

from app.core.models.enums import ErrorCode

DataType = TypeVar("DataType")


class IResponseBase(GenericModel, Generic[DataType]):
    data: Optional[DataType]


class BaseModel(BModel):
    class Config:
        orm_mode = True


class APIException(Exception):
    def __init__(self, error: ErrorCode):
        self.code = error.code
        self.message = error.message
        self.status_code = error.status_code


class MessageOut(BaseModel):
    message: str
