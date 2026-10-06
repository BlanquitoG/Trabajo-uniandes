#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cupihabitat as ch


# Funciones auxiliares (NO MODIFICAR):

def mostrar_zona(zona: dict) -> None:
    """
    Muestra los atributos de una zona en la consola.

    Parámetros:
        zona (dict): Diccionario con la información de la zona de conservación.
    """
    if zona != {}:
        print("Nombre:", zona["nombre"])
        print("ID de Zona:", zona["id zona"])
        print("Área (ha):", zona["area de hectarea"])
        print("Ecosistema:", zona["tipo de ecosistema"])
        print("Fecha de registro:", zona["fecha de registro"])
        print("Departamento:", zona["departamento"])
        print("Especies endémicas:", zona["especies endemicas"])
        print("Índice de contaminación:", zona["indice de contaminacion"])
        print("Estado de conservación:", zona["estado de conservacion"])
        print("Tiene fuente hídrica:", zona["tiene fuente hidrica"])
        print("Presencia de comunidades:", zona["presencia de comunidades"])
        print("Tiene plan de manejo:", zona["tiene plan de manejo"])
        print("Amenaza de deforestación:", zona["tiene amenaza de deforestacion"])
        print("Es área protegida:", zona["el area es protegida"])
        print("Presupuesto anual:", zona["presuouesto anual"])
    else:
        print("Error: Zona inválida.")

# Fin de las funciones auxiliares


# Funciones a implementar (Solo aquellas con TODOs):

def ejecutar_buscar_por_id(z1: dict, z2: dict, z3: dict, z4: dict) -> None:
    """
    Ejecuta la búsqueda de una zona por su ID.

    Parámetros:
        z1, z2, z3, z4 (dict): Diccionarios con la información de las cuatro zonas.

    Si se encuentra la zona, se muestran todos sus datos usando la función auxiliar: `mostrar_zona()`.
    
    Si no se encuentra, se imprime el mensaje: "No se encontró ninguna zona con ese ID."
    """
    id_buscado = int(input("Ingrese el ID de la zona a buscar: "))
    resultado = ch.buscar_zona_por_id(id_buscado, z1, z2, z3, z4)
    if resultado != {}:
        mostrar_zona(resultado)
    else:
        print("No se encontro ninguna zona con ese ID.")


def ejecutar_filtrar_por_ecosistema(z1: dict, z2: dict, z3: dict, z4: dict) -> None:
    """
    Ejecuta el filtrado de zonas por tipo de ecosistema.

    Parámetros:
        z1, z2, z3, z4 (dict): Diccionarios con la información de las cuatro zonas.

    Si hay coincidencias, se imprime:
        "Zonas pertenecientes a [X]: [Y]"
        
        Donde:
            - [X] es el ecosistema buscado, ejemplo: "Páramo"
            - [Y] son los IDs de las zonas que pertenecen a ese ecosistema, en el orden z1 a z4,
                  separados por ", " (coma seguida de un espacio).
        
    Si no hay coincidencias, se imprime:
        "No se encontraron zonas para el ecosistema buscado."
    """
    
    
    ecosistema_buscadp = input('Ingrese el ecosistema a buscar: ')
    
    ecosistemas = ch.filtrar_por_ecosistema(ecosistema_buscadp, z1, z2, z3, z4)
    
    if ecosistemas != 'Ninguna':
        print(f'Las zonas que pertenecen a {ecosistema_buscadp} son: {ecosistemas} ')
    else:
        print(f'No hay ninguna zona perteneciente a {ecosistema_buscadp}')
    

def ejecutar_mayor_biodiversidad(z1: dict, z2: dict, z3: dict, z4: dict) -> None:
    """
    Ejecuta la búsqueda de la zona con la mayor biodiversidad (especies endémicas).

    Parámetros:
        z1, z2, z3, z4 (dict): Diccionarios con la información de las cuatro zonas.

    Se imprime el encabezado: "Zona con mayor biodiversidad (especies endémicas):"
        Luego se muestran todos los datos de la zona usando la función auxiliar: `mostrar_zona()`.
    """
    zona_mas_diversa = ch.mayor_biodiversidad(z1, z2, z3, z4)
    
    print(f'Zona con mayor biodiversidad (especies endémicas) es {zona_mas_diversa}')
    mostrar_zona(zona_mas_diversa)

