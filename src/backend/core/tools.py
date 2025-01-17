import httpx
from bs4 import BeautifulSoup as soup
from pydantic_ai import RunContext

from backend.core.consts import AI_MODEL
from backend.core.core import SwotAgentDeps, SwotAnalysis, swot_agent
from backend.core.utils import report_tool_usage
from backend.logger import logger


@swot_agent.tool(prepare=report_tool_usage)
async def fetch_website_content(
    _ctx: RunContext[SwotAgentDeps], url: str
) -> str:
    """
    Fetches the HTML content of the given URL via httpx and beautifulsoup

    :param _ctx: RunContext[SwotAgentDeps]
    :param url: str
    :return: str
    """
    logger.info(f"Fetching website content for: {url}")
    async with httpx.AsyncClient(follow_redirects=True) as http_client:
        try:
            response = await http_client.get(url)
            response.raise_for_status()
            html_content = response.text
            content = soup(html_content, "html.parser")
            text_content = content.get_text(separator=" ", strip=True)
            return text_content
        except httpx.HTTPError as e:
            logger.info(f"Request failed: {e}")
            raise


@swot_agent.tool(prepare=report_tool_usage)
async def analyze_competition(
    ctx: RunContext[SwotAgentDeps],
    product_name: str,
    product_description: str,
) -> str:
    """Analyzes the competition for the given product using the Gemini model."""
    logger.info(f"Analyzing competition for: {product_name}")

    prompt = f"""
    You are a competitive analysis expert. Analyze the competition for the following product:
    Product Name: {product_name}
    Product Description: {product_description}

    Provide a detailed analysis of:
    1. Key competitors and their market position
    2. Competitive advantages and disadvantages
    3. Market trends and potential disruptions
    4. Entry barriers and competitive pressures
    """

    if not ctx.deps.client:
        logger.info("Error: OpenAI client not initialized.")
        return ""
    try:
        response = await ctx.deps.client.aio.models.generate_content(
            model=AI_MODEL,
            contents=prompt,
        )
        return response.text
    except Exception as e:
        logger.error(f"Error analyzing competition: {e}")
        return f"Error analyzing competition: {e}"


@swot_agent.tool(prepare=report_tool_usage)
async def get_reddit_insights(
    ctx: RunContext[SwotAgentDeps], query: str, subreddit_name: str = "python"
):
    """
    A tool to gain insights from a subreddit. Data is returned as string
    with newlines

    :param ctx: RunContext[SwotAgentDeps]
    :param query: str
    :param subreddit_name: str
    :return: str
    """
    subreddit = ctx.deps.reddit.subreddit(subreddit_name)
    search_results = subreddit.search(query)

    insights = []
    for post in search_results:
        insights.append(
            f"Title: {post.title}\n"
            f"URL: {post.url}\n"
            f"Content: {post.selftext}\n"
        )

    return "\n".join(insights)


async def run_agent(
    url: str, deps: SwotAgentDeps = SwotAgentDeps()
) -> SwotAnalysis | Exception:
    """
    Runs the SWOT Analysis Agent

    :param url: str
    :param deps: SwotAgentDeps
    :return: SwotAnalysis | Exception
    """
    try:
        deps.tool_history = []
        result = await swot_agent.run(
            f"Perform a comprehensive SWOT analysis for this product: {url}",
            deps=deps,
        )
        logger.info(f"Agent Result: {result}")

        if deps.update_status_func:
            await deps.update_status_func(deps.request, "Analysis Complete")
    except Exception as e:
        logger.exception(f"Error during agent run: {type(e), e, e.args}")

        if deps.update_status_func:
            await deps.update_status_func(deps.request, f"Error: {e}")

        return e
