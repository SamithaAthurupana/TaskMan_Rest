from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    tasks = relationship("Task", back_populates="owner")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="tasks")

# I built a FastAPI-based task management system with JWT authentication.
# The architecture follows a layered approach: routers handle HTTP logic, services contain business logic, and CRUD manages database interactions.
# Authentication is stateless using JWT, and endpoints are protected using dependency injection.
# The database layer uses SQLAlchemy ORM with proper indexing and relationships. The project includes structured modules and unit testing.