import json
import sys
from .tools.registry import tool_registry
from .tools.uploader_tool import UploaderTool
from .tools.connector_tool import ConnectorTool
from .tools.filesystem_tool import FileSystemTool
from .timekeeper import TimeKeeperClient

def register_all_tools():
    """
    Registers all the available tools with the tool registry.
    """
    timekeeper = TimeKeeperClient()
    tool_registry.register(UploaderTool(timekeeper))
    tool_registry.register(ConnectorTool())
    tool_registry.register(FileSystemTool())
    print("All tools registered.")

def process_command(line: str) -> dict:
    """
    Parses and processes a single JSON command string.
    """
    try:
        command = json.loads(line)
        tool_name = command.get("tool")
        action_name = command.get("action")
        args = command.get("args", {})

        if not tool_name or not action_name:
            raise ValueError("Command must include 'tool' and 'action'.")

        tool = tool_registry.get_tool(tool_name)
        if not tool:
            raise ValueError(f"Tool '{tool_name}' not found.")

        action = tool.actions.get(action_name)
        if not action:
            raise ValueError(f"Action '{action_name}' not found for tool '{tool_name}'.")

        result = action(**args)

        response = {"status": "success", "result": result}

    except json.JSONDecodeError:
        response = {"status": "error", "message": "Invalid JSON command."}
    except Exception as e:
        response = {"status": "error", "message": str(e)}

    return response

def main():
    """
    The main entry point for the TimeKeeper Boost MCP server.
    It listens for JSON commands on stdin and prints JSON responses to stdout.
    """
    register_all_tools()
    print("TimeKeeper Boost MCP Server is running. Waiting for commands...")

    for line in sys.stdin:
        response = process_command(line)
        print(json.dumps(response), flush=True)

if __name__ == "__main__":
    main()
