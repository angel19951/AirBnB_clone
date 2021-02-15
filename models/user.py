#!/usr/bin/python3
"""
city class
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
