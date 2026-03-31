import requests
from agentscope.service import ServiceResponse

def web_search(query: str) -> ServiceResponse:
    """
    Searches the web for technical information.
    Note: Requires a search engine API. This is a placeholder that 
    simulates a technical lookup for the PM.
    """
    # In a real scenario, you'd use Tavily, Google, or DuckDuckGo here.
    # We simulate a response to show how the PM uses it.
    simulated_results = {
        "requests": "Latest version is 2.31.0. Supports python 3.7+.",
        "pandas": "Latest stable is 2.2.1. Optimized for memory-efficient dataframes.",
        "bitcoin price": "Simulated technical lookup: Current price around $65,000 USD."
    }
    
    # Try to find a match or return a generic tech response
    result = simulated_results.get(query.lower(), f"Technical lookup for '{query}': Found 10+ relevant documentation pages. Recommended library: standard python libs.")
    
    return ServiceResponse(
        status=ServiceResponse.SUCCESS,
        content=result
    )
