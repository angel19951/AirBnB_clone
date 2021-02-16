#!/usr/bin/python3
"""
This module contains unit test for the FileStorage class
"""
from models import storage
from models.base_model import BaseModel
import unittest
import pep8
import json


class TestFileStorage(unittest.TestCase):
    """
    Unit test for FileStorage class
    """
    def testPep8(self):
        """
        Test pep8 requirements
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result =\
            pep8style.check_files(
                ['models/engine/file_storage.py',
                 'tests/test_models/test_engine/test_file_storage.py'
                 ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """
        Initializes an instance
        """
        self.my_model = BaseModel()

    def testNew(self):
        """
        Test new method to validate it run correctly
        """
    def testAll(self):
        """
        Test all method to validate it runs correctly
        """
        self.my_model.save()
        self.my_dict = storage.all()
        self.assertEqual(type(self.my_dict),  dict)
