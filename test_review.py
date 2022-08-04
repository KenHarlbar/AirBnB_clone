#!/usr/bin/env python3
from models import storage
from models.review import Review

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)
print()

print("-- Create a new Review --")

print()

print("-- Create a new Review 2 --")
print()
