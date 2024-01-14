#!/usr/bin/python3
"""This is used Review class."""
from models.base_model import BaseModel


class review(BaseModel):
    """This is used to represent a review
    
    Attributes:
        place_id: This is the id of the place
        user_id: This is the id of the use
        text: This is the text of the review
    """
    place_id = ""
    user_id = ""
    text = ""