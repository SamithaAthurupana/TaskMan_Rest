from sqlalchemy.orm import Session
from backend import crud

# Better design:
    # Router → Service → CRUD → DB
def create_user_task(db: Session, title: str, user_id: int):
    return crud.create_task(db, title, user_id)

def get_user_tasks(db: Session, user_id: int):
    return crud.get_tasks_by_user(db, user_id)