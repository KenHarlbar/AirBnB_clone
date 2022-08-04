#!/usr/bin/env python3
"""The User module"""

from .base_model import BaseModel


class User(BaseModel):
    """The User class to save users information"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
