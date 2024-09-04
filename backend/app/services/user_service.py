import logging

from app.core.database import get_db
from app.models.user import User
from app.schema.user import UserCreate
from argon2 import PasswordHasher, exceptions
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session


class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.password_hasher = PasswordHasher()

    def get_user(self, user_id: int) -> User | None:
        try:
            return self.db.query(User).filter(User.id == user_id).first()
        except Exception as e:
            logging.exception("Oops! An error occurred.", exc_info=e)

            raise HTTPException(status_code=500)

    def get_user_by_email(self, email: str) -> User | None:
        try:
            return self.db.query(User).filter(User.email == email).first()
        except Exception as e:
            logging.exception("Oops! An error occurred.", exc_info=e)

            raise HTTPException(status_code=500)

    def create_user(self, user: UserCreate) -> User:
        try:
            hashed_password = self.password_hasher.hash(user.password)
            db_user = User(
                username=user.username,
                email=user.email,
                hashed_password=hashed_password,
            )
            self.db.add(db_user)
            self.db.commit()
            self.db.refresh(db_user)
            return db_user
        except Exception as e:
            logging.exception("Oops! An error occurred.", exc_info=e)

            raise HTTPException(status_code=500)

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        try:
            self.password_hasher.verify(hashed_password, plain_password)
            return True
        except exceptions.VerifyMismatchError:
            return False


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)
