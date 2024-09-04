import logging

from app.models.user import User
from app.schema.user import UserCreate
from app.services.user_service import UserService
from sqlalchemy.orm import Session


def seed_users(db: Session, user_service: UserService) -> None:
    # Delete all users
    db.query(User).delete()
    # Create a list of test users
    test_users = [
        UserCreate(username="user1", email="user1@example.com", password="password1"),
        UserCreate(username="user2", email="user2@example.com", password="password2"),
        UserCreate(username="user3", email="user3@example.com", password="password3"),
    ]

    for user in test_users:
        existing_user = user_service.get_user_by_email(user.email)
        if not existing_user:
            user_service.create_user(user)
            logging.info(f"Created user: {user.username}")
        else:
            logging.info(f"User {user.username} already exists.")
