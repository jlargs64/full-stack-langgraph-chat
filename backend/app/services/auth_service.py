from datetime import datetime, timedelta
from typing import Literal

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.settings import Settings, get_settings
from app.models.user import User
from app.schema.auth import TokenData
from app.services.user_service import UserService, get_user_service


class AuthService:
    # Password hashing
    pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

    # OAuth2 password bearer scheme
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

    def __init__(self, user_service: UserService, settings: Settings) -> None:
        self.user_service = user_service
        self.SECRET_KEY = settings.auth_secret_key
        self.ALGORITHM = settings.auth_algorithm
        self.ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

    def create_access_token(
        self, data: dict, expires_delta: timedelta | None = None
    ) -> str:
        to_encode = data.copy()
        expire = datetime.now() + (
            expires_delta
            if expires_delta
            else timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    def verify_password(self, plain_password, hashed_password) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password) -> str:
        return self.pwd_context.hash(password)

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
            token_data = TokenData(email=email)
        except JWTError:
            raise credentials_exception

        user = self.user_service.get_user_by_email(username=token_data.email)
        if user is None:
            raise credentials_exception
        return user

    def authenticate_user(self, email: str, password: str) -> User | Literal[False]:
        user = self.user_service.get_user_by_email(email)
        if not user or not self.verify_password(password, user.hashed_password):
            return False
        return user


def get_auth_service(
    user_service: UserService = Depends(get_user_service),
    settings: Settings = Depends(get_settings),
) -> UserService:
    return AuthService(user_service=user_service, settings=settings)
