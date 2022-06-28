from Bebida_ import Bebida

class BebidaNoAlcoholica(Bebida):
    def __init__(self, nombre, precio, tipo, temp):
        super().__init__(nombre, precio, tipo)
        self.temp = temp
    
    def imprimir_beb_no_alco(self):
        print(f'''Nombre: {self.nombre}
        Precio: {self.precio}
        Temperatura de mantenimiento: {self.temp}
        ''')