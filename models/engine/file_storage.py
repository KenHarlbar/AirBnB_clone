#!/usr/bin/env python3
""" Module for file storage """

import json
import os


class FileStorage:
    """ Serializes instances to a JSON file and
    deserializes JSON file to instances

    Args:
    __file_path - path to the JSON file
    __objects - dictionary - store all objects by
        <class name>.id
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns: __objects """

        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key
        <obj class name>.id """

        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file
        (path: __file_path) """

        try:
            my_dict = {}
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()

            with open(self.__file_path, 'w') as f:
                json.dump(my_dict, f)
        except TypeError:
            pass

    def reload(self):
        """ deserializes the JSON file to __objects """

        try:
            with open(self.__file_path, 'r') as f:
                for key, value in (json.load(f)).items():
                    self.__objects[key] = value
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
