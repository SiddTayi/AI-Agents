#from crewai_tools import WebsiteSearchTool, ScrapeWebsiteTool
from crewai.tools import tool
from typing import Any, Dict, List, Optional, Union
from langchain_community.tools import DuckDuckGoSearchResults, TavilySearchResults


@tool
def travel_search_ddc(query: str) -> str:
    """
    Search for travel-related information using DuckDuckGo or Tavily.
    """
    search_tool_ddc = DuckDuckGoSearchResults(num_results=5)
    return search_tool_ddc.run(query)

@tool
def travel_search_tavily(query: str) -> str:
    """
    Search for travel-related information using Tavily.
    """
    search_tool_tavily = TavilySearchResults(num_results=5, search_depth = 'basic')
    return search_tool_tavily.invoke(query)

