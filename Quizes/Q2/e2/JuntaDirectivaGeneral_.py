from JuntaDirectiva_ import JuntaDirectiva

class JuntaDirectivaGeneral(JuntaDirectiva):
    def __init__(self, tipo, num_plancha, presidente, coordinador_general, tesorero, sg, sai):
        super().__init__(tipo, num_plancha, presidente, coordinador_general, tesorero)
        self.sg = sg
        self.sai = sai
    
    def imprimir_jdg(self):
        print(f'''Tipo: E
        Presidente: {self.presidente}
        Coordinador General: {self.coordinador_general}
        Tesorero: {self.tesorero}
        Secretario General: {self.sg}
        Secretario Asuntos Internos: {self.sai}''')
        