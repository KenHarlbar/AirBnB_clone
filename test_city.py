#!/usr/bin/env python3
from models import storage
from models.city import City
from models.state import State

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new City --")
my_city = City()
my_state = State()
my_city.name = "Atiba"
my_state.name = "Oyo"
my_city.state_id = str(my_state.id)
my_city.save()
print(my_city)
print()

print("-- Create a new City 2 --")
my_city2 = City()
my_state2 = State()
my_city2.name = "Ojodu"
my_state2.name = "Lagos"
my_city2.state_id = str(my_state2.id)
my_city2.save()
print(my_city2)
print()
