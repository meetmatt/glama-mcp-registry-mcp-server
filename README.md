# mcp-glama-registry

MCP Registry Server for Glama MCP
================================

This package provides an MCP server that exposes a tool to search the Glama MCP registry for MCP servers matching a query string.

## Installation

Install using [uv](https://github.com/astral-sh/uv):

```sh
uvx install mcp "mcp[cli]"
```

## Usage

You can run the server with:

```sh
python -m mcp_glama_registry
```

Or using MCP CLI:

```sh
mcp run mcp_glama_registry
```

Or directly with uv:

```sh
uv run main.py
```

## API

The server exposes a single tool:

- `search_mcp_servers(query: str) -> list`: Searches the Glama MCP registry for MCP servers matching the query string.

## Development & Testing

Install development dependencies:

```sh
uvx install -r requirements-dev.txt
```

Run tests with [pytest](https://pytest.org/):

```sh
pytest
```

## License

MIT 