#!/usr/bin/python3
"""This is a module for a base class.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """This is the class of the base model for the project."""

    def __init__(self, *args, **kwargs):
        """This is the initialization of the class.

        Args:
            - *args: list of arguments but it is unused
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for k in kwargs:
                if k == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif k != "__class__":
                    self.__dict__[k] = kwargs[k]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """This returns i dont know"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """This updates the updated_at attribute """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This returns a dict."""

        my_diction = self.__dict__.copy()
        my_diction["__class__"] = type(self).__name__
        my_diction["created_at"] = my_diction["created_at"].isoformat()
        my_diction["updated_at"] = my_diction["updated_at"].isoformat()
        return my_diction