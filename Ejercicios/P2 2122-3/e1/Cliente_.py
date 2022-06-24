class Cliente:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = int(edad)
        self.pedido = []
    
    #def añadir_pedido():
    
    def imprimir_cliente(self):
        print(f'Nombre: {self.nombre}; Cedula: {self.cedula}; Edad: {self.edad}')
