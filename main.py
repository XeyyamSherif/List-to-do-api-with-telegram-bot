import uvicorn
from models.user import User


def main():
    uvicorn.run(
        app="app.server:app",
        reload=True
    )


if __name__ == "__main__":

    main()
