def presentar_estudiante(primer_nombre: str, primer_apellido: str, codigo_uniandes: int, edad: int) -> str:
 """
 Genera una presentación en texto con los datos básicos de un estudiante de la Universidad de los Andes.
 Parámetros:
 primer_nombre (str): El primer nombre del estudiante.
 primer_apellido (str): El primer apellido del estudiante.
 codigo_uniandes (int): El código único de identificación del estudiante en la universidad.
 edad (int): La edad del estudiante.
 Retorno:
 str: Cadena con la presentación del estudiante.
 """
 # Cálculo de la edad estimada de graduación a partir de la edad actual
 edad_de_graduacion = edad + 4
 # Presentación en formato natural
 texto_de_presentacion = "Hola, mi nombre es " + primer_nombre + " " + primer_apellido + \
 ". Mi código institucional es " + str(codigo_uniandes) + \
 ". Actualmente tengo " + str(edad) + " años, " + \
 "y espero graduarme a mis " + str(edad_de_graduacion) + " años."

 return texto_de_presentacion



