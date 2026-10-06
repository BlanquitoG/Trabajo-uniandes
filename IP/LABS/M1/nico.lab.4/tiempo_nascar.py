# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 06:35:47 2026

@author: n.blancoc2
"""

def perime_pist(a: float, b: float) -> float:
    
    pi = 3.14159
    
    p1 = (3*(a+b))
    
    p2 = 3*a+b 

    p2_2 = (a+(3*b))
    
    p2_3 = (p2 * p2_2)** 0.5
    
    p_final = pi*( p1 - p2_3)
    
    return p_final


def calc_temp (a: float, b: float, vel_carr: float ) -> float:
    
    km = perime_pist(a, b)
    
    tiempo = km / vel_carr
    
    tiempo = tiempo *60
    
    tiempo = round( tiempo ,2)
    
        
    
    return tiempo
    
    
