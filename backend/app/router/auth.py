from datetime import timedelta
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.models.user import User
from app.schema import user
from app.schema.auth import Token
from app.services.auth_service import AuthService, get_auth_service

# Create the router
auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service),
) -> Token:
    user: User | Literal[False] = auth_service.authenticate_user(
        form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth_service.access_token_expire_minutes)
    access_token = auth_service.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


# @auth_router.get("/me", response_model=user)
# async def get_current_user_profile(
#     auth_service: AuthService = Depends(get_auth_service),
#     current_user: User = Depends(lambda: auth_service.get_current_user),
# ):
#     """
#     Retrieve the profile of the currently authenticated user.
#     """
#     return current_user
