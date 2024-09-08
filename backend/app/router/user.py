from fastapi import APIRouter, Depends, HTTPException

from app.models.user import User
from app.schema.user import User, UserCreate
from app.services.user_service import UserService, get_user_service

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=User)
def create_user(
    user: UserCreate, user_service: UserService = Depends(get_user_service)
) -> User:
    db_user = user_service.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(user)


@router.get("/{user_id}", response_model=User)
def read_user(
    user_id: int, user_service: UserService = Depends(get_user_service)
) -> User:
    db_user = user_service.get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
