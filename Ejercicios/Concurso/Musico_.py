from Participante_ import Participante

class Musico(Participante):
    def __init__(self, nombre, formato, categoria, telefono, registro, instrumentos):
        super().__init__(nombre, formato, categoria, telefono, registro)
        self.instrumentos = instrumentos
    
    def imprimir_otros(self):
        var = ''
        for index in range(len(self.instrumentos)):
            if index == len(self.instrumentos) - 1:
                var += self.instrumentos[index]
            else:
                var += self.instrumentos[index] + ', '
        return print(f'        Instrumentos: {var}')