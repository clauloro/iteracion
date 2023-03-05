class PERSONA:
    def __init__(self, identidad, edad, nombre, apellido, padre, madre):
        self.identidad = identidad
        self.edad = edad
        self.nombre = nombre
        self.apellido = apellido
        self.padre = padre
        self.madre = madre

familias = [PERSONA("VACÍO", 0, "", "", "HUÉRFANO", "HUÉRFANO")] * 1000

