#!/usr/bin/python3
"""
Defines the unittests test_place.py
"""
import os
from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class TestPlace(TestBasemodel):
    """
    unit for Place class
    """

    def __init__(self, *args, **kwargs):
        """
        Init test class for Place
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Tests city_id attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.city_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id(self):
        """
        Tests user_id attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name(self):
        """
        Tests type of name attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_description(self):
        """
        Tests type of description attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.description),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_rooms(self):
        """
        Tests of number_rooms attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.number_rooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_bathrooms(self):
        """
        Tests  number_bathrooms attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.number_bathrooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_max_guest(self):
        """
        Tests  of max_guest attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.max_guest),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_price_by_night(self):
        """
        Tests type of price_by_night attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.price_by_night),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_latitude(self):
        """
        Tests  of latitude attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.latitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_longitude(self):
        """
        Tests for longitude attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.longitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_amenity_ids(self):
        """
        Tests the type of amenity_ids attribute
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
