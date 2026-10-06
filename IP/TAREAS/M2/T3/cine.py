def calcular_costo_boletas(cantidad_boletas: int, tipo_sala: str, hora_pico: bool, pago_tarjeta_cinema: bool, reserva: bool) -> int:
    
    tipo_sala_lower = tipo_sala.lower()
    
    if tipo_sala_lower == 'dinamix':
        tarifa_basica = 18800
    elif tipo_sala_lower == '3d':
        tarifa_basica = 15500
    elif tipo_sala_lower == '2d':
        tarifa_basica = 11300
    else:
        return -1  # valor centinela para sala inválida (ver nota abajo)
    
    # Promoción 1: descuento en horas no pico
    descuento_no_pico = 0
    if not hora_pico:
        descuento_no_pico = tarifa_basica * 0.10
        if cantidad_boletas >= 3:
            descuento_no_pico = descuento_no_pico + 500
    
    # Promoción 2: descuento por pago con tarjeta del cine
    descuento_tarjeta = tarifa_basica * 0.05 if pago_tarjeta_cinema else 0
    
    # Promoción 3: recargo por reserva
    recargo_reserva = 2000 if reserva else 0
    
    # Promoción 4: incremento en hora pico
    if hora_pico:
        if tipo_sala_lower == 'dinamix':
            incremento = tarifa_basica * 0.50
        else:
            incremento = tarifa_basica * 0.25
    else:
        incremento = 0
    
    precio_por_boleta = tarifa_basica + incremento - descuento_no_pico - descuento_tarjeta + recargo_reserva
    
    costo_total = precio_por_boleta * cantidad_boletas
    
    return round(costo_total)