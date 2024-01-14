#!/usr/bin/python3
"""This defines the City class"""
from models.base_model import BaseModel


class city(BaseModel):
    """This should Represent a city
    
    Attributes:
        state_id: This isthe state id
        name: This is the name of the city
    """

    state_id = ""
    name = ""