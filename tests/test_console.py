#!/usr/bin/python3
"""
Unit testing for console.py
"""
from console import HBNBCommand
import sys
import io
from io import StringIO
import console
import unittest
import pep8
import cmd
from models import classes
from unittest.mock import patch


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
    """
    def testHelp(self):

        Test the help command

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help"),
            self.assertEqual(f,
                         "Documented commands (type help <topic>): \n" +
                         "========================================\n" +
                         "EOF  all  count  create  destroy  help  quit  show" +
                         " update")
    """

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
        assert HBNBCommand().onecmd("EOF")

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
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand(my_console.onecmd("destroy"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand(my_console.onecmd("destroy Jared"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand(my_console.onecmd("destroy BaseModel"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand(my_console.onecmd("destroy BaseModel 555-ddd"))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def testUpdate(self):
        """
        checks if update command is valid
        """

        my_console = self.create()
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand(my_console.onecmd("update"))
            self.assertEqual(f.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand(my_console.onecmd("update Jared"))
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand(my_console.onecmd("update BaseModel"))
            self.assertEqual(f.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand(my_console.onecmd("update BaseModel 4444-"))
            self.assertEqual(f.getvalue(), "** no instance found **\n")

    def testDocString(self):
        """
        checks if console properly documented
        """
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "console.py needs a docstring")

if __name__ == '__main__':
    unittest.main()
