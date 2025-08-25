import pytest
import json
import os
from unittest.mock import patch
from app.tools.localization_tool import LocalizationTool
from feat.language_hub import LanguageHub

# --- Fixtures ---

@pytest.fixture
def temp_locales(tmp_path):
    """Fixture to create temporary locale files for testing."""
    locales_dir = tmp_path / "feat" / "locales"
    locales_dir.mkdir(parents=True)

    en_data = {"welcome": "Hello", "test_key": "English Only"}
    pt_data = {"welcome": "Olá"}

    with open(locales_dir / "en.json", "w") as f:
        json.dump(en_data, f)

    with open(locales_dir / "pt.json", "w") as f:
        json.dump(pt_data, f)

    return str(locales_dir)

@pytest.fixture
def hub(temp_locales) -> LanguageHub:
    # We need to reset the singleton instance for testing
    LanguageHub._instance = None
    return LanguageHub(locales_dir=temp_locales)

@pytest.fixture
def loc_tool(hub) -> LocalizationTool:
    # Patch the __init__ to use our test hub instance
    with patch.object(LocalizationTool, '__init__', lambda s: setattr(s, '_language_hub', hub)):
        tool = LocalizationTool()
        tool.actions = {"get": tool.get_translation}
        yield tool


# --- LanguageHub Service Tests ---

def test_language_hub_loads_translations(hub: LanguageHub):
    """Tests that the hub correctly loads translations from files."""
    assert "en" in hub._translations
    assert "pt" in hub._translations
    assert hub._translations["en"]["welcome"] == "Hello"
    assert hub._translations["pt"]["welcome"] == "Olá"

def test_translate_fetches_correct_locale(hub: LanguageHub):
    """Tests fetching a translation for a specific locale."""
    assert hub.translate("welcome", "pt") == "Olá"
    assert hub.translate("welcome", "en") == "Hello"

def test_translate_fallback_logic(hub: LanguageHub):
    """Tests that it falls back to English when a key is missing."""
    assert hub.translate("test_key", "pt") == "English Only"

def test_translate_key_not_found(hub: LanguageHub):
    """Tests that it returns the key itself if not found in any locale."""
    assert hub.translate("non_existent_key", "pt") == "non_existent_key"

# --- LocalizationTool Tests ---

def test_localization_tool_get_translation(loc_tool: LocalizationTool):
    """Tests the tool's ability to get a translation via the hub."""
    # Test Portuguese translation
    result_pt = loc_tool.get_translation(key="welcome", locale="pt")
    assert result_pt == "Olá"

    # Test English fallback
    result_en_fallback = loc_tool.get_translation(key="test_key", locale="pt")
    assert result_en_fallback == "English Only"

    # Test key not found
    result_not_found = loc_tool.get_translation(key="non_existent_key", locale="en")
    assert result_not_found == "non_existent_key"
