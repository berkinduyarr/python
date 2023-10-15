# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 01:03:35 2023

@author: Berkin
"""

try:
    sayi = int(input("Sayı giriniz"))
except (ValueError,ZeroDivisionError):
    print("Tip uyuşmazlığı : Lütfen sayı giriniz")
except ZeroDivisionError:
    print("Payda sıfır olamaz")
except:
    print("Bir hata oluştu")
    
print("Bitti")