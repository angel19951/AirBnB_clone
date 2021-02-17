#!/usr/bin/python3
"""
Unit testing for console.py
"""
from console import HBNBCommand
import sys
import io
import console
import unittest
import pep8
import cmd


class TestConsole(unittest.TestCase):
    """
    test console code with unit testing
    """
    def testPep8(self):
        """
        check pep8 compliance in console.py as well as unittests
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py',
                                        'tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def testHelp(self):
        """
        Test the help command
        """
        input = 'help'
        assert HBNBCommand(input)

    def create(self):
        """
        creates a console instance
        """
        return HBNBCommand()

    def testEOF(self):
        """
        checks if EOF command is valid
        """
        my_console = self.create()
        assert HBNBCommand(my_console.onecmd("EOF"))

    def testQuit(self):
        """
        checks if quit command is valid
        """
        my_console = self.create()
        assert HBNBCommand(my_console.onecmd("quit"))

    def testDestroy(self):
        """
        checks if destroy command is valid
        """
        my_console = self.create()
        assert HBNBCommand(my_console.onecmd("destroy"))

    def testUpdate(self):
        """
        checks if update command is valid
        """
        my_console = self.create()
        assert HBNBCommand(my_console.onecmd("update"))

if __name__ == '__main__':
    unittest.main()
