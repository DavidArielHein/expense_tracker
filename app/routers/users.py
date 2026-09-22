from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db
from .. import schemas
from ..crud import users

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/login', response_model=schemas.UserResponse)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    new_user = users.create_user(user, db)
    return new_user