#!/usr/bin/python3
"""This defines filestorage class"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import json


class FileStorage:
    """This is the file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This returns the dict"""
        return FileStorage.__objects

    def new(self, obj):
        """This set in __object"""
        object_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_name, obj.id)] = obj

    def save(self):
        """This serializes"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """This Deserialize."""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for i in objdict.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))
        except FileNotFoundError:
            return
