#!/usr/bin/python3
"""
This module is the console for the AirBnB clone
"""
import cmd
import sys
import os
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    This is our console class
    """
    prompt = "(hbnb) "

    """
    def do_help(self, arg):

        Prints a help command to help user navigate

        if not arg:
            print()
            print("Documented commands (type help <topic>):")
            print("=========================================")
            print("EOF " + " help " + " quit")
            print("create " + " update " + " destroy ")
            print("update " + "all")
            print()
        try:
            topic = getattr(self, "help_" + arg)
            return topic()
        except AttributeError:
            pass
        else:
            if sys.flags.optimize >= 2:
                return
    """

    @staticmethod
    def val_get_key(arg):
        """Validates and returns object Key if in existance
        """

        l_arg = arg.split()
        cnt = len(l_arg)
        key = None
        if not arg:
            print("** class name missing **")
        elif l_arg[0] not in storage.classes:
            print("** class doesn't exist **")
        elif cnt < 2:
            print("** instance id missing **")
        elif '.'.join(l_arg[0:2]) not in storage.all():
            print("** no instance found **")
        else:
            key = '.'.join(l_arg[0:2])
        return key

    def do_create(self, arg):
        """
        Create a new instance of BaseModel or that isnherits from BaseModel
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

    def help_create(self):
        """
        Prints help screen for create command
        """
        print("Create command to create new class instance")
        print("Usage: create <class_name>")
        print()

    def do_show(self, arg):
        """
        print string representation of instance based on class and id
        """
        key = HBNBCommand.val_get_key(arg)
        if key:
            print(storage.all()[key])

    def help_show(self):
        """
        Prints help screen for show command
        """
        print("Show command to show string rep of an instance")
        print("Usage: show <class_name>")
        print()

    def do_all(self, arg):
        """
        prints all objects of a certain type, or all objects if none specified
        """
        if not arg:
            for i in storage.all().values():
                print(i)
        elif arg in storage.classes:
            for k, v in storage.all().items():
                if k[0: k.index('.')] == arg:
                    print(v)
        else:
            print("** class doesn't exist **")

    def help_all(self):
        """
        Prints help screen for show command
        """
        print("All command to print all objects of a certain type or all"
              " objects")
        print("Usage: all <object>")
        print()

    def do_destroy(self, arg):
        """
        Deletes an instance based on the Class and the ID
        """
        key = HBNBCommand.val_get_key(arg)
        if key:
            del storage.all()[key]
            storage.save()

    def help_destroy(self):
        """
        Prints help screen for destroy command
        """
        print("Destroy command to destroy/delete an instance of "
              "a class and id")
        print("Usage: destroy <class_name>")
        print()

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute
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
                    value = value[1:]
                    if value[-1] == '"':
                        value = value[0:-1]
                obj = storage.all()[key]
                if att_name in obj.__dict__:
                    cls = type(obj.__dict__[att_name])
                    value = cls(value)
                setattr(obj, att_name, value)
                obj.save()

    def help_update(self):
        """
        Prints help screen for update command
        """
        print("Update command to update/add to instance")
        print("Usage: update <class_name> <id>")
        print()

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
        """
        return True

    def help_quit(self):
        """
        Prints help screen for quit command
        """
        print("Quit command to exit the program")
        print()

    def do_EOF(self, arg):
        """
        Exits the program using EOF command
        """
        print()
        return True

    def help_EOF(self):
        """
        Prints help screen for EOF command
        """
        print("EOF command to exit the program")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
