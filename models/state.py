#!/usr/bin/python3
"""
state class
"""
from models.base_model import BaseModel

class State(BaseModel):
    """
    state subclass of BaseModel
    """
    def __init__(self):
        """ initializer """
        name = ""
