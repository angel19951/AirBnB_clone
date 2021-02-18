#!/usr/bin/python3
"""
This module contains unit test for the State class
"""
from models.state import State
import unittest
import pep8


class TestCity(unittest.TestCase):
    """
    Test City class using unit test
    """
    def testPep8(self):
        """
        Check pep8 linter requirements
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py',
                                        'tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def testInit(self):
        """
        Test and setup of an instance of State
        and validates it is an instance
        """
        self.new_state = State()
        self.assertIsInstance(self.new_state, State)

    def testID(self):
        """
        Test that UUID is working correctly
        """
        self.new_id_1 = State()
        self.new_id_2 = State()
        self.assertNotEqual(self.new_id_1.id, self.new_id_2.id)

    def testCreate(self):
        """
        Test that created_at is working correctly
        """
        self.create_st_1 = State()
        self.create_st_2 = State()
        self.assertNotEqual(self.create_st_1.created_at,
                            self.create_st_2.created_at)

    def testSave(self):
        """
        Test that save method is working correctly
        """
        self.save_state = State()
        self.before_save = self.save_state.updated_at
        self.save_state.save()
        self.after_save = self.save_state.updated_at
        self.assertNotEqual(self.before_save, self.after_save)

    def testUpdate(self):
        """
        Test that update method does not affect created_at date
        """
        self.update_state = State()
        self.before_update = self.update_state.created_at
        self.update_state.save()
        self.after_update = self.update_state.created_at
        self.assertEqual(self.before_update, self.after_update)

    def testDict(self):
        """
        Checks if method retuns a dictionary by
        comparing a predefined one to entered one
        """
        self.my_state = State()
        self.dictionary = dict(self.my_state.__dict__)
        self.dictionary['__class__'] = "State"
        self.dictionary['created_at'] =\
            self.dictionary['created_at'].isoformat()
        self.dictionary['updated_at'] =\
            self.dictionary['updated_at'].isoformat()
        self.assertDictEqual(self.dictionary, self.my_state.to_dict())


if __name__ == '__main__':
    unittest.main()
