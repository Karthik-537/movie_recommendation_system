from fastapi import Depends, APIRouter
from models.user import User
from password_hashing import verify_password
from database_connection import get_db
from sqlalchemy.orm import Session
from jwt.create_jwt_token import create_token

router = APIRouter(prefix="/auth")


@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user or not verify_password(password, user.password):
        return {"error": "Invalid credentials"}

    token = create_token({"sub": user.username})

    return {"access_token": token}
