def descomponer_cadena(cadena, separador):
    partes = []
    auxiliar = ''
    for caracter in cadena:
        if caracter == separador:
            partes.append(auxiliar)
            auxiliar = ''
        else:
            auxiliar += caracter
    partes.append(auxiliar)
    partes = [parte.strip() for parte in partes]
    return partes
