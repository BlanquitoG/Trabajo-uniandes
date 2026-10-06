# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:50:25 2026

@author: blanc
"""

def calcular_cambio(cambio: int) -> str:
    
    cant_quin = cambio // 500
    residuo_quin = cambio % 500

    cant_200 = residuo_quin // 200
    residuo_200 = residuo_quin % 200      

    cant_100 = residuo_200 // 100          
    residuo_100 = residuo_200 % 100       

    cant_50 = residuo_100 // 50            

    return str(cant_quin) + "," + str(cant_200) + "," + str(cant_100) + "," + str(cant_50)

print(calcular_cambio(1350))  