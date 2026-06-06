import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User

router = APIRouter(prefix="/auth", tags=["auth"])

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Username not found.")
    if verify_password(password, db_user.password):
        return {"message": "Login successful."}
    else:
        raise HTTPException(status_code=401, detail="Password incorrect.")