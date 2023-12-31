#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    """Test Cases for the Place class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Place class."""

        base = Place()
        self.assertEqual(str(type(base)), "<class 'models.place.Place'>")
        self.assertIsInstance(base, Place)
        self.assertTrue(issubclass(type(base), BaseModel))

    def test_8_attributes(self):
        """Tests the attributes of Place class."""
        attributes = storage.attributes()["Place"]
        obj = Place()
        for key, value in attributes.items():
            self.assertTrue(hasattr(obj, key))
            self.assertEqual(type(getattr(obj, key, None)), value)


if __name__ == "__main__":
    unittest.main()
