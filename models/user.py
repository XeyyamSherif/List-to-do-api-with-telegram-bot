from sqlalchemy.types import Integer, DateTime, String
from sqlalchemy.schema import Column

from app.database import Base


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    username = Column(String(100), unique=True, index=True)
    password = Column(String(50), index=True)

