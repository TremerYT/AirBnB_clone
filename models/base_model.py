#!/usr/bin/python3
"""This is the Base Models"""
import datetime
import uuid
import models


class BaseModel:
    """This is the class of the base model"""

    def __init__(self, *args, **kwargs):
        """This is the initialization"""
        if len(kwargs) != 0:
            self.id = kwargs["id"]
            self.created_at = datetime.datetime.fromisoformat(
                kwargs["created_at"])
            self.updated_at = datetime.datetime.fromisoformat(
                kwargs["updated_at"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def __str__(self):
        """This is a string rep"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """This is supposed to update time"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """This converts instance to a dictionary"""
        if isinstance(self.updated_at, datetime.datetime):
            self.updated_at = datetime.datetime.isoformat(self.updated_at)
        if isinstance(self.created_at, datetime.datetime):
            self.created_at = datetime.datetime.isoformat(self.created_at)
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__

        return result
