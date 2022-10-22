from pydantic import BaseModel, EmailStr, Field


class LoginOut(BaseModel):
    access_token: str
    token_type: str
    username: str
    email: EmailStr


class RegisterIn(BaseModel):
    username: str = Field(title="Username", description="username", max_length=50)
    name: str = Field(
        title="First Name", description="User's first name", max_length=50
    )
    surname: str = Field(
        title="Last Name", description="User's last name", max_length=50
    )
    email: EmailStr = Field(title="E-Mail", description="User's e-mail")
    password: str = Field(title="Password", description="password", min_length=6)
