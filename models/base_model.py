#!/usr/bin/python3
import uuid
from datetime import datetime
from models.__init__ import storage

"""
This module contains the BaseModel class
Attributes:
id (UUID): string with UUID
created_at (datetime): date and time created
updated_at (datetime): date and time updated
"""


class BaseModel():
    """
    BaseModel class
    Attributes:
    id (UUID): string holdin UUID
    created_at (datetime): date created
    updated_at (datetime): date updated
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class
        Attributes:
        name (str): name of the user
        my_number (int): id number
        """
        if len(kwargs) == 0:

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for k, v in kwargs.items():
                self.__dict__[k] = v
            del self.__dict__['__class__']
            self.__dict__['created_at'] = datetime.strptime(
                    self.__dict__['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__['updated_at'] = datetime.strptime(
                    self.__dict__['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """
        String rep of a class
        """
        return "[" + self.__class__.__name__ + "]" + "(" + self.id + ")" +\
            str(self.__dict__)

    def save(self):
        """
        Saves an objec to  a JSON file
        """
        storage.save()
        updated_at = datetime.now().isoformat()

    def to_dict(self):
        """
        returns a dictionary with all keys and values of __dict__
        also adds key class to the dictionary with class name
        """
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
