import pytest
import json
from unittest.mock import patch
from app.main import process_command, register_all_tools
from app.tools.registry import tool_registry

# --- MCP Server Tests ---

@pytest.fixture(autouse=True)
def setup_and_teardown_registry():
    """Clear the registry and re-register tools before each test."""
    tool_registry._tools = {}
    # We need to register tools to test the dispatcher
    register_all_tools()
    yield
    tool_registry._tools = {}

def test_mcp_server_success():
    """
    Tests a successful command dispatch through the process_command function.
    """
    # 1. Arrange
    # The FileSystemTool is registered by the fixture
    command = {"tool": "filesystem", "action": "list", "args": {"path": "."}}
    command_json = json.dumps(command)

    # 2. Act
    response = process_command(command_json)

    # 3. Assert
    assert response["status"] == "success"
    assert "pyproject.toml" in response["result"]
    assert "app" in response["result"]

def test_mcp_server_tool_not_found():
    """
    Tests the error handling when a tool is not found.
    """
    # 1. Arrange
    command = {"tool": "non_existent_tool", "action": "do_something", "args": {}}
    command_json = json.dumps(command)

    # 2. Act
    response = process_command(command_json)

    # 3. Assert
    assert response["status"] == "error"
    assert "Tool 'non_existent_tool' not found" in response["message"]

def test_mcp_server_action_not_found():
    """
    Tests the error handling when an action is not found for a tool.
    """
    # 1. Arrange
    command = {"tool": "filesystem", "action": "non_existent_action", "args": {}}
    command_json = json.dumps(command)

    # 2. Act
    response = process_command(command_json)

    # 3. Assert
    assert response["status"] == "error"
    assert "Action 'non_existent_action' not found" in response["message"]

def test_mcp_server_invalid_json():
    """
    Tests the error handling for an invalid JSON command.
    """
    # 1. Arrange
    command_json = "this is not json"

    # 2. Act
    response = process_command(command_json)

    # 3. Assert
    assert response["status"] == "error"
    assert "Invalid JSON command" in response["message"]
