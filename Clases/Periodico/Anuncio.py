class Anuncio:
    def __init__(self, seccion, nombre, cedula, titulo, cuerpo):
        self.seccion = seccion
        self.nombre = nombre
        self.cedula = cedula
        self.titulo = titulo
        self.cuerpo = cuerpo

class AnunciosComerciales(Anuncio):
    def __init__(self, seccion, nombre, cedula, titulo):
        super().__init__(seccion, nombre, cedula, titulo, 'Comercial')

class AnunciosClasificados(Anuncio):
    def __init__(self, seccion, nombre, cedula, titulo, precio, fecha_publicacion, dias, tipo):
        super().__init__(seccion, nombre, cedula, titulo, 'Clasificado')
        self.precio = precio
        self.fecha_publicacion = fecha_publicacion
        self.dias = dias
        self.tipo = tipo

class AnuncioClasificadoVivienda(AnunciosClasificados):
    def __init__(self, seccion, nombre, cedula, titulo, precio, fecha_publicacion, dias, m2, cuartos, baños, puestos, politica_habitacional):
        super().__init__(seccion, nombre, cedula, titulo, precio, fecha_publicacion, dias, 'Vivienda')
        self.m2 = m2
        self.cuartos = cuartos
        self.baños = baños
        self.puestos = puestos
        self.politica_habitacional = politica_habitacional

class AnunciosClasificadoVehiculo(AnunciosClasificados):
    def __init__(self, seccion, nombre, cedula, titulo, precio, fecha_publicacion, dias, marca, modelo, año, kilometraje):
        super().__init__(seccion, nombre, cedula, titulo, precio, fecha_publicacion, dias, 'Vehiculo')
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje