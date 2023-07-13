import datetime

from pydantic import BaseModel, Field


class CreateItem(BaseModel):
    content: str = Field(..., description="first_name")
    created_at: datetime.datetime = Field(..., description="datetime")