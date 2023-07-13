from datetime import datetime

from sqlalchemy.types import Integer, DateTime, String
from sqlalchemy.schema import Column

from app.database import Base


class ToDo(Base):
    __tablename__ = "ToDo"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(250), index=True)
    created_at = Column(DateTime, default=datetime.utcnow)



