#!/usr/bin/python3
"""
review class
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    Review subclass of BaseModel
    """
    def __init__(self):
        """ initializer """
        place_id = ""
        user_id = ""
        text = ""
