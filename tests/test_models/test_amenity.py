#!/usr/bin/python3
"""
Module instant  object of storage engine
"""
import os
from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity


class TestAmenity(TestBasemodel):
    """
    Test the Amenity class
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the test Amenity class
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """
        Tests the type of name attribute name
        """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.assertNotEqual(type(new.name), str)
        else:
            self.assertEqual(type(new.name), type(None))
