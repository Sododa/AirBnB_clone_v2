#!/usr/bin/python3
""" unittests for models"""
import os
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """test for State class """

    def __init__(self, *args, **kwargs):
        """test class for State """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Tests name attribute """
        new = self.value()
        self.assertEqual(
                type(new.name),
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
                )
