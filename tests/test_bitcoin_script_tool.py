import pytest
import json
from app.tools.bitcoin_script_tool import BitcoinScriptTool

@pytest.fixture
def script_tool() -> BitcoinScriptTool:
    return BitcoinScriptTool()

def load_test_vectors(filename: str) -> list:
    with open(f"tests/test_vectors/{filename}", "r") as f:
        return json.load(f)

def test_valid_scripts(script_tool: BitcoinScriptTool):
    """
    Tests valid script execution based on test vectors from a JSON file.
    """
    valid_tests = load_test_vectors("ec_op_tests_valid.json")

    for test_case in valid_tests:
        print(f"Running valid test: {test_case['comment']}")
        result = script_tool.simulate_script(
            script=test_case["script"],
            initial_stack=test_case["initial_stack"]
        )
        assert result["final_stack"] == test_case["final_stack"]

def test_invalid_scripts(script_tool: BitcoinScriptTool):
    """
    Tests invalid script execution, expecting specific errors.
    """
    invalid_tests = load_test_vectors("ec_op_tests_invalid.json")

    for test_case in invalid_tests:
        print(f"Running invalid test: {test_case['comment']}")
        with pytest.raises(ValueError) as excinfo:
            script_tool.simulate_script(
                script=test_case["script"],
                initial_stack=test_case["initial_stack"]
            )
        assert test_case["error"] in str(excinfo.value)
