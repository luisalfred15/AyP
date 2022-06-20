from JuntaDirectiva_ import *

class JuntaDirectivaGeneral(JuntaDirectiva):
    def __init__(self, presidente, coordinador_general, tesorero, plancha, sg, sai):
        super().__init__(presidente, coordinador_general, tesorero, plancha)
        self.sg = sg
        self.sai = sai

    def imprimir_jdg(self):
        print(f'''Presidente: {self.presidente}
        Coordinador General: {self.coordinador_general}
        Tesorero: {self.tesorero}
        Secretario General: {self.sg}
        Secretario Asuntos Internos: {self.sai}''')