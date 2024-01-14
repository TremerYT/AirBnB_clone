#!/usr/bin/python3
"""This Defines the BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This represents the BaseModel of the HBNB project"""

    def __init__(self, *args, **kwargs):
        """This initializes a new BaseModel
        Args:
            *args: This is unused.
            **kwargs (dict): This is the key pairs of the attributes
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "created_at" or j == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, time_format)
                else:
                    self.__dict__[i] = j
        else:
            models.storage.new(self)

    def save(self):
        """This Updates the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """This should return the dictionary of the BaseModel instance.
        This includes the key pair__class__ reps
        the class name of the object.
        """
        diction = self.__dict__.copy()
        diction["created_at"] = self.created_at.isoformat()
        diction["updated_at"] = self.updated_at.isoformat()
        diction["__class__"] = self.__class__.__name__
        return diction

    def __str__(self):
        """This returns the print of the representation of the BaseModel"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
