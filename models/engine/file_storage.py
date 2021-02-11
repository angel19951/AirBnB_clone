#!/usr/bin/python3
# This modul recreates a BaseModel from another one by using a
# dictionary representation.
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances
    """
    __file_path = None
    __objects = dict()

    def __init__(self, *args, **kwargs):
        """Initializer
        """

    def all(self):
        """Returns the dictionary
        """
        return self.__objects

    def new(self, obj):
        """Adds object to the dictionary
        Args:
            obj: object to add
        """
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)
        """

        with open(__file_path, 'w') as file:
            json.dump(__objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        with open(__file_path, 'r') as file:
            __objects = json.load(file)
