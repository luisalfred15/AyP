class Cliente:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.pedido = []

    def imprimir_cliente(self):
        print(f'''Nombre: {self.nombre}
        Edad: {self.edad}
        Cedula: {self.cedula}''')