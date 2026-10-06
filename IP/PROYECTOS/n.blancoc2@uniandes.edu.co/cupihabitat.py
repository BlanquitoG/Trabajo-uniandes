#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def crear_zona(
    nombre: str,
    id_zona: int,
    area_hectareas: float,
    tipo_ecosistema: str,
    fecha_registro: str,
    departamento: str,
    especies_endemicas: int,
    indice_contaminacion: float,
    estado_conservacion: str,
    tiene_fuente_hidrica: bool,
    presencia_comunidades: bool,
    tiene_plan_manejo: bool,
    amenaza_deforestacion: bool,
    es_area_protegida: bool,
    presupuesto_anual: float
) -> dict:
    """
    Crea y retorna un diccionario que representa una zona de conservación. 
        Cada atributo de la zona se almacena como un par llave-valor.
    
    Las llaves del diccionario retornado coinciden exactamente con los nombres de los parámetros.
    
    Parámetros:
        nombre (str): Nombre completo de la zona de conservación. Ejemplo: "Chingaza".
        id_zona (int): Identificador numérico de la zona de conservación. Ejemplo: 201.
        area_hectareas (float): Cantidad de hectáreas que posee una zona de conservación. Ejemplo: 76600.0.
        tipo_ecosistema (str): Tipo de ecosistema presente en la zona de conservación. Puede ser "Páramo", "Bosque Tropical", "Humedal" o "Sabana". Ejemplo: "Páramo".
        fecha_registro (str): Fecha en que se registró la zona en formato "YYYY-MM-DD". Ejemplo: "2010-05-14".
        departamento (str): Departamento donde se encuentra la zona. Ejemplo: "Cundinamarca".
        especies_endemicas (int): Número de especies endémicas registradas en la zona. Ejemplo: 15.
        indice_contaminacion (float): Nivel de contaminación de la zona. Número de 0.0 a 100.0. Ejemplo: 30.0.
        estado_conservacion (str): Estado actual de conservación de la zona. Puede ser "Estable", "Crítico" o "Vulnerable". Ejemplo: "Estable".
        tiene_fuente_hidrica (bool): Indica si la zona cuenta con cuerpos de agua o fuentes hídricas importantes. Ejemplo: True.
        presencia_comunidades (bool): Indica si habitan comunidades en la zona. Ejemplo: True.
        tiene_plan_manejo (bool): Indica si la zona cuenta con un plan de manejo ambiental aprobado. Ejemplo: True.
        amenaza_deforestacion (bool): Indica si la zona enfrenta un riesgo inminente de deforestación. Ejemplo: False.
        es_area_protegida (bool): Indica si la zona ha sido declarada formalmente como área protegida. Ejemplo: True.
        presupuesto_anual (float): Presupuesto anual asignado para el manejo de la zona en millones de pesos. Ejemplo: 1900.0.

    Retorna:
        dict: Diccionario que representa a la zona de conservación, con las llaves coincidiendo con los nombres de los parámetros.
    """
    # TODO 1: Implemente la función tal y como se describe en la documentación.
    zona = {}

    zona['nombre'] = nombre
    zona['id zona'] = id_zona
    zona['area de hectarea'] = area_hectareas
    zona['tipo de ecosistema'] = tipo_ecosistema
    zona['fecha de registro'] = fecha_registro
    zona['departamento'] = departamento
    zona['especies endemicas'] = especies_endemicas
    zona['indice de contaminacion'] = indice_contaminacion
    zona['estado de conservacion'] = estado_conservacion
    zona['tiene fuente hidrica'] = tiene_fuente_hidrica
    zona['presencia de comunidades'] = presencia_comunidades
    zona['tiene plan de manejo'] = tiene_plan_manejo
    zona['tiene amenaza de deforestacion'] = amenaza_deforestacion
    zona['el area es protegida'] = es_area_protegida
    zona['presuouesto anual'] = presupuesto_anual
    
    return zona







