from pydantic_ai import RunContext
from pydantic_ai.tools import ToolDefinition

from backend.core.core import SwotAgentDeps


async def report_tool_usage(
    ctx: RunContext[SwotAgentDeps],
    tool_def: ToolDefinition,
) -> ToolDefinition:
    """
    Reports tool usage + results to an update function
    :param ctx: RunContext[SwotAgentDeps]
    :param tool_def: ToolDefinition
    :return:
    """
    if tool_def.name in ctx.deps.tool_history:
        return tool_def

    if ctx.deps.update_status_func:
        await ctx.deps.update_status_func(
            ctx.deps.request,
            f"Using tool: {tool_def.name}...",
        )
        ctx.deps.tool_history.append(tool_def.name)

    return tool_def
