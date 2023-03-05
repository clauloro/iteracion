def baseB(n, B):
    if n == 0:
        return "0"
    resultado = ""
    while n > 0:
        resto = n % B
        if resto < 10:
            resultado = str(resto) + resultado
        else:
            resultado = chr(resto + 55) + resultado
        n //= B
    return resultado
