#!/usr/bin/env python3
""" Module for base model """

from datetime import datetime
import uuid
import models


class BaseModel:
    """ class BaseModel that defines all common attributes/methods
    for other classes """

    def __init__(self, *args, **kwargs):
        """ Initializes the instance """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            self.id = kwargs["id"]
            self.created_at = datetime.fromisoformat(kwargs["created_at"])
            self.updated_at = datetime.fromisoformat(kwargs["updated_at"])
        models.storage.new(self)

    def __str__(self):
        """ Returns string representation of instance """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Updates the public instance attribute updated_at """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values
        of __dict__ of the instance """

        return_dict = self.__dict__.copy()
        return_dict["__class__"] = self.__class__.__name__
        return_dict["created_at"] = self.created_at.\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
        return_dict["updated_at"] = self.updated_at.\
            strftime("%Y-%m-%dT%H:%M:%S.%f")
        return return_dict
