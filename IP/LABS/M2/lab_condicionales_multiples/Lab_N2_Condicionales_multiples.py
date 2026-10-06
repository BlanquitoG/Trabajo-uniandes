# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:52:10 2026

@author: Juan Oyuela
"""

"""

Laboratorio - Condicionales y Diccionarios
Nivel avanzado

Restricciones:
- No usar ciclos (for, while).
- No usar listas ni tuplas.
- No usar diccionarios anidados.
- No usar match.
- Las funciones deben retornar un diccionario.
- No modificar el diccionario recibido como parámetro.
"""


# ============================================================
# EJERCICIO 1
# EVALUACIÓN INTEGRAL DE UNA SOLICITUD DE CRÉDITO
# ============================================================


solicitud = {
        "nombre": "Laura Gómez",
        "edad": 34,
        "ingresos": 8500000,
        "gastos": 2800000,
        "deudas": 1500000,
        "puntaje": 720,
        "moras": 0,
        "antiguedad": 4,
        "producto": "VEHICULO"
    }



def evaluar_credito(solicitud: dict) -> dict:
    nombre = solicitud["nombre"]
        
    disponible = solicitud['ingresos'] - solicitud['gastos'] - solicitud['deudas'] # capacidad disponible
        
        #nivel de riesgo:
    if  solicitud['puntaje'] >= 750 and solicitud['moras'] == 0:
        riesgo = 'BAJO'
    elif solicitud['puntaje'] >=650 and solicitud['moras'] < 2:
        riesgo = "MEDIO"
    else:
        riesgo = "ALTO"
        
    if (riesgo == 'BAJO' or riesgo == 'MEDIO') and disponible >= 2000000\
            and solicitud['antiguedad']>=1 and solicitud['edad'] >= 21:
        decision = 'APROBADA'
    else:
        decision = 'RECHAZADA'
    
    
    
    if solicitud['puntaje'] < 550 or solicitud['moras'] >= 3 or solicitud['edad'] <18 or\
        solicitud['gastos'] + solicitud['deudas'] > solicitud['ingresos']:
        decision = 'RECHAZADA'
    
    if decision == 'APROBADA' and riesgo == 'BAJO':
        monto_base = disponible * 8
    elif decision == 'APROBADA' and riesgo == 'MEDIO':
            monto_base = disponible * 4
    else:
        monto_base = 0
    

     
    
    if solicitud['producto'] == 'VEHICULO' and monto_base <60000000:
        monto_aprobado = monto_base

    elif solicitud['producto'] == 'EDUCACION' and monto_base <40000000:
        monto_aprobado = monto_base
    
    elif solicitud['producto'] == 'LIBRE_INVERSION' and monto_base <40000000:
        monto_aprobado = monto_base
    
    elif solicitud['producto'] and monto_base <20000000:
        monto_aprobado = 0
         
   
        
    dictionari = {}
    
    dictionari['nombre'] = nombre

    dictionari['disponible'] = disponible

    dictionari['riesgo'] = riesgo

    dictionari['decision'] = decision

    dictionari['monto aprobado'] = monto_aprobado
    
    
    return dictionari


# ============================================================
# EJERCICIO 2
# SISTEMA DE ADMISIÓN Y ASIGNACIÓN DE BECAS
# ============================================================
aspirante = {
    "nombre": "Daniel Rojas",
    "matematicas": 88,
    "lenguaje": 74,
    "ingles": 91,
    "entrevista": 82,
    "estrato": 3,
    "sanciones": 0,
    "programa": "INGENIERIA",
    "solicita_beca": True
}

def evaluar_aspirante(aspirante: dict) -> dict:
    """
    Evalúa la admisión, nivel académico y posibilidad de beca
    de un aspirante.

    Parámetros:
        aspirante (dict): información académica y personal
                          del aspirante.

    Retorno:
        dict: resultado de la evaluación.
    """

    # --------------------------------------------------------
    # 1. Recuperar la información del diccionario
    # --------------------------------------------------------

    nombre = aspirante["nombre"]

    # Complete la recuperación de los demás datos necesarios.

    puntaje = (aspirante['matematicas'] * 0.35 ) + (aspirante['lenguaje'] * 0.20) + (aspirante['ingles'] * 0.20) + \
        (aspirante['entrevista'] * 0.25)
   



    if aspirante['programa'] == 'INGENIERIA':
        if puntaje >= 78 and aspirante["matemáticas"] >= 75:
            estado = 'ADMITIDO'
        else:
            estado = 'NO ADMITIDO'
    if aspirante['programa'] == 'ECONOMIA':
        if puntaje >= 76 and aspirante["matemáticas"] >= 70 and aspirante['lenguaje'] >= 70:
            estado = 'ADMITIDO'
        else:
            estado = 'NO ADMITIDO'
    if aspirante['programa'] == 'DERECHO':
        if puntaje >= 75 and aspirante['lenguaje'] >= 78:
            estado = 'ADMITIDO'
        else:
            estado = 'NO ADMITIDO'
    if aspirante['programa']:
        if puntaje >= 72:
            estado = 'ADMITIDO'
        else:
            estado = 'NO ADMITIDO'
    if aspirante["sanciones"] >= 2 or aspirante['entrevista'] <50 or aspirante['matematicas'] <40 or aspirante['lenguaje'] <40 or\
        aspirante['ingles'] <40:
            estado = 'NO ADMITIDO'
    if estado =='NO ADMITIDO' and puntaje>=70 and aspirante['entrevista'] >=65 and aspirante['sanciones'] <2 \
        and aspirante['matematicas'] >50 and aspirante['lenguaje'] >50 and aspirante['ingles'] >50:
        estado = 'ADMISION CONDICIONAL'

    

    

    # --------------------------------------------------------
    # 7. Determinar la beca
    # --------------------------------------------------------
    
    beca = aspirante['solicita_beca']

    if beca == True and puntaje >=90 and aspirante['estrato']<=3 and aspirante['matematicas'] >= 85 and aspirante['ingles'] >=85\
        and aspirante['sanciones'] == 0:
        por_beca = 'BECA COMPLETA'
    elif beca == True and puntaje >=82 and aspirante['estrato']<=4 and aspirante['matematicas'] >= 75 and aspirante['ingles'] >=85\
        and aspirante['sanciones'] <2:
        por_beca = 'BECA PARCIAL'
    else:
        por_beca = 'SIN BECA'
    

  

    # --------------------------------------------------------
    # 8. Determinar el nivel académico
    # --------------------------------------------------------

    if puntaje >= 85 and aspirante['matematicas'] >= 70 and aspirante['ingles'] >=70\
        and aspirante['lenguaje'] >=70:
            nivel = 'ALTO'
    elif puntaje >= 70 and aspirante['matematicas'] >= 55 and aspirante['ingles'] >=55\
        and aspirante['lenguaje'] >=55:
            nivel = 'MEDIO'
    else:
        nivel = 'BAJO'
    
    


    # --------------------------------------------------------
    # 9. Determinar si existe una alerta
    # --------------------------------------------------------

    if aspirante['matematicas'] <60 and aspirante['ingles'] <60\
        and aspirante['lenguaje'] <60 and aspirante['entrevista'] >=1:
            alerta = True
    else:
        alerta = False
            

    # Complete las condiciones correspondientes.


    # --------------------------------------------------------
    # 10. Construir el diccionario resultado
    # --------------------------------------------------------

    resultado = {
        "nombre": nombre,
        "puntaje": round(puntaje, 2),
        "estado": estado,
        "nivel": nivel,
        "beca": por_beca,
        "alerta": alerta
    }

    return resultado


# ============================================================
# ZONA DE PRUEBAS
# ============================================================

# ------------------------------------------------------------
# Caso de prueba - Ejercicio 1
# ------------------------------------------------------------

solicitud_1 = {
    "nombre": "Laura Gómez",
    "edad": 34,
    "ingresos": 8500000,
    "gastos": 2800000,
    "deudas": 1500000,
    "puntaje": 720,
    "moras": 0,
    "antiguedad": 4,
    "producto": "VEHICULO"
}


# ------------------------------------------------------------
# Caso de prueba - Ejercicio 2
# ------------------------------------------------------------

aspirante_1 = {
    "nombre": "Daniel Rojas",
    "matematicas": 88,
    "lenguaje": 74,
    "ingles": 91,
    "entrevista": 82,
    "estrato": 3,
    "sanciones": 0,
    "programa": "INGENIERIA",
    "solicita_beca": True
}


# ============================================================
# PRUEBAS
# ============================================================

# Descomente las siguientes instrucciones cuando haya
# implementado las funciones.

# resultado_credito = evaluar_credito(solicitud_1)
# print(resultado_credito)

# resultado_aspirante = evaluar_aspirante(aspirante_1)
# print(resultado_aspirante)


# ============================================================
# CASOS DE PRUEBA ADICIONALES
# ============================================================

# Cree al menos tres casos adicionales para cada ejercicio.
#
# Los casos deben comprobar:
#
# 1. Un resultado favorable.
# 2. Un resultado desfavorable.
# 3. Una excepción.
# 4. Una situación límite.
#
# Recuerde que NO debe utilizar ciclos para ejecutar
# los casos de prueba.
