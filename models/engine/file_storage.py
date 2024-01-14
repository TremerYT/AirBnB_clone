#!/usr/bin/python3
"""This Defines the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This represents an abstracted storage engine

    Attributes:
        __file_path (str): This is the name of the file to save the objects
        __objects (dict): This is a dictionary of objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This should return the dictionary objects"""
        return FileStorage._objects

    def new(self, obj):
        """This sets in objects with key"""
        object_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_class_name, obj.id)] = obj

    def save(self):
        """This should serialize objects to the JSON file"""
        obj_dic = FileStorage.__objects
        object_dic = {obj: obj_dic[obj].to_dict() for obj in obj_dic.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(object_dic, f)

    def reload(self):
        """This deserializes the JSON file to objects if it exists"""
        try:
            with open(FileStorage.__file_path) as f:
                object_dictionary = json.load(f)
                for i in object_dictionary.values():
                    class_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(class_name)(**i))
        except FileNotFoundError:

            return
