from Bebida_ import *

class BebidaAlcoholica(Bebida):
    def __init__(self, nombre, precio, grado_alco):
        super().__init__(nombre, precio)
        self.grado_alco = grado_alco
    
    def imprimir_beb_no_alc(self):
        print(f'Nombre: {self.nombre}; Precio: {self.precio}; Grado alcoholico: {self.grado_alco}')