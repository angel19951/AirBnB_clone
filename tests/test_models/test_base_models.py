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
                                        'tests/test_models/test_base_models.py'
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
        self.save_obj = BaseModel()
        self.before_save = self.save_obj.updated_at
        self.save_obj.save()
        self.after_save = self.save_obj.updated_at
        self.assertNotEqual(self.before_save, self.after_save)

    def testUpdate(self):
        """
        checks if update method does not affect created_at date by
        comparing the different dates on the same file
        """
        self.update_obj = BaseModel()
        self.before_update = self.update_obj.created_at
        self.update_obj.save()
        self.after_update = self.update_obj.created_at
        self.assertEqual(self.before_update, self.after_update)

    def testDict(self):
        """
        Tests that method retuns a dictionary by
        comparing a predefined one to entered one
        """
        self.my_model = BaseModel()
        self.dictionary = dict(self.my_model.__dict__)
        self.dictionary['__class__'] = "BaseModel"
        self.dictionary['created_at'] =\
            self.dictionary['created_at'].isoformat()
        self.dictionary['updated_at'] =\
            self.dictionary['updated_at'].isoformat()
        self.assertDictEqual(self.dictionary, self.my_model.to_dict())
"""
    def testId_ToStr(self):
"""
# Test that id is a string
"""
        self.assertEqual(str(type(self.)))
"""
if __name__ == '__main__':
    unittest.main()
