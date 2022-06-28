from Bebida_ import Bebida

class BebidaAlcoholica(Bebida):
    def __init__(self, nombre, precio, tipo, grado):
        super().__init__(nombre, precio, tipo)
        self.grado = grado

    def imprimir_beb_alco(self):
        print(f'''Nombre: {self.nombre}
        Precio: {self.precio}
        Grado alcoholico: {self.grado}
        ''')
        
        