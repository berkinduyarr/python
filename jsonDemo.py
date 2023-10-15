# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 22:37:24 2023

@author: Berkin
"""

import json

with open ("users.json") as users:
    data = json.load(users)
    
    for x in range(6):
        print(data[x]["username"])
        print(data[x]["email"])
        print(data[x]["address"]["street"])
        print(data[x]["address"]["geo"]["lat"])