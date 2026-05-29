import os
from crewai.tools import tool
# pyrefly: ignore [missing-import]
from serpapi import Client

@tool("Web Search Tool")
def web_search_tool(query: str) -> str:
    """Search the web for latest information, facts, news, and statistics."""
    normalized_query = query.lower().strip()
    try:
        serpapi_api_key = os.getenv("SERPAPI_API_KEY")
        if not serpapi_api_key:
            raise ValueError("SERPAPI_API_KEY environment variable is missing")

        client = Client(api_key=serpapi_api_key)
        data = client.search({
            "engine": "google",
            "q": normalized_query,
            "num": 5,
        })

        results = data.get("organic_results", [])
        if not results:
            return "No relevant search results found."

        return "\n\n".join(
            f"Title: {r.get('title')}\nBody: {r.get('snippet')}\nURL: {r.get('link')}"
            for r in results
        )

    except ValueError as e:
        raise RuntimeError(f"Web search configuration error: {str(e)}") from e
    except Exception as e:
        return f"Web search temporarily unavailable: {str(e)}"
