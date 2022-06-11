from Participante_ import Participante

class Libre(Participante):
    def __init__(self, nombre, formato, categoria, telefono, registro, talento):
        super().__init__(nombre, formato, categoria, telefono, registro)
        self.talento = talento
    
    def imprimir_otros(self):
        print(f'''Talento: {self.talento}''')