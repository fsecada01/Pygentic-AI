import os

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from backend import create_app
from backend.logger import logger
from backend.settings import app_settings, debug_arg

app = create_app(debug=debug_arg, settings_obj=app_settings)

# app.logger = CustomizeLogger.make_logger(config_path)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    exc_str = f"{exc}".replace("\n", "; ").replace("  ", " ")
    logger.error(f"{request}: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}

    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Oops! {exc.name} did something. "
            "There goes a rainbow..."
        },
    )


app.mount(
    "/static",
    StaticFiles(directory=os.path.join(app_settings.frontend_dir, "static")),
    name="static",
)
