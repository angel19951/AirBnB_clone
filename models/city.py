#!/usr/bin/python3
"""
city class
"""
from models.base_model import BaseModel

class City(BaseModel):
    """
    city subclass of BaseModel
    """
    def __init__(self):
        """ initializer """
        state_id = ""
        name = ""
