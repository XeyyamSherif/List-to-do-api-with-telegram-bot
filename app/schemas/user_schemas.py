from pydantic import BaseModel, Field


class SignUp(BaseModel):
    first_name: str = Field(..., description="first_name")
    mail: str = Field(..., description="mail")
    password: str = Field(..., description="password")
