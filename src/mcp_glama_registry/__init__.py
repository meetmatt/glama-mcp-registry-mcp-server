from mcp.server.fastmcp import FastMCP
import httpx

mcp = FastMCP("MCP Registry Search Server")

@mcp.tool()
async def search_mcp_servers(query: str) -> list:
    """
    Search the Glama MCP registry for MCP servers matching the query string.
    Args:
        query (str): Search keywords (e.g., 'telegram', 'docker')
    Returns:
        list: List of MCP servers (dicts) matching the query
    """
    url = f"https://glama.ai/api/mcp/v1/servers?query={query}"
    async with httpx.AsyncClient(timeout=10) as client:
        resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and "servers" in data:
            return data["servers"]
        return []

def main():
    mcp.run(transport="stdio") 