from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    email:str
    password:str

class TaskCreate(BaseModel):
    title: str

class TaskResponse(BaseModel):
    id : int
    title:str
    complete: bool

    class Config:
        orm_mode = True
