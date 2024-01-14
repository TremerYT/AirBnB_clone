#!/usr/bin/python3
"""This defines a place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This represents a place.

    Attributes:
        city_id: This is the city id
        user_id: This is the user id
        name: This is the name of the place
        description: This is the description of the place
        number_rooms: This is the number of rooms
        number_bathrooms: This is the number of bathrooms
        max_guest: This is the amount of guest to hold
        price_by_night: This is the price per night
        latitude: This is the latitude of the place
        longitude: This is the longitude of the place
        amenity_ids: This is the list of amenities
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
