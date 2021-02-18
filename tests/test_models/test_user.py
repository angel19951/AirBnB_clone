#!/usr/bin/python3
"""
This module contains unit test for the User class
"""
from models.user import User
from models.base_model import BaseModel
import unittest
import pep8


class TestUserClass(unittest.TestCase):
    """
    Test user class using unit test
    """
    def testPep8(self):
        """
        Check pep8 linter requirements
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py',
                                       'tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style error (and warnings).")

    def testInit(self):
        """
        Test and setup of an object instance of User class
        and makes sure it is instance
        """
        self.user = User()
        self.assertIsInstance(self.user, User)

    def testId(self):
        """
        Checks that uuid is working correctly and has not been corrupted
        """
        self.new_id_1 = User()
        self.new_id_2 = User()
        self.assertEqual(self.new_id_2.id, self.new_id_2.id)

    def testCreate(self):
        """
        Tests that create_at method is working correctly by
        creating and comparing two intances at the same time
        """
        self.create_1 = User()
        self.create_2 = User()
        self.assertNotEqual(self.create_1.created_at, self.create_2.created_at)

    def testSave(self):
        """
        Check if save method is working correctly by
        comparing two intances save/updated datetime
        to validated if updated_at datetime is unique
        """
        self.save_user = User()
        self.before_save = self.save_user.updated_at
        self.save_user.save()
        self.after_save = self.save_user.updated_at
        self.assertNotEqual(self.before_save, self.after_save)

    def testUpdate(self):
        """
        Checks if update method is working correctly by
        comparing the different dates on the file
        """
        self.update_user = User()
        self.before_update = self.update_user.created_at
        self.update_user.save()
        self.after_update = self.update_user.created_at
        self.assertEqual(self.before_update, self.after_update)

    def testDict(self):
        """
        Checks if to_dict method returns a dictionary by
        comparing a predefined one to the entered one
        """
        self.my_user = User()
        self.dictionary = dict(self.my_user.__dict__)
        self.dictionary['__class__'] = "User"
        self.dictionary['created_at'] =\
            self.dictionary['created_at'].isoformat()
        self.dictionary['updated_at'] =\
            self.dictionary['updated_at'].isoformat()
        self.assertDictEqual(self.dictionary, self.my_user.to_dict())

if __name__ == '__main__':
    unittest.main()
