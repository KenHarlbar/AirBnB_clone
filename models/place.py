#!/usr/bin/python3
""" Module for class Place """

from models.base_model import BaseModel


class Place(BaseModel):
    """ class that defines all Amenity instances

    Args:
        city_id: string - empty string: it will be the City.id
        user_id: string - empty string: it will be the User.id
        name:
        description:
        number_rooms:
        number_bathrooms:
        max_guest:
        price_by_night:
        latitude:
        longitude:
        amenity_ids: list of string
    """

    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
