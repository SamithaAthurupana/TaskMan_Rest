from fastapi import FastAPI
from backend import models
from backend import database
from backend.database import engine
from backend.routers import user
from backend.routers import task
from backend.services import task_service


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)


@app.get("/")
def root():
    return {"message": "Task API Running"}

