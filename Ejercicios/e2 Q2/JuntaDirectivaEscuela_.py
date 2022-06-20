from JuntaDirectiva_ import *

class JuntaDirectivaEscuela(JuntaDirectiva):
    def __init__(self, presidente, coordinador_general, tesorero, plancha, escuela):
        super().__init__(presidente, coordinador_general, tesorero, plancha)
        self.escuela = escuela
    
    def imprimir_jde(self):
        print(f'''Presidente: {self.presidente}
        Coordinador General: {self.coordinador_general}
        Tesorero: {self.tesorero}
        Escuela: {self.escuela}''')