def buscar_zona_por_id(id_buscado: int, z1: dict, z2: dict, z3: dict, z4: dict) -> dict:
    """
    Retorna el diccionario de la zona cuyo identificador numérico coincida exactamente con el valor buscado.

    Parámetros:
        id_buscado (int): Número exacto del ID de la zona a buscar.
        z1 (dict): Diccionario que representa la primera zona.
        z2 (dict): Diccionario que representa la segunda zona.
        z3 (dict): Diccionario que representa la tercera zona.
        z4 (dict): Diccionario que representa la cuarta zona.

    Retorna:
        dict: Diccionario correspondiente a la zona con el ID coincidente o diccionario vacío si no hay coincidencia.
    """
    # TODO 2: Implemente la función tal y como se describe en la documentación.
    if z1['id zona'] == id_buscado:
        return z1
    elif z2['id zona'] == id_buscado:
        return z2
    elif z3['id zona'] == id_buscado:
        return z3
    elif z4['id zona'] == id_buscado:
        return z4
    else:
        return {}


def filtrar_por_ecosistema(ecosistema_buscado: str, z1: dict, z2: dict, z3: dict, z4: dict) -> str:
    """
    Filtra las zonas cuyo tipo de ecosistema coincida exactamente con el buscado.
    La comparación es sensible a mayúsculas, minúsculas y caracteres especiales. 
        Por ejemplo, "Páramo" coincide con "Páramo", pero no con "páramo".    
    Retorna una cadena de caracteres con los IDs de las zonas filtradas en el orden z1 a z4,
    separados por ", " (coma seguida de un espacio).
    
    Parámetros:
        ecosistema_buscado (str): Nombre exacto del ecosistema a buscar. Ejemplo: "Páramo".
        z1 (dict): Diccionario que representa la primera zona.
        z2 (dict): Diccionario que representa la segunda zona.
        z3 (dict): Diccionario que representa la tercera zona.
        z4 (dict): Diccionario que representa la cuarta zona.

    Retorna:
        str: Cadena de caracteres con los IDs de las zonas filtradas o "Ninguna" si no hay coincidencias.
    """
    # TODO 3: Implemente la función tal y como se describe en la documentación.
    ids_encontrados = ""
    
    if z1['tipo de ecosistema'] == ecosistema_buscado:
        ids_encontrados = ids_encontrados + str(z1['id zona'])
    
    if z2['tipo de ecosistema'] == ecosistema_buscado:
        if ids_encontrados == "":
            ids_encontrados = str(z2['id zona'])
        else:
            ids_encontrados = ids_encontrados + ", " + str(z2['id zona'])
    
    if z3['tipo de ecosistema'] == ecosistema_buscado:
        if ids_encontrados == "":
            ids_encontrados = str(z3['id zona'])
        else:
            ids_encontrados = ids_encontrados + ", " + str(z3['id zona'])
    
    if z4['tipo de ecosistema'] == ecosistema_buscado:
        if ids_encontrados == "":
            ids_encontrados = str(z4['id zona'])
        else:
            ids_encontrados = ids_encontrados + ", " + str(z4['id zona'])
    
    if ids_encontrados == "":
        return "Ninguna"
    else:
        return ids_encontrados

def mayor_biodiversidad(z1: dict, z2: dict, z3: dict, z4: dict) -> dict:
    """
    Retorna el diccionario de la zona con la mayor cantidad de especies endémicas.

    Parámetros:
        z1 (dict): Diccionario que representa la primera zona.
        z2 (dict): Diccionario que representa la segunda zona.
        z3 (dict): Diccionario que representa la tercera zona.
        z4 (dict): Diccionario que representa la cuarta zona.

    Retorna:
        dict: Diccionario correspondiente a la zona con el mayor número de especies endémicas.
            En caso de empate, retorna la última zona evaluada que alcanza esa cantidad máxima en el orden z1 a z4.
    """
    # TODO 4: Implemente la función tal y como se describe en la documentación.
    mejor_zona = z1
    
    if z2['especies endemicas'] >= mejor_zona['especies endemicas']:
        mejor_zona = z2
    
    if z3['especies endemicas'] >= mejor_zona['especies endemicas']:
        mejor_zona = z3
    
    if z4['especies endemicas'] >= mejor_zona['especies endemicas']:
        mejor_zona = z4
    
    return mejor_zona
    
    
    
    


