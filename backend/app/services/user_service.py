from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.schemas.user import UserCreate


def create_user(db: Session, user_data: UserCreate) -> User:
    existing_user = db.scalar(
        select(User).where(
            (User.email == user_data.email)
            | (User.username == user_data.username)
        )
    )

    if existing_user:
        raise ValueError("Username or email already exists")

    user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hash_password(user_data.password),
        leetcode_username=user_data.leetcode_username,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user