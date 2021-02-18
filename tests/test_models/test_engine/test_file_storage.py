#!/usr/bin/python3
"""
This module contains unit test for the FileStorage class
"""
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
import unittest
import pep8
import json
import os

file = 'file.json'


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
        self.my_city = City()

    def test_docstring(self):
        """
        Test docstring
        """
        self.assertIsNotNone(FileStorage.__doc__)

    def testInstance(self):
        """
        Test that a file is an instance
        """
        self.assertIsInstance(self.my_model, BaseModel)

    def testCityInstance(self):
        """
        Test that an object is an instance
        """
        self.assertIsInstance(self.my_city, BaseModel)

    def tearDown(self):
        """
        Deletes an instance
        """
        del self.my_model

    def testNew(self):
        """
        Test new method to validate that it runs correctly
        """
        new_dict = storage.all().copy()
        storage.new(BaseModel())
        self.assertNotEqual(new_dict, storage.all())

    def testAll(self):
        """
        Test all method to validate that it runs correctly
        """
        my_dict = storage.all()
        self.assertEqual(type(my_dict), dict)

    def testSave(self):
        """
        Test save if it creates a json file
        """
        os.remove(file)
        self.my_model.save()
        self.assertTrue(os.path.isfile(file))

    def testReload(self):
        """
        Uses basemodel to test if reload is
        deserializing json correctly
        """
        flag = 0
        my_obj = dict()
        self.my_model.save()
        model_id = self.my_model.id
        storage.reload()
        my_objs = storage.all().copy()
        for key, val in my_objs.items():
            if model_id in key:
                if type(val).__name__ == "BaseModel":
                    flag = 1
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()
