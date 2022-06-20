class Plancha:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero
    
    def imprimir_plancha(self):
        print(f'''Nombre: {self.nombre}
        Numero: {self.numero}''')