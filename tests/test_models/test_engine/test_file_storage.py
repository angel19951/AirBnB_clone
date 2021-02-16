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
        self.all_storage = storage.all()
        storage.new(self.my_model)
        self.new_dict = storage.all()
        self.assertEqual(self.all_storage, self.new_dict)

    def testAll(self):
        """
        Test all method to validate it runs correctly
        """
        self.my_dict = storage.all()
        self.assertEqual(type(self.my_dict),  dict)

    def testSave(self):
        """
        Test save method to validate it works correctly
        """
        self.dict_save = storage.save()
        storage.save()
        self.new_save = storage.save()
        self.assertEqual(self.dict_save, self.new_save)

    def testReload(self):
        """
        Test reload method to validate it works correctly
        """
        self.file_reload = storage.reload()
        storage.reload()
        self.file_save = storage.reload()
        self.assertEqual(self.file_reload, self.file_save)
