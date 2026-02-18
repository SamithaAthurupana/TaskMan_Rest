from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import schemas, crud, models
from backend.auth import create_access_token, verify_password
from fastapi import status

router = APIRouter(prefix="/users", tags=["Users"])

# How do you handle validation errors?
# FastAPI automatically validates request body using Pydantic. For business-level validation, I raise HTTPException with appropriate status codes.
@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400,detail="Email already registered")
    return crud.create_user(db, user.email, user.password)

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token,"token_type": "bearer"}