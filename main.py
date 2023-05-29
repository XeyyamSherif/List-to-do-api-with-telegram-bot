import uvicorn


def main():
    uvicorn.run(
        app="app.server:app",
        reload=True
    )


if __name__ == "__main__":
    main()
