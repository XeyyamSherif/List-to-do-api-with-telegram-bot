from fastapi import FastAPI

from app.database import create_tables
from pythondi import Provider

from controllers.to_do_item import ToDoController
from controllers.user import UserController
from pythondi import configure, configure_after_clear

from repositories.user_repo import UserRepository


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Note"
    )
    return app_


app = create_app()


@app.on_event("startup")
async def startup():
    create_tables()
