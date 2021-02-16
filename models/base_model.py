#!/usr/bin/python3
import uuid
from datetime import datetime
import models
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
    id (UUID): string holding UUID
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
            models.storage.new(self)
        else:
            del kwargs['__class__']
            kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """
        String rep of a class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Saves an objec to  a JSON file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary with all keys and values of __dict__
        also adds key class to the dictionary with class name
        """
        adict = self.__dict__.copy()
        adict["__class__"] = self.__class__.__name__
        adict["created_at"] = self.created_at.isoformat()
        adict["updated_at"] = self.updated_at.isoformat()
        return adict
