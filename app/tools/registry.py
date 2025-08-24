from __future__ import annotations
from typing import Any, Callable

class Tool:
    """Base class for all tools."""
    name: str
    actions: dict[str, Callable[..., Any]]

    def __init__(self):
        self.actions = {}

class ToolRegistry:
    """A registry for all available tools for the MCP server."""

    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool):
        """Registers a tool."""
        if tool.name in self._tools:
            raise ValueError(f"Tool with name '{tool.name}' is already registered.")
        self._tools[tool.name] = tool
        print(f"Registered tool: {tool.name}")

    def get_tool(self, tool_name: str) -> Tool | None:
        """Retrieves a tool by its name."""
        return self._tools.get(tool_name)

    def list_tools(self) -> list[str]:
        """Returns a list of the names of all registered tools."""
        return list(self._tools.keys())

# A global instance of the registry
tool_registry = ToolRegistry()
