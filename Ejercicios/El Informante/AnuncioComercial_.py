from Anuncio_ import Anuncio

class AnuncioComercial(Anuncio):
    def __init__(self, nombre, cedula, seccion, titulo, cuerpo):
        super().__init__(nombre, cedula, seccion, titulo, cuerpo)