def ejecutar_registro_mas_antiguo(z1: dict, z2: dict, z3: dict, z4: dict) -> None:
    """
    Ejecuta la búsqueda de la zona con el registro más antiguo.

    Parámetros:
        z1, z2, z3, z4 (dict): Diccionarios con la información de las cuatro zonas.

    Se imprime el encabezado: "Zona con el registro más antiguo:"
        Luego se muestran todos los datos de la zona usando la función auxiliar: `mostrar_zona()`.
    """
    mas_antiguo = ch.registro_mas_antiguo(z1, z2, z3, z4)
    
    print(f'Zona con el registro más antiguo: {mas_antiguo}')
    mostrar_zona(mas_antiguo)
    

def ejecutar_verificar_intervencion(z1: dict, z2: dict, z3: dict, z4: dict) -> None:
    """
    Ejecuta la verificación de si una zona requiere intervención urgente.

    Parámetros:
        z1, z2, z3, z4 (dict): Diccionarios con la información de las cuatro zonas.
        
    Se solicita al usuario el ID numérico de la zona que desea evaluar (número entero).

    Si la zona existe (se busca con la función: buscar_zona_por_id), se imprime uno de los siguientes mensajes:
        - "La zona SÍ requiere intervención urgente."
        - "La zona NO requiere intervención urgente."
        
    Si no se encuentra la zona, se imprime:
        "Zona no encontrada."
    """
    ID = int(input('Ingrese el ID de la zona: '))
        
    existe_id = ch.buscar_zona_por_id(ID, z1, z2, z3, z4) 
    
    if existe_id == z1 or z2 or z3 or z4:
        
        intervenir = ch.requiere_intervencion_urgente(existe_id)
    
        if intervenir == True:
            print(f'La zona SI requiere interverencion urgente')
        else:
            print('La zona NO requiere intervencion urgente')
    else:
        print(f'Zona no encontrada')
        


def ejecutar_recomendar_fondos(z1: dict, z2: dict, z3: dict, z4: dict) -> None:
    """
    Ejecuta la recomendación de la mejor zona para recibir fondos de conservación ambiental.

    Parámetros:
        z1, z2, z3, z4 (dict): Diccionarios con la información de las cuatro zonas.

    Se solicita al usuario un presupuesto máximo permitido para la ayuda (número flotante).

    Si el puntaje de prioridad de la zona recomendada es mayor que 0.0,
        Se imprime el encabezado: "Zona recomendada para recibir los fondos (puntaje: [X])"
        
            Donde:
                - [X] es el puntaje de la zona recomendada. 
        
        Y luego se muestran sus datos usando la función auxiliar: `mostrar_zona()`.
        
    Si el puntaje es 0.0, se imprime:
        "Ninguna zona cumple con los requerimientos mínimos para los fondos."
    
    El puntaje a tener en cuenta debe corresponder al puntaje de prioridad de la zona recomendada,
    calculado utilizando el mismo presupuesto máximo ingresado por el usuario.
    """
    max_presupuesto = float(input('Ponga su maximo presupuesto: '))
    
    zona = ch.recomendar_para_fondos(z1, z2, z3, z4, max_presupuesto)
    
    puntaje = ch.puntaje_prioridad_fondos(zona, max_presupuesto)
    
    if puntaje > 0.0:
        print(f'Zona recomendada para recibir los fondos {puntaje}')
    else:
        print(f'Ninguna zona cumple con los requerimientos mínimos para los fondos.')
    mostrar_zona(zona)

# Fin de las funciones a implementar


# Funciones del menú:

def imprimir_separador(simbolo: str, repeticiones: int) -> None:
    print(simbolo * repeticiones)


