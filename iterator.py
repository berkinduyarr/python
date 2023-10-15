# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 01:30:50 2023

@author: Berkin
"""

sehirler = ["Ankara","İstanbul","İzmir","Van"]

iteratorum = iter(sehirler)

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))

for sehir in sehirler:
    print(sehir)


