from fastapi import FastAPI

from app.database import create_tables


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Note"
    )
    return app_


app = create_app()


@app.on_event("startup")
async def startup():
    create_tables()