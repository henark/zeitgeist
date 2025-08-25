from __future__ import annotations
import os
import json
from typing import Any

class LanguageHub:
    """
    A service for loading and managing translations from locale files.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Implement as a Singleton to ensure translations are loaded only once.
        if not cls._instance:
            cls._instance = super(LanguageHub, cls).__new__(cls)
        return cls._instance

    def __init__(self, locales_dir: str = "feat/locales"):
        # The __init__ will be called every time, but the data is loaded only once.
        if hasattr(self, '_translations'):
            return

        self.locales_dir = locales_dir
        self._translations: dict[str, dict[str, str]] = {}
        self._load_translations()

    def _load_translations(self):
        """
        Loads all .json files from the locales directory into memory.
        """
        if not os.path.exists(self.locales_dir):
            # In a real app, we might want to log a warning.
            return

        for filename in os.listdir(self.locales_dir):
            if filename.endswith(".json"):
                locale_name = filename.split(".")[0]
                filepath = os.path.join(self.locales_dir, filename)
                with open(filepath, "r", encoding="utf-8") as f:
                    self._translations[locale_name] = json.load(f)

    def translate(self, key: str, locale: str, fallback_locale: str = "en") -> str:
        """
        Retrieves a translation for a given key and locale.
        Falls back to the fallback_locale if the key is not found in the target locale.
        Returns the key itself if not found in either locale.
        """
        # Try to get the translation from the specified locale
        translation = self._translations.get(locale, {}).get(key)

        if translation:
            return translation

        # If not found, try the fallback locale
        fallback_translation = self._translations.get(fallback_locale, {}).get(key)

        if fallback_translation:
            return fallback_translation

        # If still not found, return the key itself as a last resort
        return key
