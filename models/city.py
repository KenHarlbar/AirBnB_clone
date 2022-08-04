#!/usr/bin/env python3
""" Module for City """

from models.base_model import BaseModel


class City(BaseModel):
    """ Class for all state objects

    Args:
        state_id - state ID
        name - name of city
    """

    state_id = ""
    name = ""
