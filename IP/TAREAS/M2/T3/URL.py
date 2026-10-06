def formatear_url(url: str) -> str:
    
    # Paso 1: Validar la URL
    empieza_valido = url.startswith("http://") or url.startswith("https://")
    
    # Quito la barra final (si existe) solo para poder extraer bien la extensión
    url_temp = url[:-1] if url.endswith("/") else url
    
    extension = "." + url_temp.split(".")[-1]
    extensiones_validas = (".com", ".org", ".net", ".edu")
    
    if not empieza_valido or extension.lower() not in extensiones_validas:
        return "URL no válida"
    
    # Paso 2: Formatear la URL
    url_formateada = url.lower()
    
    if url_formateada.endswith("/"):
        url_formateada = url_formateada[:-1]
    
    if url_formateada.startswith("http://"):
        url_formateada = "https://" + url_formateada[len("http://"):]
    
    if url_formateada.startswith("https://www."):
        url_formateada = "https://" + url_formateada[len("https://www."):]
    
    return url_formateada