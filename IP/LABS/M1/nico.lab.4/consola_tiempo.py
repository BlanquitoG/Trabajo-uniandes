# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 06:59:36 2026

@author: n.blancoc2
"""

import tiempo_nascar as te

def la_mahestuosa_cantidad_de_tiempo_flipante():
    
    eje_mayor = float(input("Digite su eje mayor de la pista: "))
    
    eje_menor = float(input("Digete su eje menor de la pista: "))
    
    vel = float(input("Ingrese su velociada en km/h: "))
    
    tiempo_demorado = te.calc_temp(eje_mayor, eje_menor, vel)
    
    print("Usted se demoro", tiempo_demorado, "minutos")
    
la_mahestuosa_cantidad_de_tiempo_flipante()