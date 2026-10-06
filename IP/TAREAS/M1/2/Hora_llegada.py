# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:03:45 2026

@author: blanc
"""

def calcular_horario_llegada(hora_salida: int, minuto_salida: int, segundo_salida: int, duracion_horas: int, duracion_minutos: int, duracion_segundos: int)->str:
    
   segundos_llegada = (segundo_salida + duracion_segundos) % 60
   residuo_segundos = (segundo_salida + duracion_segundos) // 60
   
   minutos_llegada = (minuto_salida + duracion_minutos + residuo_segundos) % 60
   residuo_min = (minuto_salida + duracion_minutos + residuo_segundos) // 60

   horas_llegada = (hora_salida + duracion_horas + residuo_min) % 24
   
   return str(horas_llegada) + ':' +str(minutos_llegada)  + ':' + str(segundos_llegada)

print(calcular_horario_llegada(15, 59, 32,8, 31, 58))