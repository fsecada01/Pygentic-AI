import asyncio
import os
import random
import time
from typing import Any

from fastapi import APIRouter, Form, Request
from jinjax import Catalog, JinjaX
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from backend.core.core import SwotAnalysis
from backend.logger import logger
from backend.settings import app_settings
from backend.site.consts import (
    ANALYSIS_COMPLETE_MESSAGE,
    ANALYZING_MESSAGE,
    result_store,
    status_store,
)

user_frontend = APIRouter(prefix="", tags=["frontend"])
frontend = app_settings.frontend_dir

templates = Jinja2Templates(directory=os.path.join(frontend, "templates"))
templates.env.add_extension(JinjaX)
catalog = Catalog(jinja_env=templates.env)
list(
    map(
        lambda folder: catalog.add_folder(
            os.path.join(frontend, "components", folder)  # noqa
        ),
        ("main", "forms", "snippets"),
    )
)

user_frontend.mount(
    "/static",
    StaticFiles(directory=os.path.join(frontend, "static")),
    name="static",
)


def run_agent_with_progress(session_id, url):
    pass


@user_frontend.post("analyze", response_class=HTMLResponse)
async def analyze_url(request: Request, url: str = Form(...)) -> HTMLResponse:
    """
    Analyze a given URL using SWOT analysis agent
    :param request:
    :param url:
    :return:
    """
    running_tasks = set()
    session_id = str(id(request))
    request.session["analysis_id"] = session_id
    request.session["start_time"] = asyncio.get_event_loop().time()

    # Clearing out the status store for the analysis ID session
    status_store[session_id] = []

    status_store[session_id].append(ANALYZING_MESSAGE)

    logger.info(f"Starting new analysis with session ID: {session_id}")

    task = asyncio.create_task(run_agent_with_progress(session_id, url))
    running_tasks.add(task)
    task.add_done_callback(running_tasks.discard)

    return templates.TemplateResponse(
        "status.html",
        context={
            "request": request,
            "messages": [ANALYZING_MESSAGE],
            "result": False,
        },
    )


@user_frontend.get("/status", response_class=HTMLResponse)
async def get_status(request: Request):
    """
    Returns the current status messages
    :param request:
    :return:
    """
    context = {"request": request, "messages": [], "result": False}
    session_id = request.session.get("analysis_id")
    if session_id:
        messages = status_store.get(session_id, [])
        result = ANALYSIS_COMPLETE_MESSAGE in messages
        logger.info(
            f"Status check - Session ID: {'session_id'}, Messages: "
            f"{messages}"
        )

        context.update({"messages": messages, "result": result})

    return templates.TemplateResponse("status.html", context=context)


@user_frontend.get("/result", response_class=HTMLResponse)
async def get_result(request: Request) -> HTMLResponse:
    """
    Returns the SWOT analysis result from the existing session ID.

    :param request: Request
    :return: HTMLResponse
    """
    session_id = request.session.get("analysis_id")

    if session_id and session_id in result_store:
        result = result_store[session_id]
    else:
        result = None

    return templates.TemplateResponse(
        "result.html",
        {"request": request, "result": result},
    )


def emulate_tool_completion(session_id: str, message: str) -> None:
    """Pydantic AI doesn't provide a post-processing hook, so we need to emulate one."""

    # Sleep a random amount of time between 0 and 5 seconds
    time.sleep(random.randint(0, 5))
    status_store[session_id].append(message)


async def update_status(session_id: str, message: Any) -> None:
    """Updates status messages and handles SWOT analysis results."""
    logger.info(f"Updating status for session {session_id}: {message}")

    # Handle SWOT analysis result
    if isinstance(message, SwotAnalysis):
        result_store[session_id] = message.model_dump()
        status_store[session_id].append(ANALYSIS_COMPLETE_MESSAGE)
        return

    # Handle string messages
    if isinstance(message, str):
        # Instantly store first status message, emulate tool completion for others
        if message == ANALYSIS_COMPLETE_MESSAGE:
            status_store[session_id].append(message)
        else:
            loop = asyncio.get_running_loop()
            await loop.run_in_executor(
                None, emulate_tool_completion, session_id, message
            )

    logger.info(
        f"Status messages for session {session_id}: {status_store[session_id]}"
    )
