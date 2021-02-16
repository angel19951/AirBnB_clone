#!/usr/bin/python3
"""
This module contains unit test for the BaseModel class
"""
from models.base_model import BaseModel
import unittest
import pep8


class TestBaseClass(unittest.TestCase):
    """
    Test Base clase using unit test
    """

    def testPep8(self):
        """
        Check pep8 linter requirements
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py',
                                        'tests/test_models/test_base_model.py'
                                        ])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """
        Set up for the class to use
        """
        self.new_instance_1 = BaseModel()
        self.new_instance_2 = BaseModel()

    def testInit(self):
        """
        Test and setup of an object instance of BaseModel
        and makes sure it is an instance
        """
        self.assertIsInstance(self.new_instance_1, BaseModel)
        self.assertIsInstance(self.new_instance_2, BaseModel)

    def testId(self):
        """
        Test that UUID is working correctly by
        comparing two instances to validate if id is unique
        """
        self.assertNotEqual(self.new_instance_1.id,
                            self.new_instance_2.id)

    def testCreate(self):
        """
        Test that created_at is wroking correctly by
        creating two intances at the same time and comparing
        them
        """
        self.assertNotEqual(self.new_instance_1.created_at,
                            self.new_instance_2.created_at)

    def testSave(self):
        """
        Checks if save method is working correctly by
        comparing two intances saved/updated datetime
        to validate if update_at datetime is unique
        """
        self.before_save = self.new_instance_1.updated_at
        self.new_instance_1.save()
        self.after_save = self.new_instance_1.updated_at
        self.assertNotEqual(self.before_save, self.after_save)

    def testUpdate(self):
        """
        checks if update method does not affect created_at date by
        comparing the different dates on the same file
        """
        self.before_update = self.new_instance_2.created_at
        self.new_instance_2.save()
        self.after_update = self.new_instance_2.created_at
        self.assertEqual(self.before_update, self.after_update)

    def testDict(self):
        """
        Tests that method retuns a dictionary by
        comparing a predefined one to entered one
        """
        self.dictionary = dict(self.new_instance_1.__dict__)
        self.dictionary['__class__'] = "BaseModel"
        self.dictionary['created_at'] =\
            self.dictionary['created_at'].isoformat()
        self.dictionary['updated_at'] =\
            self.dictionary['updated_at'].isoformat()
        self.assertDictEqual(self.dictionary, self.new_instance_1.to_dict())

    def testId_ToStr(self):
        """
        Test that id is string
        """
        self.assertEqual(type(self.new_instance_1.id), str)

if __name__ == '__main__':
    unittest.main()
