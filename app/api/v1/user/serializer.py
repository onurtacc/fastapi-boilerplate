from pydantic import EmailStr

from app.core.schemas import BaseModel


class UserDetailOut(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    role: str
    created_at: str
