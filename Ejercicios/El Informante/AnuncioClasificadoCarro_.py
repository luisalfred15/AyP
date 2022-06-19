from statistics import mode
from AnuncioClasificado_ import AnuncioClasificado

class AnuncioClasificadoCarro(AnuncioClasificado):
    def __init__(self, nombre, cedula, seccion, titulo, cuerpo, precio, fecha, duracion, tipo, marca, modelo, año, color, kms):
        super().__init__(nombre, cedula, seccion, titulo, cuerpo, precio, fecha, duracion, tipo)
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.kms = kms