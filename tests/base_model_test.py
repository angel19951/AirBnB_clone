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
                                        'base_model_test.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def testInit(self):
        """
        Test and setup of an object instance of BaseModel
        and makes sure it is an instance
        """
        self.new_instance = BaseModel()
        self.assertIsInstance(self.new_instance, BaseModel)

    def testId(self):
        """
        Test that UUID is working correctly by
        comparing two instances to validate if id is unique
        """
        self.new_id_1 = BaseModel()
        self.new_id_2 = BaseModel()
        self.assertNotEqual(self.new_id_1.id, self.new_id_2.id)

    def testCreate(self):
        """
        Test that created_at is wroking correctly by
        creating two intances at the same time and comparing
        them
        """
        self.create_1 = BaseModel()
        self.create_2 = BaseModel()
        self.assertNotEqual(self.create_1.created_at, self.create_2.created_at)

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
        Checks if method retuns a dictionary by
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

if __name__ == '__main__':
    unittest.main()
