# tools/web_search_tool.py

# ✅ Handle both new and old LangChain versions
try:
    from langchain_community.tools import DuckDuckGoSearchRun
except ImportError:
    try:
        from langchain.tools import DuckDuckGoSearchRun
    except ImportError:
        DuckDuckGoSearchRun = None  # fallback if unavailable

from utils.guardrails import validate_input, filter_output


def web_search(query: str) -> str:
    """Performs a quick web search using DuckDuckGo with safety guardrails."""
    if not validate_input(query):
        return "❌ Invalid query input."

    if DuckDuckGoSearchRun is None:
        return "⚠️ Web search tool unavailable (missing langchain_community or langchain)."

    try:
        search = DuckDuckGoSearchRun()
        result = search.run(query)
        return filter_output(result)
    except Exception as e:
        return f"⚠️ Web search failed: {str(e)}"
