# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 07:32:31 2026

@author: blanc
"""

def retorno(num: int)-> dict:
    
    numero = {}
    
    num = str(num)
    
    cero = num.count('0')    
    uno = num.count('1')    
    dos = num.count('2')    
    tres = num.count('3')    
    cuatro = num.count('4')    
    cinco = num.count('5')    
    seis = num.count('6')    
    siete = num.count('7')    
    ocho = num.count('8')    
    nueve = num.count('9')    
    
    if cero > 0:
        numero ['0'] = cero
    if uno > 0:
        numero ['1'] = uno
    if dos > 0:
        numero ['2'] = dos
    if tres > 0:
        numero ['3'] = tres
    if cuatro > 0:
        numero ['4'] = cuatro
    if cinco > 0:
        numero ['5'] = cinco
    if seis > 0:
        numero ['6'] = seis
    if siete > 0:
        numero ['7'] = siete
    if ocho > 0:
        numero ['8'] = ocho
    if nueve > 0:
        numero ['9'] = nueve 
    return numero
        