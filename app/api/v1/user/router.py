from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.v1.dependencies import get_current_active_user
from app.api.v1.user.serializer import UserDetailOut
from app.core.models import User
from app.core.schemas import IResponseBase
from app.db.database import get_db
from app.services.user import UserService

router = APIRouter()


@router.get("/", response_model=IResponseBase[UserDetailOut])
def get_current_user_detail(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)
):
    user = UserService(db).encode_user_detail(current_user)
    return IResponseBase[UserDetailOut](data=user)
