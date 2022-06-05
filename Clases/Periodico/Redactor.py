from Seccion import Seccion

class Empleado:
    def __init__(self, nombre, cedula, seccion):
        self.nombre = nombre
        self.cedula = cedula
        self.seccion = seccion


class RedactorJefe(Empleado):
    def __init__(self, nombre, cedula, seccion):
        super().__init__(nombre, cedula, seccion)
    
    def decidir_publicacion()

class Redactor(Empleado):
    def __init__(nombre, cedula, seccion, redactores):
        super().__init__(nombre, cedula, seccion)
        self.redactores = list(redactores)
    
    def escribir_articulo()