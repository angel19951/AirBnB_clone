#!/usr/bin/python3
# This modul recreates a BaseModel from another one by using a
# dictionary representation.
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file
    to instances
    """
    __file_path = 'file.json'
    __objects = dict()
    my_classes = {'BaseModel': BaseModel, "Amenity": Amenity, "City": City,
                  'State': State, "Place": Place, "Review": Review}

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
        dict_add = {}
        with open(self.__file_path, 'w') as file:
            for k, v in self.__objects.items():
                dict_add[k] = v.to_dict()
            json.dump(dict_add, file)

            """json.dump(self.__objects, file)"""

    def reload(self):
        """Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                aux_dict = json.load(file)
                self.__objects = {}
                for k, att_dict in aux_dict.items():
                    model = self.my_classes[k[0: k.index('.')]]
                    self.__objects[k] = model(**att_dict)
        except FileNotFoundError:
            pass
