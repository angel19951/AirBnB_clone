#!/usr/bin/python3
"""
amenity class
"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    amenity subclass of BaseModel
    """
    def __init__(self):
        """initializer"""
        name = ""
