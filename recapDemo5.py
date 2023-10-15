# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 01:18:39 2023

@author: Berkin
"""
import sys

liste = [7,'engin',0,3,"6"]

for x in liste:
    try:
        print("Sayı: " + str(x))
        sonuc = 1/int(x)
        print("Sonuç : " +str(sonuc))
    except ValueError:
        print(str(x)+ " bir sayı değil")
    except ZeroDivisionError:
        print(str(x)+ " için sıfıra bölme hatası")
    except:
        print(str(x) + " hesaplanamadı")
        print("Sistem diyor ki : " + str(sys.exc_info()[0]))
    finally:
        print("İşlemler bitti")

    
    