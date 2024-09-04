import logging
from hashlib import sha256

from app.core.database import get_db
from app.models.user import User
from app.schema.user import UserCreate
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session


class UserService:
    def __init__(self) -> None:
        pass

    def get_user(db: Session, user_id: int) -> User | None:
        try:
            return db.query(User).filter(User.id == user_id).first()
        except Exception as e:
            logging.exception("Oops! An error occurred.", e)
            raise HTTPException(status_code=500)

    def get_user_by_email(db: Session, email: str) -> User | None:
        try:
            return db.query(User).filter(User.email == email).first()
        except Exception as e:
            logging.exception("Oops! An error occurred.", e)
            raise HTTPException(status_code=500)

    def create_user(db: Session, user: UserCreate) -> User:
        try:
            hashed_password = sha256(user.password.encode("utf-8")).hexdigest()
            db_user = User(
                username=user.username,
                email=user.email,
                hashed_password=hashed_password,
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except Exception as e:
            logging.exception("Oops! An error occurred.", e)
            raise HTTPException(status_code=500)


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)
