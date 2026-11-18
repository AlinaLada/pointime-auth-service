from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from uuid import uuid4

from app.database import get_db
from app.models import User
from app.schemas import UserRegister
from app.auth import (
    hash_password,
    verify_password
)

router = APIRouter()


@router.post("/register")
def register(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        return {
            "error": "Email already exists"
        }

    new_user = User(
        id=uuid4(),
        email=user.email,
        username=user.username,
        password_hash=hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    return {
        "message": "User created"
    }

from app.schemas import UserLogin


@router.post("/login")
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not existing_user:
        return {
            "error": "User not found"
        }

    if not verify_password(
        user.password,
        existing_user.password_hash
    ):
        return {
            "error": "Invalid password"
        }

    return {
        "message": "Login successful"
    }