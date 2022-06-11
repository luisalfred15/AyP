from Participante_ import Participante

class Cantante(Participante):
    def __init__(self, nombre, formato, categoria, telefono, registro, cancion, autor):
        super().__init__(nombre, formato, categoria, telefono, registro)
        self.cancion = cancion
        self.autor = autor
    
    def imprimir_otros(self):
        print(f'''Cancion: {self.cancion}
        Autor: {self.autor}''')