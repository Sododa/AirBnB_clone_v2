#!/usr/bin/python3
"""
Defines the unittests for models/state.py
"""
import os
from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class TestState(TestBasemodel):
    """
    A unittest for State class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the test class for State
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Tests the type of name attribute
        """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.name), str)
        else:
            self.assertIsNone(new.name)
