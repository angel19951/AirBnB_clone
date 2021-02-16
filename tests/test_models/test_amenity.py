#!/usr/bin/python3
"""
This module contains unit test for the Amenity class
"""
from models.amenity import Amenity
import unittest
import pep8


class TestUser(unittest.TestCase):
    """
    Test amenity class unsing unit test
    """
    def testPep8(self):
        """
        Check pep8 linter requirements
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py',
                                        'tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def testInit(self):
        """
        Test and setup of a amenity instance of Amenity
        and makes sure it is instance
        """
        self.new_amenity = Amenity()
        self.assertIsInstance(self.new_amenity, Amenity)

    def testID(self):
        """
        Test that UUID is not corrupted and working correctly
        """
        self.new_id_1 = Amenity()
        self.new_id_2 = Amenity()
        self.assertNotEqual(self.new_id_1.id, self.new_id_2.id)

    def testCreate(self):
        """
        Test that created_at is working correctly
        """
        self.create_1 = Amenity()
        self.create_2 = Amenity()
        self.assertNotEqual(self.create_1.created_at, self.create_2.created_at)

    def testSave(self):
        """
        Test that save method is working correctly by
        comparing two intances saved/updated validating
        they are unique
        """
        self.save_amen = Amenity()
        self.before_save = self.save_amen.updated_at
        self.save_amen.save()
        self.after_save = self.save_amen.updated_at
        self.assertNotEqual(self.before_save, self.after_save)

    def testUpdate(self):
        """
        Test that update method does not affect created_at date by
        comparing datimes of the file
        """
        self.update_amen = Amenity()
        self.before_update = self.update_amen.created_at
        self.update_amen.save()
        self.after_update = self.update_amen.created_at
        self.assertEqual(self.before_update, self.after_update)

    def testDict(self):
        """
        Test that to_dict() method returns a dictionary by
        comparing a predefined one to the entered one
        """
        self.my_amenity = Amenity()
        self.dictionary = dict(self.my_amenity.__dict__)
        self.dictionary['__class__'] = 'Amenity'
        self.dictionary['created_at'] =\
            self.dictionary['created_at'].isoformat()
        self.dictionary['updated_at'] =\
            self.dictionary['updated_at'].isoformat()
        self.assertDictEqual(self.dictionary, self.my_amenity.to_dict())

if __name__ == '__main__':
    unittest.main()
