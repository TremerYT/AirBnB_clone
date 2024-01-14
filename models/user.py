#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class user(BaseModel):
    """This represents a user

    Attributes:
        email: This is the email of the user
        password: This is the password of the user
        first_name: This is the first name of the user
        last_name: This is the last_name of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