def registro_mas_antiguo(z1: dict, z2: dict, z3: dict, z4: dict) -> dict:
    """
    Retorna el diccionario de la zona con la fecha de registro más antigua.

    Notas:
        - Las fechas de registro ("fecha_registro") siempre están en el formato "YYYY-MM-DD" (Año-Mes-Día).
        
          En Python, este formato permite que las fechas puedan compararse directamente como strings, 
          ya que el orden lexicográfico coincide con el orden cronológico.
        
          Ejemplos de comparaciones:
              "2005-02-15" < "2006-06-10"  # → True (Porque 2005 es anterior a 2006)
              "2010-08-23" > "2009-12-31"  # → True (Porque 2010 es posterior a 2009)
              "2015-03-10" < "2015-03-20"  # → True (Mismo año y mes, pero el día 10 es anterior al día 20)
                      
    Parámetros:
        z1 (dict): Diccionario que representa la primera zona.
        z2 (dict): Diccionario que representa la segunda zona.
        z3 (dict): Diccionario que representa la tercera zona.
        z4 (dict): Diccionario que representa la cuarta zona.

    Retorna:
        dict: Diccionario correspondiente a la zona con la fecha de registro más antigua.
            En caso de empate, retorna la primera zona que tenga dicha fecha en el orden z1 a z4.

    """
    # TODO 5: Implemente la función tal y como se describe en la documentación.
    mas_antiguo = z1

    if z2['fecha de registro'] < mas_antiguo['fecha de registro']:
        mas_antiguo = z2
        
    if z3['fecha de registro'] < mas_antiguo['fecha de registro']:
        mas_antiguo = z3
            
    if z4['fecha de registro'] < mas_antiguo['fecha de registro']:
        mas_antiguo = z4

    return mas_antiguo

def requiere_intervencion_urgente(zona: dict) -> bool:
    """
    Determina si la zona requiere intervención urgente basándose en su estado de conservación y nivel de contaminación.
    
    Condiciones excluyentes para requerir intervención:
        - Estado de conservación es "Crítico" y su índice de contaminación es igual o mayor a 40.0.
        - Estado de conservación es "Vulnerable" y su índice de contaminación es igual o mayor a 70.0.
        
    Debe usar únicamente operadores lógicos (and, or, not), sin usar estructuras condicionales.

    Parámetros:
        zona (dict): Diccionario que representa la zona a evaluar.

    Retorna:
        bool: True si la zona requiere intervención urgente, False en caso contrario.
    """
    # TODO 6: Implemente la función tal y como se describe en la documentación.
    critico = zona['indice de contaminacion'] >= 40 and zona['estado de conservacion'] == 'Crítico'
    
    vulerable = zona['indice de contaminacion'] >= 70 and zona['estado de conservacion'] == 'Vulnerable'
    
    intervencion = critico or vulerable
    
    return intervencion    

def puntaje_prioridad_fondos(zona: dict, max_presupuesto: float) -> float:
    """
    Calcula un puntaje de prioridad para que la zona reciba fondos de conservación ambiental con base en ciertas condiciones.
    
    El cálculo se realiza de acuerdo con las siguientes reglas:
    
    1. Si la zona no es un área protegida o no requiere intervención urgente, su puntaje es 0.0.
        
    2. Caso contrario, el puntaje inicia en 0.0 y se suman 0.2 puntos por cada una de las siguientes condiciones que se cumplan:
        - Tiene fuente hídrica.
        - Hay presencia de comunidades.
        - Existe amenaza de deforestación.
        - Tiene más de 10 especies endémicas.
        - Su presupuesto anual actual es menor o igual al presupuesto máximo permitido que se recibe por parámetro.

    Parámetros:
        zona (dict): Diccionario que representa la zona a evaluar.
        max_presupuesto (float): Presupuesto máximo permitido para considerar a una zona para los fondos.

    Retorna:
        float: Puntaje de prioridad para fondos de conservación (entre 0.0 y 1.0), redondeado a dos decimales.
    """
    puntaje = 0
    # TODO 7: Implemente la función tal y como se describe en la documentación.
    if zona['el area es protegida'] != True or requiere_intervencion_urgente(zona) == False:
        puntaje = 0
    if zona['tiene fuente hidrica'] == True:
        puntaje += 0.2
    if zona['presencia de comunidades'] == True:
        puntaje += 0.2
    if zona['tiene amenaza de deforestacion'] == True:
        puntaje += 0.2
    if zona['especies endemicas'] >10:
        puntaje += 0.2
    if zona['presuouesto anual'] <= max_presupuesto :
        puntaje += 0.2
    return round(puntaje,2)


