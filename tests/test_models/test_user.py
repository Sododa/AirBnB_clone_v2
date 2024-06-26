#!/usr/bin/python3
"""
Defines the unittests for user.py
"""
import os
# from sqlalchemy import Column
from tests.test_models.test_base_model import TestBasemodel
from models.user import User


class TestUser(TestBasemodel):
    """
    A unittest for User class
    """

    def __init__(self, *args, **kwargs):
        """
        Initial the test class for User
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Tests first_name attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.first_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_last_name(self):
        """
        Tests last_name attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.last_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_email(self):
        """
        Tests email attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.email),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_password(self):
        """
        Tests password attribute
        """
        new = self.value()
        self.assertEqual(
            type(new.password),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
