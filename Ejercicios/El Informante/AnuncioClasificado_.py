from Anuncio_ import Anuncio

class AnuncioClasificado(Anuncio):
    def __init__(self, nombre, cedula, seccion, titulo, cuerpo, precio, fecha, duracion, tipo):
        super().__init__(nombre, cedula, seccion, titulo, cuerpo)
        self.precio = precio
        self.fecha = fecha
        self.duracion = duracion
        self.tipo = tipo