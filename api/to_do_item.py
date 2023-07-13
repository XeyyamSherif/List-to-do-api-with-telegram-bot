from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.schemas.to_do_schemas import CreateItem
from controllers.to_do_item import ToDoController

to_do_router = APIRouter()


@to_do_router.post("/create_user", tags=["To_do"])
async def sign_up(request: CreateItem):
    item = await ToDoController().create_item(request.dict())
    return ""
