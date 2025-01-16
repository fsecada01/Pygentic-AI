from collections.abc import Callable
from typing import Any

from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

from backend.core.consts import AI_MODEL, default_system_prompt
from backend.db.base import Base
from backend.utils import get_val


class SwotAnalysis(Base):
    """SQLModel for SWOT Analysis Response Object"""

    strengths: list[str]
    weaknesses: list[str]
    opportunities: list[str]
    threats: list[str]
    analysis: str


class SwotAgentDeps(Base):
    """Agent Dependencies for SWOT Analysis"""

    request: Any | None = None
    update_status_func: Callable | None = None
    tool_history: list[str]


swot_agent = Agent(
    OpenAIModel(model_name=AI_MODEL, api_key=get_val("OPENAI_API_KEY")),
    deps_type=SwotAgentDeps,
    result_type=SwotAnalysis,
    system_prompt=default_system_prompt,
    retries=5,
)
