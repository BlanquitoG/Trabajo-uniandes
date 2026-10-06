def desperdicio_de_gaseosa(amigo_1, amigo_2, amigo_3, capacidad_boton):
    if amigo_1["capacidad_actual"] + capacidad_boton > amigo_1["capacidad_vaso"]:
        return amigo_1["nombre"]
    elif amigo_2["capacidad_actual"] + capacidad_boton > amigo_2["capacidad_vaso"]:
        return amigo_2["nombre"]
    elif amigo_3["capacidad_actual"] + capacidad_boton > amigo_3["capacidad_vaso"]:
        return amigo_3["nombre"]
    else:
        return "Sin derrames"