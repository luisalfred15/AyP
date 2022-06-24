from Bebida_ import *

class BebidaNoAlcoholica(Bebida):
    def __init__(self, nombre, precio, temp):
        super().__init__(nombre, precio)
        self.temp = temp
    
    def imprimir_beb_no_alc(self):
        print(f'Nombre: {self.nombre}; Precio: {self.precio}')