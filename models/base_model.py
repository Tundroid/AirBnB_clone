#!/usr/bin/python3
"""BaseModel module"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class implementation"""

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
