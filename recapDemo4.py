# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 22:10:21 2023

@author: Berkin
"""

ogrenciler = ["Engin","Derin","Salih","Ali","Ayşe"]

fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
fileToAppend.close()
