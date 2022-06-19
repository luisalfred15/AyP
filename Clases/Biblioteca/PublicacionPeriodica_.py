from Publicacion_ import *

class PublicacionPeriodica(Publicacion):
    def __init__(self, nombre, autor, fecha_publicacion, tipo_publicacion):
        super().__init__(nombre, autor, fecha_publicacion, tipo_publicacion)
        self.tipo_publicacion = 'Publicacion periodica'