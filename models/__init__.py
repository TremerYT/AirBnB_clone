#!/usr/bin/python3
"""__init__ method found in models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()