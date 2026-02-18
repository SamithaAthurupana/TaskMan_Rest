from sqlalchemy.orm import Session
from passlib.hash import bcrypt
from backend import models
from backend.auth import hash_password

def create_user(db, email, password):
    hashed_password = hash_password(password)
    user = models.User(email=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_task(db: Session, title:str, user_id: int):
    db_task = models.Task(title, owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task