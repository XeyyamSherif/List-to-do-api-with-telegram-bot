import uvicorn

from api.user import user_router
from app.server import app
from models.user import User

app.include_router(user_router)

def main():
    uvicorn.run(
        app="app.server:app",
        reload=True
    )


if __name__ == "__main__":
    main()
