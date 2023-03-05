def raiz_cuadrada_entera(n):
    """
    Calcula la raíz cuadrada entera de un número entero.
    """
    if n < 0:
        raise ValueError("La raíz cuadrada no está definida para números negativos")
    if n == 0:
        return 0
    r = 1
    while r * r <= n:
        r += 1
    return r - 1
