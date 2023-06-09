from typing import Any

from pydantic import BaseModel


class BaseResponseSchema(BaseModel):
    success = True
    message: Any
    status: int = 200
    data: Any
    error_code: str = "no error"
