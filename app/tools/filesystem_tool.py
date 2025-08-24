from __future__ import annotations
import os
from typing import Any
from .registry import Tool

# Define a base directory to restrict file system access for security
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

class FileSystemTool(Tool):
    """
    A tool for interacting with the local file system in a controlled manner.
    """
    name = "filesystem"

    def __init__(self):
        super().__init__()
        self.actions = {
            "read": self.read,
            "list": self.list,
            "write": self.write,
        }

    def _is_safe_path(self, path: str) -> bool:
        """
        Check if the resolved path is within the project's base directory.
        """
        abs_path = os.path.abspath(os.path.join(BASE_DIR, path))
        return os.path.commonpath([abs_path, BASE_DIR]) == BASE_DIR

    def read(self, path: str) -> str:
        """
        Reads the content of a file.
        """
        if not self._is_safe_path(path):
            raise PermissionError("Access to paths outside the project directory is denied.")

        full_path = os.path.join(BASE_DIR, path)
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()

    def list(self, path: str = ".") -> list[str]:
        """
        Lists files and directories in a given path.
        """
        if not self._is_safe_path(path):
            raise PermissionError("Access to paths outside the project directory is denied.")

        full_path = os.path.join(BASE_DIR, path)
        return os.listdir(full_path)

    def write(self, path: str, content: str) -> str:
        """
        Writes content to a file. Overwrites the file if it exists.
        """
        if not self._is_safe_path(path):
            raise PermissionError("Access to paths outside the project directory is denied.")

        full_path = os.path.join(BASE_DIR, path)

        # Ensure parent directory exists
        parent_dir = os.path.dirname(full_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"Successfully wrote {len(content)} characters to {path}"
