from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.schemas.user_schemas import SignUp
from controllers.user import UserController

user_router = APIRouter()


@user_router.post("/sign_up", tags=["Users"])
async def sign_up(request: SignUp):
    await UserController().create_user(**request.dict())
    return ""