def recomendar_para_fondos(z1: dict, z2: dict, z3: dict, z4: dict, max_presupuesto: float) -> dict:
    """
    Evalúa cuatro zonas de conservación y retorna la recomendada para recibir fondos basándose en su puntaje de prioridad.
    
    Nota:
        - La función siempre debe retornar una de las cuatro zonas siguiendo los criterios de selección y desempate establecidos, 
        incluso cuando todas tengan un puntaje de 0.0. Determinar si la zona retornada cumple los requisitos mínimos
        para recibir fondos será responsabilidad de la función de consola correspondiente.

    Parámetros:
        z1 (dict): Diccionario que representa la primera zona.
        z2 (dict): Diccionario que representa la segunda zona.
        z3 (dict): Diccionario que representa la tercera zona.
        z4 (dict): Diccionario que representa la cuarta zona.
        max_presupuesto (float): Presupuesto máximo permitido para ser considerado en la ayuda.

    Retorna:
        dict: Zona con mayor prioridad para recibir los fondos ambientales.

            En caso de empate:
            - Se prioriza la zona con mayor cantidad de especies endémicas.
            - Si persiste el empate, se prioriza la zona con menor presupuesto anual.
            - Si aún persiste el empate, se retorna la primera zona evaluada según el orden z1, z2, z3 y z4.
    """
    # TODO 8: Implemente la función tal y como se describe en la documentación.
    puntaje1 = puntaje_prioridad_fondos(z1, max_presupuesto)
    puntaje2 = puntaje_prioridad_fondos(z2, max_presupuesto)
    puntaje3 = puntaje_prioridad_fondos(z3, max_presupuesto)
    puntaje4 = puntaje_prioridad_fondos(z4, max_presupuesto)
    
    mejor_zona = z1
    mejor_puntaje = puntaje1
    
    # Comparar z2
    if puntaje2 > mejor_puntaje:
        mejor_zona = z2
        mejor_puntaje = puntaje2
    elif puntaje2 == mejor_puntaje:
        if z2['especies endemicas'] > mejor_zona['especies endemicas']:
            mejor_zona = z2
        elif z2['especies endemicas'] == mejor_zona['especies endemicas']:
            if z2['presuouesto anual'] < mejor_zona['presuouesto anual']:
                mejor_zona = z2
    if puntaje3 > mejor_puntaje:
        mejor_zona = z3
        mejor_puntaje = puntaje3
    elif puntaje3 == mejor_puntaje:
        if z3['especies endemicas'] > mejor_zona['especies endemicas']:
            mejor_zona = z3
        elif z3['especies endemicas'] == mejor_zona['especies endemicas']:
            if z3['presuouesto anual'] < mejor_zona['presuouesto anual']:
                mejor_zona = z3
    if puntaje4 > mejor_puntaje:
        mejor_zona = z4
        mejor_puntaje = puntaje4
    elif puntaje4 == mejor_puntaje:
        if z4['especies endemicas'] > mejor_zona['especies endemicas']:
            mejor_zona = z4
        elif z4['especies endemicas'] == mejor_zona['especies endemicas']:
            if z4['presuouesto anual'] < mejor_zona['presuouesto anual']:
                mejor_zona = z4
    
    return mejor_zona