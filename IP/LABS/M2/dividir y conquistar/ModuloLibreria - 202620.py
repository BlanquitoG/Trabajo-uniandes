# -*- coding: utf-8 -*-
def crear_libro(nom: str, cod: str,autor: int, adp: int, cant: int, pdv: float, cpu: float)->dict:
    dic_libro = { "nombre": nom, 
                       "codigo": cod,  
                       "autor": autor, 
                       "añoPublicacion": adp,
                       "cantidad": cant,
                       "precio": pdv, 
                       "costoProduccion": cpu}
    return dic_libro

#PROGRAMA PRINCIPAL
libro1 = crear_libro("Harry Potter y la piedra filosofal", "HPJK1997", "J.K. Rowling", 1997, 200 , 25000, 9000)
libro2 = crear_libro("Los Juegos del Hambre", "JHSC2008", "Suzanne Collins", 2008, 100 , 27000, 12000)
libro3 = crear_libro("El Hobbit", "EHJR1937", "J.R.R tolkien",1937, 50 , 35000, 15000)
libro4 = crear_libro("Hamlet", "HWS1589", "William Shakespeare", 1589, 20 , 26000, 13000)

def mayor_ganancia (libro1: dict, libro2: dict, libro3: dict, libro4:dict)->dict:
    
        ganancia1 = libro1['precio'] - libro1['costoProduccion']
        ganancia2 = libro2['precio'] - libro2['costoProduccion']
        ganancia3 = libro3['precio'] - libro3['costoProduccion']
        ganancia4 = libro4['precio'] - libro3['costoProduccion']
        
        if ganancia1 > ganancia2 and ganancia1 > ganancia3 and ganancia1 > ganancia4:
            return libro1
        elif ganancia2 > ganancia1 and ganancia2 > ganancia3 and ganancia2 > ganancia4:
            return libro2
        elif ganancia3 > ganancia1 and  ganancia3 > ganancia2 and  ganancia3 > ganancia4:
            return libro3
        elif  ganancia4 > ganancia1 and ganancia4 > ganancia2 and ganancia4 > ganancia3:
            return libro4

print(mayor_ganancia(libro1, libro2, libro3, libro4))
'''
def hacer_pedido(libro1: dict, libro2: dict, libro3: dict, libro4: dict, libro: str) -> bool:
    
    if libro1['nombre'].lower() == libro.lower():
        if libro1['cantidad'] <= 50:
            libro1['cantidad'] = libro1['cantidad'] + 100
            return True
        else:
            return False
    elif libro2['nombre'].lower() == libro.lower():
        if libro2['cantidad'] <= 50:
            libro2['cantidad'] = libro2['cantidad'] + 100
            return True
        else:
            return False
    elif libro3['nombre'].lower() == libro.lower():
        if libro3['cantidad'] <= 50:
            libro3['cantidad'] = libro3['cantidad'] + 100
            return True
        else:
            return False
    elif libro4['nombre'].lower() == libro.lower():
        if libro4['cantidad'] <= 50:
            libro4['cantidad'] = libro4['cantidad'] + 100
            return True
        else:
            return False
    else:
        return False
'''
def  publicacion_antes_anio(libro1: dict, libro2: dict, libro3: dict, libro4: dict, anio:int)->dict:
    
    
    
    
    libro_publi= {}
    
    if libro1['añoPublicacion'] <= anio:
        libro_publi [libro1['nombre']]= libro1['añoPublicacion']
    if libro2['añoPublicacion'] <= anio:
        libro_publi [libro2['nombre']]= libro2['añoPublicacion']
    if libro3['añoPublicacion'] <= anio:
        libro_publi [libro3['nombre']]= libro3['añoPublicacion']
    if libro4['añoPublicacion'] <= anio:
        libro_publi [libro4['nombre']]=libro4['añoPublicacion']
    return libro_publi
    
print(publicacion_antes_anio(libro1, libro2, libro3, libro4, 2008))

def ganacias_venta_libro(libro1: dict, libro2: dict, libro3: dict, libro4: dict,nomb_lib: str)->dict:
    
    
    ganancia1 = (libro1['precio'] - libro1['costoProduccion']) * libro1['cantidad']
    ganancia2 = (libro2['precio'] - libro2['costoProduccion']) * libro2['cantidad']
    ganancia3 = (libro3['precio'] - libro3['costoProduccion']) * libro3['cantidad']
    ganancia4 = (libro4['precio'] - libro4['costoProduccion']) * libro4['cantidad']
    
    libro_gananc = {}
    
    if nomb_lib.lower() == libro1['nombre'].lower():
        libro_gananc [libro1['nombre']] = ganancia1
        
    if nomb_lib.lower() == libro2['nombre'].lower():
        libro_gananc [libro2['nombre']] = ganancia2
        
    if nomb_lib.lower() == libro3['nombre'].lower():
        libro_gananc [libro3['nombre']] = ganancia3
        
    if nomb_lib.lower() == libro4['nombre'].lower():
        libro_gananc [libro4['nombre']] = ganancia4
        
        
    return libro_gananc

def venta_por_mayor(libro1: dict, libro2: dict, libro3: dict, libro4: dict, nombre: str, cantidad: int) -> dict:
    
    if libro1['nombre'].lower() == nombre.lower():
        libro_encontrado = libro1
    elif libro2['nombre'].lower() == nombre.lower():
        libro_encontrado = libro2
    elif libro3['nombre'].lower() == nombre.lower():
        libro_encontrado = libro3
    elif libro4['nombre'].lower() == nombre.lower():
        libro_encontrado = libro4
    else:
        libro_encontrado = None
    
    resultado = {}
    
    if libro_encontrado is None:
        resultado['costo_total'] = 0
        resultado['descuento'] = 0
        return resultado
    
    porcentaje_comprado = cantidad / libro_encontrado['cantidad']
    
    if porcentaje_comprado > 0.25 and porcentaje_comprado < 0.5:
        descuento = 0.10
    elif porcentaje_comprado >= 0.5 and porcentaje_comprado < 0.75:
        descuento = 0.20
    elif porcentaje_comprado >= 0.75:
        descuento = 0.30
    else:
        descuento = 0.0
    
    costo_sin_descuento = libro_encontrado['precio'] * cantidad
    costo_total = costo_sin_descuento - (costo_sin_descuento * descuento)
    
    resultado['costo_total'] = costo_total
    resultado['descuento'] = descuento
    
    return resultado    
         
   
    
         
    
    
    
    
    
    
    
    
    
    