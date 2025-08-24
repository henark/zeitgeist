import pytest
import os
import json
from unittest.mock import MagicMock, patch, AsyncMock
from app.tools.filesystem_tool import FileSystemTool
from app.tools.documentation_tool import DocumentationTool
from app.tools.connector_tool import ConnectorTool
from app.tools.uploader_tool import UploaderTool
from app.timekeeper import TimeKeeperClient

# --- Fixtures ---

@pytest.fixture
def fs_tool() -> FileSystemTool:
    return FileSystemTool()

@pytest.fixture
def doc_tool() -> DocumentationTool:
    return DocumentationTool()

@pytest.fixture
def uploader_tool() -> UploaderTool:
    mock_timekeeper = MagicMock(spec=TimeKeeperClient)
    return UploaderTool(timekeeper=mock_timekeeper)

@pytest.fixture
def connector_tool() -> ConnectorTool:
    return ConnectorTool()

@pytest.fixture
def temp_file(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("hello world")
    # Return the path relative to the base directory for the tool
    return os.path.relpath(p, os.getcwd())

# --- FileSystemTool Tests ---

def test_fs_tool_list_files(fs_tool: FileSystemTool):
    # Should be able to list the current directory
    files = fs_tool.list(".")
    assert "pyproject.toml" in files
    assert "app" in files

def test_fs_tool_read_write_cycle(fs_tool: FileSystemTool):
    path = "test_write_file.txt"
    content = "This is a test."

    # Write the file
    write_result = fs_tool.write(path, content)
    assert "Successfully wrote" in write_result

    # Read the file
    read_content = fs_tool.read(path)
    assert read_content == content

    # Cleanup
    os.remove(path)

def test_fs_tool_path_safety(fs_tool: FileSystemTool):
    # Test that accessing paths outside the project directory is denied
    with pytest.raises(PermissionError):
        fs_tool.read("/etc/passwd")

    with pytest.raises(PermissionError):
        fs_tool.list("../../../")

    with pytest.raises(PermissionError):
        fs_tool.write("/tmp/test.txt", "danger")

# --- DocumentationTool Tests ---

def test_doc_tool_search(doc_tool: DocumentationTool, tmp_path):
    # Create a dummy docs directory and file using pytest's tmp_path fixture
    docs_dir = tmp_path / "docs"
    docs_dir.mkdir()
    doc_file = docs_dir / "test_doc.md"
    doc_content = "This is a test of the documentation search tool.\nIt should find the keyword 'Litestar'."
    doc_file.write_text(doc_content)

    # Temporarily patch the DOCS_DIRECTORY constant in the tool
    with patch('app.tools.documentation_tool.DOCS_DIRECTORY', str(docs_dir)):
        # Search for the keyword
        results = doc_tool.search("Litestar")
        assert len(results) == 1
        assert results[0]["filepath"] == str(doc_file)
        assert "Litestar" in results[0]["snippet"]

        # Search for a non-existent keyword
        no_results = doc_tool.search("NonExistentKeyword")
        assert "No results found" in no_results[0].get("message", "")

# --- UploaderTool Tests (adapted from previous tests) ---

def test_uploader_tool_success(uploader_tool: UploaderTool, temp_file: str):
    filename = os.path.basename(temp_file)
    result = uploader_tool.handle_file_upload(source_path=temp_file, filename=filename)

    assert result["status"] == "success"
    assert result["metadata"]["filename"] == filename
    assert os.path.exists(result["filepath"])

# --- ConnectorTool Tests ---

def test_connector_tool_get_latest_block(connector_tool: ConnectorTool):
    # Mock the async call within the sync method
    mock_connector = MagicMock()
    # Create a mock that is awaitable
    mock_connector.get_latest_block = AsyncMock(return_value={"number": 123, "hash": "abc"})
    connector_tool._connectors["bitcoin"] = mock_connector

    # Act
    result = connector_tool.get_latest_block("bitcoin")

    # Assert
    assert result["number"] == 123
    assert result["hash"] == "abc"
    mock_connector.get_latest_block.assert_awaited_once()
