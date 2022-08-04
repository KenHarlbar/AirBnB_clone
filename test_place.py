#!/usr/bin/env python3
from models import storage
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity as Am

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
print()

print("-- Create a new City --")
my_place = Place()
my_city = City()
my_state = State()
my_amenity = Am()
my_city.name = "Ikeja"
my_state.name = "Lagos"
my_city.state_id = str(my_state.id)
my_amenity.name = "Free Wifi"
my_place.city_id = my_city.id
my_place.name = "Balo Hub"
my_place.description = "Lorem Ipsum Chockolate Sinsum, Mako cheese drip trop"
my_place.number_rooms = 1
my_place.number_bathrooms = 1
my_place.price_by_night = 50
my_place.max_guest = 2
my_place.latitude = 120.45
my_place.longitude = 270.54
my_place.amenity_ids.append(str(my_amenity.id))
my_place.save()
print(my_place)
print(my_place.amenity_ids)
print()
