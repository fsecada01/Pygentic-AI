import os

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import HTMLResponse, JSONResponse
from starlette.staticfiles import StaticFiles

from backend import create_app
from backend.logger import logger
from backend.settings import app_settings, debug_arg
from backend.site.router import templates, user_frontend
from backend.utils import get_val

app = create_app(debug=debug_arg, settings_obj=app_settings)

# app.logger = CustomizeLogger.make_logger(config_path)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    """
    Custom validation error messaging for end-users. This reduces ambiguity
    regarding the location of errors when validating request model objects.

    :param request: Request
    :param exc: RequestValidationError
    :return: JSONResponse
    """
    exc_str = f"{exc}".replace("\n", "; ").replace("  ", " ")
    logger.error(f"{request}: {exc_str}")
    content = {"status_code": 10422, "message": exc_str, "data": None}

    return JSONResponse(
        content=content,
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    )


class UnicornException(Exception):
    """
    Inherited from Exception to provide the proper name for the error being
    raised.
    """

    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    """
    Returns a JSON response with a 418 response code instead of a default
    500. This provides some greater information for APIs/end-users.

    :param request: Request
    :param exc: UnicornException
    :return: JSONResponse
    """
    return JSONResponse(
        status_code=418,
        content={
            "message": f"Oops! {exc.name} did something. "
            "There goes a rainbow...",
        },
    )


app.mount(
    "/static",
    StaticFiles(directory=os.path.join(app_settings.frontend_dir, "static")),
    name="static",
)

app.add_middleware(
    SessionMiddleware,
    secret_key=get_val("SECRET_KEY"),
    max_age=get_val("MAX_AGE", 3600),
    same_site="lax",
    https_only=get_val("HTTPS_ONLY", False),
)

app.include_router(user_frontend)


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request) -> HTMLResponse:
    """
    default homepage for the web application
    :param request:
    :return: HTMLResponse
    """
    return templates.TemplateResponse("home.html", {"request": request})


if app_settings.DEBUG in (True, "True"):
    from debug_toolbar.middleware import DebugToolbarMiddleware
    from debug_toolbar.panels.sqlalchemy import SQLAlchemyPanel

    from backend.db.db import engine

    logger.debug(f"App Debug settings flag is {app_settings.DEBUG}")

    class SQLAModelPanel(SQLAlchemyPanel):
        """
        Inheriting from SQLAlchemyPanel to include the sync engine object
        from the SQLModel async engine instance.
        """

        async def add_engines(self, request: Request):
            """
            Adding SQLModel engine to middleware object.
            :param request: Request
            :return:
            """
            self.engines.add(engine.sync_engine)

    app.add_middleware(
        DebugToolbarMiddleware,
        panels=["app.SQLAModelPanel"],
        disable_panels=["debug_toolbar.panels.profiling.ProfilingPanel"],
    )


if __name__ == "__main__":
    import uvicorn

    if debug_arg:
        uvicorn.run("app:app", port=5000, reload=True)
    else:
        uvicorn.run(
            "app:app",
            host="0.0.0.0",
            port=get_val("APP_PORT", 5000),
            workers=get_val("WORKERS", 1),
        )
