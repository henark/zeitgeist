import unittest
from unittest.mock import MagicMock
from pathlib import Path
import sys
import os

# Add the 'vibe-coder' directory to the Python path to allow importing 'planner'
sys.path.insert(0, str(Path(__file__).parent))

# Now we can import the planner and its task classes
from planner import next_task, GasOptimizationTask, DocumentationTask

class TestPlanner(unittest.TestCase):
    """
    Test suite for the planner to verify the basic reasoning engine.
    """

    def setUp(self):
        """
        Set up the test environment before each test.
        """
        # A mock ledger object is needed for the next_task function signature.
        self.mock_ledger = MagicMock()

        # The GasOptimizationTask depends on 'TimeChain.sol' and 'README.md'
        # Let's ensure dummy versions exist for our tests.
        self.root_dir = Path(__file__).parent.parent.parent
        (self.root_dir / "TimeChain.sol").write_text("contract TimeChain {}")
        # The documentation task reads README.md, so let's ensure it exists.
        if not (self.root_dir / "README.md").exists():
            (self.root_dir / "README.md").write_text("# Test README")


    def test_selects_gas_task_from_dict(self):
        """
        Tests if the planner selects GasOptimizationTask when 'gas' is in a dict message.
        """
        print("\nRunning test: test_selects_gas_task_from_dict")
        coh = {"message": "we need to optimize gas costs"}
        task = next_task(coh, self.mock_ledger)
        self.assertIsInstance(task, GasOptimizationTask, "Should select GasOptimizationTask")
        patch = task.generate_patch()
        self.assertIsInstance(patch, str)
        self.assertIn("gas_optimized", patch, "Patch should contain expected content")

    def test_selects_docs_task_from_string(self):
        """
        Tests if the planner selects DocumentationTask when 'docs' is in a string message.
        """
        print("\nRunning test: test_selects_docs_task_from_string")
        coh = "please improve the project docs"
        task = next_task(coh, self.mock_ledger)
        self.assertIsInstance(task, DocumentationTask, "Should select DocumentationTask")
        patch = task.generate_patch()
        self.assertIsInstance(patch, str)
        self.assertIn("## Autonomous Agents", patch, "Patch should contain new section")

    def test_selects_no_task_for_unrelated_message(self):
        """
        Tests if the planner returns None when no keywords are found in the message.
        """
        print("\nRunning test: test_selects_no_task_for_unrelated_message")
        coh = "a generic, unrelated message about something else"
        task = next_task(coh, self.mock_ledger)
        self.assertIsNone(task, "Should not select any task")

    def test_handles_empty_string_message(self):
        """
        Tests if the planner returns None for an empty string message.
        """
        print("\nRunning test: test_handles_empty_string_message")
        coh = ""
        task = next_task(coh, self.mock_ledger)
        self.assertIsNone(task, "Should not select any task for empty string")

    def test_handles_dict_without_relevant_key(self):
        """
        Tests if the planner returns None for a dictionary without a 'message' or 'text' key.
        """
        print("\nRunning test: test_handles_dict_without_relevant_key")
        coh = {"unrelated_key": "some other value"}
        task = next_task(coh, self.mock_ledger)
        self.assertIsNone(task, "Should not select any task for irrelevant dict")

if __name__ == '__main__':
    # Change the current working directory to the script's directory
    # to ensure file paths in the planner work as expected.
    os.chdir(str(Path(__file__).parent))
    unittest.main()
