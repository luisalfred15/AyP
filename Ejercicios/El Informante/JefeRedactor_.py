from Empleado_ import Empleado
import random

class JefeRedactor(Empleado):
    def __init__(self, nombre, cedula, seccion):
        super().__init__(nombre, cedula, seccion)
    
    def supervisar_articulo():
        print('Articulo supervisado')
    
    def publicar_articulo():
        decision = random.randint(0, 1)
        if decision:
            return True
        else:
            return False