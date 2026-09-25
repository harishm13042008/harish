from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import (
    ensure_directories,
    get_settings,
)

from app.routes import router


settings = get_settings()

ensure_directories()


app = FastAPI(
    title=settings.app_name,

    description=(
        "AI comic story and "
        "illustration creator."
    ),

    version="1.0.0",
)


app.mount(
    "/static",
    StaticFiles(
        directory="static"
    ),
    name="static",
)


app.include_router(router)


@app.get("/health")
def health():

    return {
        "status": "ok",
        "demo_mode": settings.demo_mode,
        "image_provider": (
            settings.image_provider
        ),
    }