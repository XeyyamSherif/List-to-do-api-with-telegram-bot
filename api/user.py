from fastapi import APIRouter

from app.schemas.user_schemas import SignUp

user_router = APIRouter()


@user_router.post("/sign_up", tags=["Users"])
async def sign_up(request: SignUp):
    print(request)
    return ""
