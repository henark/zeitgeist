import pytest
import os
from unittest.mock import MagicMock, AsyncMock
from app.services.uploader import UploaderService, MAX_FILE_SIZE_BYTES
from app.timekeeper import TimeKeeperClient

# Use pytest's async capabilities
pytestmark = pytest.mark.asyncio

@pytest.fixture
def uploader_service() -> UploaderService:
    """Fixture to create an UploaderService with a mocked TimeKeeperClient."""
    mock_timekeeper = MagicMock(spec=TimeKeeperClient)
    # The __init__ of UploaderService doesn't require timekeeper for file uploads,
    # but it will for other methods. Let's provide it for consistency.
    service = UploaderService(timekeeper=mock_timekeeper)
    return service

@pytest.fixture(autouse=True)
def cleanup_files():
    """Fixture to clean up any created files after tests run."""
    yield
    # Cleanup code
    upload_dir = "uploads"
    if os.path.exists(upload_dir):
        for f in os.listdir(upload_dir):
            os.remove(os.path.join(upload_dir, f))
        if not os.listdir(upload_dir):
            os.rmdir(upload_dir)

async def test_handle_file_upload_success(uploader_service: UploaderService):
    """
    Tests a successful file upload.
    """
    # 1. Arrange
    mock_file_content = b"This is a test file."
    mock_upload_file = AsyncMock()
    mock_upload_file.filename = "test.txt"
    mock_upload_file.content_type = "text/plain"
    mock_upload_file.read = AsyncMock(return_value=mock_file_content)

    # 2. Act
    result = await uploader_service.handle_file_upload(mock_upload_file)

    # 3. Assert
    assert result["status"] == "success"
    assert result["metadata"]["filename"] == "test.txt"
    assert result["metadata"]["size_bytes"] == len(mock_file_content)
    assert "sha256_checksum" in result["metadata"]
    assert os.path.exists(result["filepath"])

async def test_handle_file_upload_disallowed_type(uploader_service: UploaderService):
    """
    Tests a file upload with a disallowed file extension.
    """
    # 1. Arrange
    mock_upload_file = AsyncMock()
    mock_upload_file.filename = "test.exe"
    mock_upload_file.content_type = "application/octet-stream"
    mock_upload_file.read = AsyncMock(return_value=b"some data")

    # 2. Act
    result = await uploader_service.handle_file_upload(mock_upload_file)

    # 3. Assert
    assert result["status"] == "error"
    assert "File type not allowed" in result["message"]

async def test_handle_file_upload_too_large(uploader_service: UploaderService):
    """
    Tests a file upload that exceeds the maximum size.
    """
    # 1. Arrange
    # Create content larger than the max size
    large_content = b"a" * (MAX_FILE_SIZE_BYTES + 1)
    mock_upload_file = AsyncMock()
    mock_upload_file.filename = "large_file.txt"
    mock_upload_file.content_type = "text/plain"
    mock_upload_file.read = AsyncMock(return_value=large_content)

    # 2. Act
    result = await uploader_service.handle_file_upload(mock_upload_file)

    # 3. Assert
    assert result["status"] == "error"
    assert "exceeds maximum size" in result["message"]

async def test_handle_file_upload_no_filename(uploader_service: UploaderService):
    """
    Tests a file upload with no filename.
    """
    # 1. Arrange
    mock_upload_file = AsyncMock()
    mock_upload_file.filename = ""  # No filename

    # 2. Act
    result = await uploader_service.handle_file_upload(mock_upload_file)

    # 3. Assert
    assert result["status"] == "error"
    assert "No filename provided" in result["message"]
