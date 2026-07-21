from fastapi import FastAPI

from .routes import router

from .config import PROJECT_NAME, VERSION

app = FastAPI(
    title=PROJECT_NAME,
    version=VERSION
)

app.include_router(router)