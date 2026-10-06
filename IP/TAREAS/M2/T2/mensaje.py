def clasificar_mensaje(mensaje: str) -> str:
    
    mensaje_lower = mensaje.lower()
    
    categoria = {}
    
    categoria['Urgente'] = ("urgente", "inmediato", "emergencia")
    
    categoria['Trabajo'] = ("reunión", "proyecto", "informe", "tarea")
    
    categoria['Personal'] = ("amigo", "familia", "casa", "fiesta")
    
    categoria['Spam'] = ("oferta", "gratis", "descuento", "promoción")
    
    if categoria['Urgente'][0] in mensaje_lower or categoria['Urgente'][1] in mensaje_lower or categoria['Urgente'][2] in mensaje_lower:
        resultado = 'Categoría: Urgente - Prioridad: Alta'
    
    elif categoria['Trabajo'][0] in mensaje_lower or categoria['Trabajo'][1] in mensaje_lower or categoria['Trabajo'][2] in mensaje_lower\
        or categoria['Trabajo'][3] in mensaje_lower:
            resultado = 'Categoría: Trabajo - Prioridad: Media'
            
    elif categoria['Personal'][0] in mensaje_lower or categoria['Personal'][1] in mensaje_lower or categoria['Personal'][2] in mensaje_lower or\
        categoria['Personal'][3] in mensaje_lower:
            resultado = 'Categoría: Personal - Prioridad: Baja'
            
    elif categoria['Spam'][0] in mensaje_lower or categoria['Spam'][1] in mensaje_lower or categoria['Spam'][2] in mensaje_lower or\
        categoria['Spam'][3] in mensaje_lower:
            resultado = 'Categoría: Spam - Prioridad: Muy Baja'
    else:
        resultado = 'Categoría: Normal - Prioridad: Normal'
        
    return resultado