import uvicorn

from api.to_do_item import to_do_router
from api.user import user_router
from app.server import app

app.include_router(user_router)
app.include_router(to_do_router)


def main():
    uvicorn.run(
        app="app.server:app",
        reload=True
    )


if __name__ == "__main__":
    main()
