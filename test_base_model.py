#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
print(my_model)
print("\nTesting to_dict...\n")
print(my_model.to_dict())
print("\Printing model again...\n")
print(my_model)