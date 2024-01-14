#!/usr/bin/python3
"""This defines the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This represents  a state
    
    Attributes:
        name: This is the name of the state.
    """
    
    name = ""