#!/usr/bin/python3
"""
FileStorage module
Handles serialization and deserialization of model instances to JSON.
"""

import json
import os


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file back to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to storage dictionary.
        Key format: <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file.
        """
        obj_dict = {
            key: value.to_dict() for key, value in self.__objects.items()
        }
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f, indent=4)

    def reload(self):
        """
        Deserialize the JSON file back to __objects.
        If the file does not exist, do nothing.
        """
        if os.path.isfile(self.__file_path):
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.city import City
            from models.place import Place
            from models.amenity import Amenity
            from models.review import Review

            classes = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Place": Place,
                "Amenity": Amenity,
                "Review": Review,
            }

            try:
                with open(self.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        cls_name = value["__class__"]
                        if cls_name in classes:
                            self.__objects[key] = classes[cls_name](**value)
            except Exception:
                pass
