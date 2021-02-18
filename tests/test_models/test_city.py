#!/usr/bin/python3
"""
This module contains unit test for the City class
"""
from models.city import City
import unittest
import pep8


class TestUser(unittest.TestCase):
    """
    Test City class using unit test
    """
    def testPep8(self):
        """
        Check pep8 linter requirements
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py',
                                        'tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def testInit(self):
        """
        Test and setup of an instance of City class
        and validates it is an instance
        """
        self.new_city = City()
        self.assertIsInstance(self.new_city, City)

    def testId(self):
        """
        Test that UUID is working correctly by
        comparing two instances to validate if id is unique
        """
        self.new_id_1 = City()
        self.new_id_2 = City()
        self.assertNotEqual(self.new_id_1.id, self.new_id_2.id)

    def testCreate(self):
        """
        Test that created_at if woring correctly
        """
        self.new_city_1 = City()
        self.new_city_2 = City()
        self.assertNotEqual(self.new_city_1.created_at,
                            self.new_city_2.created_at)

    def testSave(self):
        """
        Test that save method is working correctly
        """
        self.save_city = City()
        self.before_save = self.save_city.updated_at
        self.save_city.save()
        self.after_save = self.save_city.updated_at
        self.assertNotEqual(self.before_save, self.after_save)

    def testUpdate(self):
        """
        Test if update method does not affect created_at date
        """
        self.update_city = City()
        self.before_update = self.update_city.created_at
        self.update_city.save()
        self.after_update = self.update_city.created_at
        self.assertEqual(self.before_update, self.after_update)

    def testDict(self):
        """
        Test that to_dict method retuns a dictionary
        """
        self.my_city = City()
        self.dictionary = dict(self.my_city.__dict__)
        self.dictionary['__class__'] = "City"
        self.dictionary['created_at'] =\
            self.dictionary['created_at'].isoformat()
        self.dictionary['updated_at'] =\
            self.dictionary['updated_at'].isoformat()
        self.assertEqual(self.dictionary, self.my_city.to_dict())

if __name__ == '__main__':
    unittest.main()
