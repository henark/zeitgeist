from __future__ import annotations
import os
from typing import Any
from .registry import Tool

DOCS_DIRECTORY = "docs"

class DocumentationTool(Tool):
    """
    A tool for searching through the project's markdown documentation.
    """
    name = "documentation"

    def __init__(self):
        super().__init__()
        self.actions = {
            "search": self.search,
        }

    def search(self, query: str) -> list[dict[str, str]]:
        """
        Performs a case-insensitive keyword search in all .md files in the docs/ directory.
        Returns a list of matching lines and their file paths.
        """
        if not os.path.exists(DOCS_DIRECTORY) or not os.path.isdir(DOCS_DIRECTORY):
            return [{"error": "Docs directory not found."}]

        query_lower = query.lower()
        results = []

        for filename in os.listdir(DOCS_DIRECTORY):
            if filename.endswith(".md"):
                filepath = os.path.join(DOCS_DIRECTORY, filename)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        for i, line in enumerate(f):
                            if query_lower in line.lower():
                                results.append({
                                    "filepath": filepath,
                                    "line_number": i + 1,
                                    "snippet": line.strip()
                                })
                except Exception as e:
                    results.append({"error": f"Could not read file {filepath}: {e}"})

        if not results:
            return [{"message": f"No results found for query: '{query}'"}]

        return results
