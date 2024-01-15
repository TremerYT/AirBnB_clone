#!/usr/bin/python3
"""This is a class for reviews"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This is a review class"""
    place_id = ""
    user_id = ""
    text = ""
