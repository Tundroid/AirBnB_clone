#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = uuid.uuid4()
            self.created_at = self.updated_at = datetime.now()
        else:
            self.id = kwargs["id"]
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.update_at = datetime.fromisoformat(kwargs["updated_at"])

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict

