#!/usr/bin/python3
import uuid
import datetime
import json
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
    def __init__(self):
        """
        Initializes the BaseModel class
        Attributes:
        name (str): name of the user
        my_number (int): id number
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """
        String rep of a class
        """
        return "[" + self.__class__.__name__ + "]"+ "(" + self.id + ")" +\
            str(self.__dict__)

    def save(self):
        """
        Saves an objec to  a JSON file
        """
        updated_at = datetime.datetime.now().isoformat()

    def to_dict(self):
        dict = self.__dict__
        dict["__class__"] = self.__class__.__name__
        return self.__dict__
