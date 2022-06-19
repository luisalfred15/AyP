from JuntaDirectiva_ import JuntaDirectiva

class JuntaDirectivaEscuela(JuntaDirectiva):
    def __init__(self, tipo, num_plancha, presidente, coordinador_general, tesorero, escuela):
        super().__init__(tipo, num_plancha, presidente, coordinador_general, tesorero)
        self.escuela = escuela
    
    def imprimir_jde(self):
        print(f'''Tipo: G
        Presidente: {self.presidente}
        Coordinador General: {self.coordinador_general}
        Tesorero: {self.tesorero}
        Secretario General: {self.escuela}''')