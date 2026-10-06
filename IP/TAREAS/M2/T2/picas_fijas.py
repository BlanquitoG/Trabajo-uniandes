

def picas_y_fijas(numero_secreto: int, intento: int)-> dict:
    
    inte= str(intento)
    secreto = str(numero_secreto)
    
    fijas = (inte[0] == secreto[0]) +(inte[1] == secreto[1]) + (inte[2] == secreto[2])\
        +(inte[3] == secreto[3])
    total_coincididas = (inte[0] in secreto) + (inte[1] in secreto) + (inte[2] in secreto) +\
        (inte[3] in secreto)
    
    picas_total = total_coincididas - fijas
    
    fi_pi = {}
    
    fi_pi ['PICAS'] = picas_total
    
    fi_pi ['FIJAS'] = fijas
    
            
    
    return fi_pi