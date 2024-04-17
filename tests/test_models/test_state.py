#!/usr/bin/python3
"""
Defines the unittests for models/state.py
"""
import os
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    A unittest class for testing the State model
    """

    def setUp(self):
        """
        Set up before each test case
        """
        self.state = State()

    def tearDown(self):
        """
        Clean up after each test case
        """
        del self.state

    def test_name_attribute(self):
        """
        Test the 'name' attribute of the State instance
        """
        # Check if the 'name' attribute is of type str
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertIsInstance(self.state.name, str)
        else:
            # For database storage, 'name' should initially be None
            self.assertIsNone(self.state.name)

    def test_save_method(self):
        """
        Test the 'save' method of the State instance
        """
        # Save the State instance and check if the updated_at attribute changes
        initial_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, initial_updated_at)


if __name__ == '__main__':
    unittest.main()
