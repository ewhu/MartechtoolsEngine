# test_martechtoolsengine.py
"""
Tests for MartechtoolsEngine module.
"""

import unittest
from martechtoolsengine import MartechtoolsEngine

class TestMartechtoolsEngine(unittest.TestCase):
    """Test cases for MartechtoolsEngine class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MartechtoolsEngine()
        self.assertIsInstance(instance, MartechtoolsEngine)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MartechtoolsEngine()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
