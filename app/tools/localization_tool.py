from __future__ import annotations
from typing import Any
from .registry import Tool
from feat.language_hub import LanguageHub

class LocalizationTool(Tool):
    """
    A tool for retrieving translated strings from the Language Hub.
    """
    name = "localization"

    def __init__(self):
        super().__init__()
        self._language_hub = LanguageHub()
        self.actions = {
            "get": self.get_translation,
        }

    def get_translation(self, key: str, locale: str) -> str:
        """
        Gets a translation for a given key and locale.
        """
        return self._language_hub.translate(key, locale)
