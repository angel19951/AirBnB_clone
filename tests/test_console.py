#!/usr/bin/python3
"""
Unit testing for console.py
"""
from console import HBNBCommand
import sys
from io import StringIO
import console
import unittest
import pep8
from models import classes
from unittest.mock import patch, create_autospec
import os
from models import storage


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

    def setUp(self):
        """
        Sets ups the Test console Unittest by catching in/output
        with a mock object
        """
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def session(self):
        """
        creates a console instance
        """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def testEOF(self):
        """
        checks if EOF command is valid
        """
        my_console = self.session()
        assert HBNBCommand().onecmd("EOF")

    def testQuit(self):
        """
        checks if quit command is valid
        """
        my_console = self.session()
        assert HBNBCommand(my_console.onecmd("quit"))

    def test_create(self):
        """
        Test that create throws proper errors + works w all classes
        """
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create asgshsd"))
            self.assertEqual(out.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(out.getvalue(), "** class name missing **\n")
        for cls in classes:
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("create {}".format(cls))
                self.assertTrue(len(str(out.getvalue())) == 37)

    def testDestroy(self):
        """
        tests existence of destroy method and validates
        error messages
        """
        my_console = self.session()
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy"))
            self.assertEqual(out.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy Jared"))
            self.assertEqual(out.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy BaseModel"))
            self.assertEqual(out.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("destroy BaseModel 555-ddd"))
            self.assertEqual(out.getvalue(), "** no instance found **\n")
        for cls in classes.keys():
            obj = classes[cls]()
            key = ".".join([cls, obj.id])
            storage.all()[key] = obj
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("destroy {} {}".format(cls, obj.id))
                self.assertEqual(out.getvalue(), '')
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("show {} {}".format(cls, obj.id))
                self.assertEqual("** no instance found **\n", out.getvalue())
        for cls in classes.keys():
            obj = classes[cls]()
            key = ".".join([cls, obj.id])
            storage.all()[key] = obj
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd('{}.destroy("{}")'.format(cls, obj.id))
                self.assertEqual(out.getvalue(), '')
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("show {} {}".format(cls, obj.id))
                self.assertEqual("** no instance found **\n", out.getvalue())

    def testUpdate(self):
        """
        checks if update command is valid.
        validates all method error messages
        """
        my_console = self.session()
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("update"))
            self.assertEqual(out.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("update Jared"))
            self.assertEqual(out.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("update BaseModel"))
            self.assertEqual(out.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as out:
            self.assertFalse(my_console.onecmd("update BaseModel 4444-"))
            self.assertEqual(out.getvalue(), "** no instance found **\n")

    def testCount(self):
        """
        test that count command returns appropriate val
        """
        for k in classes.keys():
            count = 0
            for c in storage.all():
                if k in c:
                    count += 1
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("{}.count()".format(k))
                self.assertEqual(int(out.getvalue().strip()), count)

    def testShow(self):
        """
        test that validates show command
        """
        for k in classes.keys():
            obj = classes[k]()
            storage.all()[".".join([k, obj.id])] = obj
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd("show {} {}".format(k, obj.id))
                self.assertEqual(str(obj) + '\n', out.getvalue())
            with patch('sys.stdout', new=StringIO()) as out:
                HBNBCommand().onecmd('{}.show("{}")'.format(k, obj.id))
                self.assertEqual(str(obj) + '\n', out.getvalue())

    def testDocString(self):
        """
        checks if console module is documented.
        also checks all module methods for documentation
        """
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(HBNBCommand.do_create.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.val_get_key.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_show.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_all.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_destroy.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_update.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.emptyline.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_quit.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_EOF.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.default.__doc__) > 1)
        self.assertTrue(len(HBNBCommand.do_count.__doc__) > 1)


if __name__ == '__main__':
    unittest.main()
