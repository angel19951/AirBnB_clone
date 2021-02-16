#!/usr/bin/python3
"""
Defines User class that inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user subclass of BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
