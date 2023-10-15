# -*- coding: utf-8 -*-
"""
Created on Wed May 31 00:50:14 2023

@author: Berkin
"""

#sehir = "Ankara"

#print(sehir.upper())
#print(sehir.endswtih("a"))

def selamVer(isim):
    print("Merhaba " + isim)
    
    
selamVer("Engin")    

def selamVer2(isim = "ziyaretçi ", soyİsim = "arkadaş"):
    print("Merhaba " + isim + soyİsim)
    
selamVer2("Derin ")
selamVer2("Engin ","Demiroğ ")


def dikUcgenAlaniHesapla(a,b):
    return a*b/2
alan = dikUcgenAlaniHesapla(2,3)
print(alan)

dikUcgenAlaniHesapla2 = lambda a,b : a*b/2

print(dikUcgenAlaniHesapla2(3,6))

print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2

print(x(4,5))
