"""
Test module for the biblestudy package.

This file demonstrates that the package can be imported and tested.
"""

import unittest
import sys
import os

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from biblestudy import main
from biblestudy.config_loader import get_notes_directory


class TestBibleStudyPackage(unittest.TestCase):
    """Test cases for the biblestudy package."""
    
    def test_package_import(self):
        """Test that the main package can be imported."""
        self.assertIsNotNone(main)
        self.assertTrue(callable(main))
    
    def test_config_fallback(self):
        """Test that config loading works without config.py."""
        notes_dir = get_notes_directory()
        self.assertEqual(notes_dir, "notes")
    
    def test_cli_module_exists(self):
        """Test that CLI module exists and has main function."""
        from biblestudy import cli
        self.assertTrue(hasattr(cli, 'main'))
        self.assertTrue(callable(cli.main))


if __name__ == '__main__':
    unittest.main()