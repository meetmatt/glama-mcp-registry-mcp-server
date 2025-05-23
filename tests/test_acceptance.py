import pytest
from mcp_glama_registry import search_mcp_servers

@pytest.mark.asyncio
async def test_search_mcp_servers_returns_list():
    result = await search_mcp_servers("telegram")
    assert isinstance(result, list) 