import asyncio
from mcp.server.fastmcp import FastMCP
from agents import run_research

# Create FastMCP instance
mcp = FastMCP("crew_research")

@mcp.tool()
async def crew_research(query: str) -> str:
    """Run CrewAI-based research system for given user query. Can do both standard and deep web search.

    Args:
        query (str): The research query or question.

    Returns:
        str: The research response from the CrewAI pipeline.
    """
    return run_research(query)


# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")


# add this inside ./.cursor/mcp.json
# {
#   "mcpServers": {
#     "crew_research": {
#       "command": "uv",
#       "args": [
#         "--directory",
#         "\Users\neeraj kumar\ai-engineering-hub\Multi-Agent-deep-researcher-mcp-windows-linux>",
#         "run",
#         "server.py"
#       ],
#       "env": {
#         "LINKUP_API_KEY": "4dc1e667-2e63-4b0c-9f25-cd89a4dad"
#       }
#     }
#   }
# }
