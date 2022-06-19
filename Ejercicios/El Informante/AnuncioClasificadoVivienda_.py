from AnuncioClasificado_ import AnuncioClasificado

class AnuncioClasificadoVivienda(AnuncioClasificado):
    def __init__(self, nombre, cedula, seccion, titulo, cuerpo, precio, fecha, duracion, tipo, m2, cuartos, baños, puestos_estaciona, politica_hab):
        super().__init__(nombre, cedula, seccion, titulo, cuerpo, precio, fecha, duracion, tipo)
        self.m2 = m2
        self.cuartos = cuartos
        self.baños = baños
        self.puestos_estaciona = puestos_estaciona
        self.politica_hab = politica_hab