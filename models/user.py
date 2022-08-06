#!/usr/bin/python3
"""The User module"""

from .base_model import BaseModel


class User(BaseModel):
    """
    The User class that defines users attributes
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
