#!/usr/bin/python3
"""
Tests for Amenity class
"""

import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test amenity class
    """

    @classmethod
    def setUpClass(cls):
        """ Setup class """
        cls.my_amenity = Amenity()
        #cls.my_amenity.name = "Wi-fi"

    @classmethod
    def tearDownClass(cls):
        del cls.my_amenity
        try:
            os.remove("BaseModel.json")
        except FileNotFoundError:
            pass

    def test_is_subclass(self):
        """
        Tests Amenity inherits from BaseModel
        """
        self.assertTrue(issubclass(self.my_amenity.__class__, BaseModel), True)

    def test_funcs(self):
        """
        Tests documentation
        """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes(self):
        """
        Tests attributes in the class
        """
        self.assertTrue('id' in self.my_amenity.__dict__)
        self.assertTrue('created_at' in self.my_amenity.__dict__)
        self.assertTrue('updated_at' in self.my_amenity.__dict__)
        #self.assertTrue('name' in self.my_amenity.__dict__)

    def test_str_attributes(self):
        """
        Tests attributes are strings
        """
        self.assertEqual(type(self.my_amenity.name), str)

if __name__ == "__main__":
    unittest.main()
