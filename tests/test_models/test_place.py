#!/usr/bin/python3
"""
This module contains unit test for the Place class
"""
from models.place import Place
import unittest
import pep8


class TestPlace(unittest.TestCase):
    """
    Test Place class using unit test
    """
    def testPep8(self):
        """
        Check pep8 linter requirements
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/place.py',
                                        'tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def testInit(self):
        """
        Test and setup of an object instance of Place
        and validates it is an instance
        """
        self.new_instance = Place()
        self.assertIsInstance(self.new_instance, Place)

    def testId(self):
        """
        Test that UUID is working correctly
        """
        self.new_id_1 = Place()
        self.new_id_2 = Place()
        self.assertNotEqual(self.new_id_1.id, self.new_id_2.id)

    def testCreate(self):
        """
        Test that created_at is wroking correctly
        """
        self.create_place_1 = Place()
        self.create_place_2 = Place()
        self.assertNotEqual(self.create_place_1.created_at,
                            self.create_place_2.created_at)

    def testSave(self):
        """
        Checks if save method is working correctly
        """
        self.save_place = Place()
        self.save_place.save()
        self.before_save = self.save_place.updated_at
        self.save_place.save()
        self.after_save = self.save_place.updated_at
        self.assertNotEqual(self.before_save, self.after_save)

    def testUpdate(self):
        """
        Test update method does not affect created_at date by
        comparing the different dates on the same file
        """
        self.update_place = Place()
        self.before_update = self.update_place.created_at
        self.update_place.save()
        self.after_update = self.update_place.created_at
        self.assertEqual(self.before_update, self.after_update)

    def testDict(self):
        """
        Checks if method retuns a dictionary by
        comparing a predefined one to entered one
        """
        self.my_place = Place()
        self.dictionary = dict(self.my_place.__dict__)
        self.dictionary['__class__'] = "Place"
        self.dictionary['created_at'] =\
            self.dictionary['created_at'].isoformat()
        self.dictionary['updated_at'] =\
            self.dictionary['updated_at'].isoformat()
        self.assertDictEqual(self.dictionary, self.my_place.to_dict())

if __name__ == '__main__':
    unittest.main()
