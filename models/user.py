from sqlalchemy import Column, Integer, DateTime, String
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    username = Column(String(100), unique=True, index=True)
    password = Column(String(50), index=True)
