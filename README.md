# MCP Registry Server for Glama MCP

This package provides an MCP server that exposes a tool to search the Glama MCP registry for MCP servers matching a query string.  
See [Glama.ai MCP Registry](https://glama.ai/mcp/servers) for additional information.

## Installation

Install using [uv](https://github.com/astral-sh/uv):

```sh
uv sync
```

## Usage

```json
{
  "mcpServers": {
    "glama-registry": {
      "command": "uvx",
      "args": [
        "mcp-glama-registry"
      ]
    }
  }
}
```

## API

The server exposes a single tool:

- `search_mcp_servers(query: str) -> list`: Searches the Glama MCP registry for MCP servers matching the query string.

## Development & Testing

Install development dependencies:

```sh
uv sync --all-groups
```

Run tests with [pytest](https://pytest.org/):

```sh
uv run pytest
```

See `tests/test_acceptance.py` for an example of how to use the API in code.

## License

MIT
