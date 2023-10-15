# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:26:26 2023

@author: Berkin
"""

import json

data = '{"firstName":engin","lastName":demiroğ"}'

y = json.loads(data)

type(y)

print(y["firstName"])
print(y["firstName"])

customer = {
    "firstName":"engin",
    "email":"engindemirog@gmail.com"
    }

customerJson = json.dumps(customer)
print(customer)

print(json.dumps("Engin"))
