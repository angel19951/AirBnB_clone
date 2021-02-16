#!/usr/bin/python3
"""
Defines Package 'models' and the shared variables
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
