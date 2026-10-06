# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 10:09:56 2026

@author: blanc
"""

import calculo_polea as ca

def el_flipante_calclulo_de_tensionxd():
    
    masa_mayor = float(input('Ingrese el valor de la masa mayor: '))
    
    masa_menor =  float(input('Ingrese el valor de la masa menor:  '))
    
   
    tension = ca.calcular_tension_polea_libre(masa_mayor, masa_menor)
    
    print(f'La tension de la polea es {tension} N')
    
el_flipante_calclulo_de_tensionxd()