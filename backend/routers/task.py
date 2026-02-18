from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend import schemas, crud
from backend.auth import get_current_user
from backend import models

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/")
def create_task(task: schemas.TaskCreate,
                db: Session = Depends(get_db),
                current_user: models.User = Depends(get_current_user)):
    return crud.create_task(db, task.title, current_user.id)


@router.get("/")
def get_tasks(db: Session = Depends(get_db),
              current_user: models.User = Depends(get_current_user)):
    return db.query(models.Task).filter(
        models.Task.owner_id == current_user.id
    ).all()