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
    prompt = "(hbnb)"

    def do_help(self, arg):
        """
        Prints a help command to help user navigate
        """
        if not arg:
            print()
            print("Documented commands (type help <topic>):")
            print("=========================================")
            print("EOF " + " help " + " quit")
            print()
        try:
                topic = getattr(self, "help_" + arg)
                return topic()
        except AttributeError:
            pass
        else:
            if sys.flags.optimize >= 2:
                return

    def do_create(self, arg):
        """
        Create a new instance of BaseModel or that isnherits from BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg in storage.my_classes.keys():
            new_obj = storage.my_classes[arg]()
            storage.new(new_obj)
            storage.save()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def emptyline(self):
        """
        Empties the prompt
        """
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")

    def postloop(self):
        """
        Print empty line post cmd loop
        """
        print(end="")

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
        print("EOF")
        return True

    def help_EOF(self):
        """
        Prints help screen for EOF command
        """
        print("EOF command to exit the program")
        print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
