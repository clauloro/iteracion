ruta_archivo = '/etc/passwd'
usuarios_sin_descripcion = []

with open(ruta_archivo, 'r') as archivo:
    for linea in archivo:
        partes = linea.strip().split(':')
        usuario = partes[0]
        gcos = partes[4]
        if not gcos:
            usuarios_sin_descripcion.append(usuario)
if usuarios_sin_descripcion:
    print('Los siguientes usuarios no tienen descripción en el campo GCOS:')
    print('\n'.join(usuarios_sin_descripcion))
else:
    print('Todos los usuarios tienen una descripción en el campo GCOS.')

