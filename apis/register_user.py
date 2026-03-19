from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from password_hashing import hash_password
from models.user import User
from database_connection import get_db
from pydantic import BaseModel

router = APIRouter(prefix="/user")


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    hashed = hash_password(user.password)

    user = User(username=user.username, email=user.email, password=hashed)
    db.add(user)
    db.commit()

    return {"message": "User created"}
