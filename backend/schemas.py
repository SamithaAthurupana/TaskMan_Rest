from typing import Optional
from pydantic import BaseModel
from typing import List

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
        from_attributes = True   # (Pydantic v2)
        # If using Pydantic v1, use:
        # orm_mode = True