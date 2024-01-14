#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel

class amenity(BaseModel):
    """This is used to represent the amenity.
    
    Attributes:
        name: This is the name of the amenity
    """
    
    name = ""