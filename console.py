#!/usr/bin/python3
"""
This module is the console for the AirBnB clone
"""
import cmd
import json
from models import storage
from models.base_model import BaseModel
import re
import shlex


class HBNBCommand(cmd.Cmd):
    """
    This is our console class
    """
    prompt = "(hbnb) "

    @staticmethod
    def val_get_key(arg):
        """
        Validates and returns object Key if in existance
        """

        l_arg = arg.split()
        cnt = len(l_arg)
        key = None
        tmp_key = None
        if not arg:
            print("** class name missing **")
        elif l_arg[0] not in storage.classes:
            print("** class doesn't exist **")
        elif cnt < 2:
            print("** instance id missing **")
        else:
            l_arg[1] = l_arg[1].strip('"')
            tmp_key = '.'.join(l_arg[0:2])
            if tmp_key not in storage.all():
                print("** no instance found **")
            else:
                key = tmp_key
        return key

    def do_create(self, arg):
        """
        Creates a new class instance, if sucessful it prints the ID of
        the new instance.

        Usage: create <class_name>"
        """
        if not arg:
            print("** class name missing **")
        elif arg in storage.classes:
            new_obj = storage.classes[arg]()
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Shows the string representation of an instance based on the
        given Class and ID

        Usage: show <class_name>
        """
        key = HBNBCommand.val_get_key(arg)
        if key:
            print(storage.all()[key])

    def do_all(self, arg):
        """
        Prints all objects of a certain type, or all objects if no Class
        was specified.

        Usage: all <class name>
             : <class name>.all()
        """
        cls = arg.split()
        if not arg:
            for i in storage.all().values():
                print(i)
        elif cls[0] in storage.classes:
            for k, v in storage.all().items():
                if k[0: k.index('.')] == cls[0]:
                    print(v)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Destroys/deletes an instance based on the Class and the ID

        Usage: destroy <class_name>"
        """
        key = HBNBCommand.val_get_key(arg)
        if key:
            del storage.all()[key]
            storage.save()

    def do_update(self, arg):
        """
        Updates an instance based on the Class name and ID by adding
        or updating an attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        key = HBNBCommand.val_get_key(arg)
        if key:
            l_arg = arg.split()
            if len(l_arg) < 3:
                print("** attribute name missing **")
            elif len(l_arg) < 4:
                print("** value missing **")
            else:
                att_name, value = l_arg[2:4]

                if value[0] == '"':
                    value = " ".join(l_arg[3:])
                    value = value[1:]
                    if '"' in value:
                        value = value[0: value.index('"')]
                obj = storage.all()[key]
                if att_name in obj.__dict__:
                    cls = type(obj.__dict__[att_name])
                    value = cls(value)
                setattr(obj, att_name, value)
                obj.save()

    def emptyline(self):
        """
        Empties the prompt
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")

    def do_quit(self, arg):
        """
        Exits the program using quit command

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        Exits the program using EOF command
        """
        print()
        return True

    patterns = {'all': re.compile('.*'),
                'count': re.compile('.*'),
                'show': re.compile('.*'),
                'destroy': re.compile('.*')}

    """-------------ADVANCE TASKS-----------------"""

    def default(self, arg):
        """
        Overwtrites the default method when an input to the prompt
        is not reconognized, validates
        """
        if '.' in arg:
            cls = arg[0:arg.index('.')]
            if cls in storage.classes and '(' in arg and ')' in arg:
                cmnd = arg[arg.index('.') + 1: arg.index('(')]
                if cmnd in self.patterns:
                    to_match = arg[arg.index('(') + 1: arg.index(')')]
                    if to_match:
                        match = self.patterns[cmnd].match(to_match)
                        if match:
                            self.onecmd(' '.join([cmnd, cls, match.group()]))
                            return
                    elif arg.index('(') < arg.index(')'):
                        self.onecmd(cmnd + ' ' + cls)
                        return

        print("*** Unknown syntax: " + arg)

    def do_count(self, arg):
        """
        Retrieves the number of instances of a class.

        Usage: count <class name>
             : <class name>.count()
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] in storage.classes:
            cnt = 0
            for k in storage.all().keys():
                if k[0: k.index('.')] == args[0]:
                    cnt += 1
            print(cnt)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
