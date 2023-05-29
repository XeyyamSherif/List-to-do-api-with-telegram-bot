from fastapi import FastAPI


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Social Network"
    )
    return app_


app = create_app()

