from Participante_ import Participante

class Bailarin(Participante):
    def __init__(self, nombre, formato, categoria, telefono, registro, estilo):
        super().__init__(nombre, formato, categoria, telefono, registro)
        self.estilo = estilo
    
    def imprimir_otros(self):
        print(f'''Estilo: {self.estilo}''')