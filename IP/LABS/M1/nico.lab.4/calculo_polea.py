# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 16:39:42 2026

@author: blanc
"""

def calcular_aceleracion_polea_libre(masaM: float, masam: float) -> float:
    
    gravedad = 9.8
    
    
    pesoM = masaM * gravedad
    
    
    pesom = masam * gravedad
    
    
    
    acele = (pesoM - pesom) / (masaM + masam)
    
    return acele


def calcular_tension_polea_libre(masaM: float, masam: float) -> float:
    
    gravedad = 9.8
   
    aceleracion = calcular_aceleracion_polea_libre(masaM, masam)
    
    
    tension = masam * (aceleracion + gravedad)
    
    
    return tension
                                  