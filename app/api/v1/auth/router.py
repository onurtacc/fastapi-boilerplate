from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.v1.auth.serializer import LoginOut, RegisterIn
from app.core.schemas import MessageOut
from app.db.database import get_db
from app.services.user import UserService

router = APIRouter()


@router.post("/login", response_model=LoginOut)
def user_login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    return UserService(db).login_user(form_data.username, form_data.password)


@router.post("/register", response_model=MessageOut)
def user_register(
    form_data: RegisterIn,
    db: Session = Depends(get_db),
):
    return UserService(db).create_user(
        username=form_data.username,
        name=form_data.name,
        surname=form_data.surname,
        email=form_data.email,
        password=form_data.password,
    )
