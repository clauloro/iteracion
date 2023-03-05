def cuadrados_perfectos(limite):
    cuadrados = []
    suma = 0
    impar = 1
    while suma <= limite:
        cuadrado = suma
        cuadrados.append(cuadrado)
        impar += 2
        suma += impar
    return cuadrados

