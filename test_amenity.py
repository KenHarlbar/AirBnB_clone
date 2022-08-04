#!/usr/bin/env python3
from models import storage
from models.amenity import Amenity as Am

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new City --")
my_ame = Am()
my_ame.name = "Personal Car"
my_ame.save()
print(my_ame)
print()

print("-- Create a new City 2 --")
my_ame2 = Am()
my_ame2.name = "Free Wifi"
my_ame2.save()
print(my_ame2)
print()
