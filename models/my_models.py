#!/usr/bin/python3
"""
Defines a dict with all the classes from package model
that we would like to know of in order to reload in the engine or
to validate it exist if passed in the console.
"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.user import User


classes = {"BaseModel": BaseModel, "Amenity": Amenity, "City": City,
           "State": State, "Place": Place, "Review": Review,
           "User": User}
