from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import schemas, crud
from backend.auth import get_current_user
from backend import models
from fastapi import status
from backend.services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Why not call CRUD directly from router?
# Because router handles HTTP logic, service handles business logic, and CRUD handles database logic. This separation improves maintainability and testing.
@router.post("/")
def create_task(task: schemas.TaskCreate,db: Session = Depends(get_db),current_user: models.User = Depends(get_current_user)):
    return task_service.create_user_task(db,task.title,current_user.id)

# Why use response_model?
# Response models enforce output validation, hide internal fields, and ensure API contract consistency.
@router.get("/", response_model=List[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db),
              current_user: models.User = Depends(get_current_user)):
    return db.query(models.Task).filter(models.Task.owner_id == current_user.id).all()