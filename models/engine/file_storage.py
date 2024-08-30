#!/usr/bin/python3
"""FileStorage Module"""

import json
from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review


class FileStorage():
    """FileStorage class implementation"""

    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            data = {key: obj.to_dict() for key, obj in self.__objects.items()}
            json.dump(data, file)

    def reload(self):
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                # read and remove leading and trailing whitespaces
                # this will prevent crashing if file.json exists and is empty
                file_content = file.read().strip()
                if len(file_content):
                    objects = json.loads(file_content)
                    for value in objects.values():
                        self.new(eval(value["__class__"])(**value))
        except FileNotFoundError:
            pass
