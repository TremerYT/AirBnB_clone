#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This is a class for the user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
