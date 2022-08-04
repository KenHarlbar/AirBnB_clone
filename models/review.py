#!/usr/bin/env python3
""" Module for Review """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Class for all state objects

    Args:
        place_id: Place.id
        user_id: User.id
        text: the actual review
    """
    place_id = ""
    user_id = ""
    text = ""
