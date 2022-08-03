#!/usr/bin/env python3
""" Module for file storage """

import json
import os


class FileStorage:
    """ Serializes instances to a JSON file and
    deserializes JSON file to instances """

    def __init__(self):
        """ Initializes class """

        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ Returns: __objects """

        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key
        <obj class name>.id """

        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = \
            obj.__dict__

    def save(self):
        """ serializes __objects to the JSON file
        (path: __file_path) """

        with open(self.__file_path, 'a') as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        """ deserializes the JSON file to __objects """

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                dictionary = f.read()
            self.__objects = json.load(dictionary)
