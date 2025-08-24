from __future__ import annotations
import os
import hashlib
import logging
from typing import Any
from .registry import Tool
from ..timekeeper import TimeKeeperClient

# Define allowed file extensions and max size
ALLOWED_EXTENSIONS = {"json", "xml", "csv", "bin", "txt", "log"}
MAX_FILE_SIZE_MB = 100
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024
UPLOAD_DIRECTORY = "uploads"

class UploaderTool(Tool):
    """
    A tool for handling various types of uploads.
    """
    name = "uploader"

    def __init__(self, timekeeper: TimeKeeperClient):
        super().__init__()
        self._timekeeper = timekeeper
        self.actions = {
            "upload_file": self.handle_file_upload,
            "upload_blockchain_data": self.handle_blockchain_data,
            "upload_spacetime_data": self.handle_spacetime_data,
            "upload_smart_contract": self.handle_smart_contract_upload,
        }
        if not os.path.exists(UPLOAD_DIRECTORY):
            os.makedirs(UPLOAD_DIRECTORY)

    def is_allowed_file(self, filename: str) -> bool:
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    def handle_file_upload(self, source_path: str, filename: str) -> dict:
        logging.info(f"Handling file upload for source: {source_path}")
        if not os.path.exists(source_path):
            return {"status": "error", "message": f"Source file not found: {source_path}"}

        if not self.is_allowed_file(filename):
            return {"status": "error", "message": f"File type not allowed: {filename}"}

        file_size = os.path.getsize(source_path)
        if file_size > MAX_FILE_SIZE_BYTES:
            return {"status": "error", "message": f"File exceeds maximum size of {MAX_FILE_SIZE_MB}MB."}

        with open(source_path, "rb") as f:
            file_content = f.read()

        sha256_hash = hashlib.sha256()
        sha256_hash.update(file_content)
        checksum = sha256_hash.hexdigest()

        filepath = os.path.join(UPLOAD_DIRECTORY, filename)
        with open(filepath, "wb") as f:
            f.write(file_content)

        metadata = {
            "filename": filename,
            "size_bytes": file_size,
            "sha256_checksum": checksum,
        }
        return {"status": "success", "filepath": filepath, "metadata": metadata}

    def handle_blockchain_data(self, data: dict[str, Any]) -> dict:
        logging.info(f"Handling blockchain data upload for chain: {data.get('chain')}")
        # This logic would be more complex, using the ConnectorTool
        return {"status": "success", "message": "Blockchain data received.", "data": data}

    def handle_spacetime_data(self, data: dict[str, Any]) -> dict:
        logging.info("Handling spacetime data upload request.")
        return {"status": "not_implemented", "feature": "spacetime_data"}

    def handle_smart_contract_upload(self, data: dict[str, Any]) -> dict:
        logging.info("Handling smart contract upload request.")
        return {"status": "not_implemented", "feature": "smart_contract"}