def iniciar_aplicacion() -> None:
    """
    Inicia la aplicación creando cuatro zonas predefinidas (z1, z2, z3 y z4) 
    utilizando la función crear_zona() de la lógica.
    
    Cada zona se crea con los argumentos definidos y el orden especificado
    por la función crear_zona() de la lógica.
    
    Para el detalle de cada parámetro, revise el docstring de crear_zona() en la lógica.

    Las cuatro zonas creadas son:

        - z1: Chingaza.
        - z2: Serranía de Chiribiquete.
        - z3: Ciénaga Grande.
        - z4: Santurbán.
    
    Usted puede modificar los datos de estas zonas para hacer más pruebas.
    """
    z1 = ch.crear_zona("Chingaza", 201, 76600.0, "Páramo", "2010-05-14", "Cundinamarca", 15, 30.0, "Estable", True, True, True, False, True, 1900.0)
    z2 = ch.crear_zona("Serranía de Chiribiquete", 202, 4268095.0, "Bosque Tropical", "1989-09-21", "Guaviare", 45, 10.0, "Vulnerable", True, True, True, True, True, 16000.0)
    z3 = ch.crear_zona("Ciénaga Grande", 203, 52800.0, "Humedal", "1998-03-10", "Magdalena", 8, 85.0, "Crítico", True, True, False, True, True, 31700.0)
    z4 = ch.crear_zona("Santurbán", 204, 142000.0, "Páramo", "2015-11-05", "Santander", 8, 45.0, "Crítico", True, True, False, False, True, 18000.0)

    imprimir_separador("*", 50)
    print("\nBienvenido a CupiHabitat\n")
    imprimir_separador("*", 50)
    print("\nZonas registradas:\n")
    imprimir_separador("-", 50)
    mostrar_zona(z1)
    imprimir_separador("-", 50)
    mostrar_zona(z2)
    imprimir_separador("-", 50)
    mostrar_zona(z3)
    imprimir_separador("-", 50)
    mostrar_zona(z4)
    imprimir_separador("-", 50)

    ejecutando = True
    while ejecutando:
        ejecutando = mostrar_menu_aplicacion(z1, z2, z3, z4)
        if ejecutando:
            input("\nPresione Enter para continuar...")

def mostrar_menu_aplicacion(z1: dict, z2: dict, z3: dict, z4: dict) -> bool:
    """
    Muestra el menú de opciones y ejecuta la opción seleccionada.

    Parámetros:
        z1, z2, z3, z4 (dict): Diccionarios con la información de las cuatro zonas.

    Retorna:
        bool: True si el programa debe seguir ejecutándose, False para terminar.
    """
    print("\nMenú:")
    print("1 - Buscar zona por ID")
    print("2 - Filtrar por tipo de ecosistema")
    print("3 - Zona con mayor biodiversidad")
    print("4 - Zona con el registro más antiguo")
    print("5 - Verificar si requiere intervención urgente")
    print("6 - Recomendar zona para fondos")
    print("7 - Salir\n")

    opcion = input("Seleccione una opción: ").strip()
    print("\n" + "-" * 50 + "\n")

    continuar_ejecutando = True

    if opcion == "1":
        ejecutar_buscar_por_id(z1, z2, z3, z4)
    elif opcion == "2":
        ejecutar_filtrar_por_ecosistema(z1, z2, z3, z4)
    elif opcion == "3":
        ejecutar_mayor_biodiversidad(z1, z2, z3, z4)
    elif opcion == "4":
        ejecutar_registro_mas_antiguo(z1, z2, z3, z4)
    elif opcion == "5":
        ejecutar_verificar_intervencion(z1, z2, z3, z4)
    elif opcion == "6":
        ejecutar_recomendar_fondos(z1, z2, z3, z4)
    elif opcion == "7":
        continuar_ejecutando = False
    else:
        print("Opción inválida. Intente nuevamente.")

    return continuar_ejecutando

if __name__ == "__main__":
    iniciar_aplicacion()

# Fin de las funciones del menú.