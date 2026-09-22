from fastapi import HTTPException, status

from sqlalchemy import select
from sqlalchemy.orm import Session
from pwdlib import PasswordHash

from .. import schemas, models

password_hash = PasswordHash.recommended()
DUMMY_HASH = password_hash.hash('dummypassword')


def create_user(user: schemas.UserCreate, db: Session):
    # Verify if the user already exists
    stmt = select(models.UserDB).where(models.UserDB.email == user.email)
    user_db = db.scalar(stmt)
    
    if(user_db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Email already registered'
        )
    
    # Add user to DB
    user_password = password_hash.hash(user.password)
    
    new_user = models.UserDB(
        username=user.username,
        email=user.email,
        hashed_password=user_password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)