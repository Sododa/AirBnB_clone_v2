#!/usr/bin/python3
"""
Defines the unittests for models/test_state.py
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
        new = self.value(name="California")
        self.assertEqual(type(new.name), str)
