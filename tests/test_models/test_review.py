#!/usr/bin/python3
"""
This module contains unit test for Review class
"""
from models.review import Review
import unittest
import pep8


class TestRevie(unittest.TestCase):
    """
    Test Review class using unit test
    """
    def testPep8(self):
        """
        Check pep8 linter requirements
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py',
                                        'tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def testInit(self):
        """
        Test and setup of an object instance of Review
        and validates it is an instance
        """
        self.new_instance = Review()
        self.assertIsInstance(self.new_instance, Review)

    def testId(self):
        """
        Test that UUID is working correctly
        """
        self.new_review_1 = Review()
        self.new_review_2 = Review()
        self.assertNotEqual(self.new_review_1.id,
                            self.new_review_2.id)

    def testCreate(self):
        """
        Test that created_at is wroking correctly
        """
        self.create_1 = Review()
        self.create_2 = Review()
        self.assertNotEqual(self.create_1.created_at, self.create_2.created_at)

    def testSave(self):
        """
        Test that save method is working correctly
        """
        self.save_review = Review()
        self.before_save = self.save_review.updated_at
        self.save_review.save()
        self.after_save = self.save_review.updated_at
        self.assertNotEqual(self.before_save, self.after_save)

    def testUpdate(self):
        """
        Test that update method does not affect created_at date by
        comparing the different dates on the same file
        """
        self.update_review = Review()
        self.before_update = self.update_review.created_at
        self.update_review.save()
        self.after_update = self.update_review.created_at
        self.assertEqual(self.before_update, self.after_update)

    def testDict(self):
        """
        Checks if method retuns a dictionary by
        comparing a predefined one to entered one
        """
        self.my_review = Review()
        self.dictionary = dict(self.my_review.__dict__)
        self.dictionary['__class__'] = "Review"
        self.dictionary['created_at'] =\
            self.dictionary['created_at'].isoformat()
        self.dictionary['updated_at'] =\
            self.dictionary['updated_at'].isoformat()
        self.assertDictEqual(self.dictionary, self.my_review.to_dict())

if __name__ == '__main__':
    unittest.main()
