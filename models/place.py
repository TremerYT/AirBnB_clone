#!/usr/bin/python3
"""This defines a class for a place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This is the place class"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_room = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
